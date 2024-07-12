from datetime import datetime

from flask import jsonify, Blueprint, request, json
from Resources.database.connectionbd import connectionb

receptor_bpost = Blueprint('ms_injectionPost', __name__)


class InjectionPostController:
    @receptor_bpost.route('/api/ms/postDatos', methods=['POST'])
    def IngresoDatos():
        try:
            if request.method == "POST":
                db = connectionb()
                db.connect()
                diccionarioDatos = request.json

                def convert_to_date(date_str):
                    try:
                        return datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
                    except ValueError:
                        return datetime.strptime(date_str, "%Y-%m-%d")

                # Crear el diccionario base para insertar datos
                data_to_insert = {
                    "IDREGISTRO": diccionarioDatos.get('Id Registro'),
                    "FGENERACIONREGISTRO": convert_to_date(diccionarioDatos.get('Fecha Generacion Registro')),
                    "NOMBREPROMOCION": diccionarioDatos.get('Nombre Promocion'),
                    "FINICIOCONTRATACION": convert_to_date(diccionarioDatos.get('Fecha Inicio Promocion')),
                    "FFINCONTRATACION": convert_to_date(diccionarioDatos.get('Fecha Finalizacion Promocion')),
                    "FFINANTICIPADACONTRATACION": None,
                    "ISVALID": 'Y',
                    "PRODUCTOID": int(diccionarioDatos.get('Producto_Id', 0)),
                    "VARIANTID": int(diccionarioDatos.get('Variant_Id', 0)),
                    "REDID": None,
                    "CANALID": int(diccionarioDatos.get('CanalId', 0)),
                    "EXCEPCION": None,
                    "MESINICIOPROMOCION": int(diccionarioDatos.get('Mes Inicio Promocion', 0)),
                    "MESFINPROMOCION": int(diccionarioDatos.get('Mes Fin Promocion', 0)),
                    "FFINPROMOCION": None,
                    "DIASGOZADOS": diccionarioDatos.get('Dias Gozados'),
                    "PRECIOPROMOCIONAL": float(diccionarioDatos.get('Precio Promocional', 0.0)),
                    "PRECIOREFERENCIAL": float(diccionarioDatos.get('Precio Referencial', 0.0)),
                    "FCADUCIDADANTICIPADAREGISTRO": None,
                    "BURO": ','.join(map(str, diccionarioDatos.get('Buro', []))),
                    "FORMADEPAGO": ','.join(map(str, diccionarioDatos.get('Forma de Pago', []))),
                    "ENTIDADBANCARIA": None,
                    "EMISORTARJETA": None,
                    "CIUDADES": ','.join(map(str, diccionarioDatos.get('Ciudades', []))),
                    "SECTORES": json.dumps(diccionarioDatos.get('Sectores', [])),
                    "SUBSECTORES": json.dumps(diccionarioDatos.get('Subsectores', [])),
                    "UPGRADE": None,
                    "PRODUCTOSADICIONALES": None
                }

                # Convertir el diccionario a una consulta SQL
                def generar_query(data):
                    columns = ', '.join(data.keys())
                    values_list = []
                    for v in data.values():
                        if v is None:
                            values_list.append('NULL')
                        elif isinstance(v, str):
                            # Reemplazar comillas simples en el valor de la cadena
                            sanitized_value = v.replace("'", "''")
                            values_list.append("'{}'".format(sanitized_value))
                        elif isinstance(v, (int, float)):
                            values_list.append(str(v))
                        elif isinstance(v, datetime):
                            formatted_date = v.strftime('%Y-%m-%d %H:%M:%S')
                            values_list.append("TO_DATE('{}', 'YYYY-MM-DD HH24:MI:SS')".format(formatted_date))
                        elif isinstance(v, list) or isinstance(v, dict):
                            json_value = json.dumps(v).replace("'", "''")
                            values_list.append("'{}'".format(json_value))
                    values = ', '.join(values_list)
                    squery = "INSERT INTO YTBL_EXAMPLETABLEBD ({}) VALUES ({})".format(columns, values)
                    return squery

                # Manejar el campo UPGRADE si existe
                if 'UPGRADE' in diccionarioDatos:
                    data_to_insert['UPGRADE'] = json.dumps(diccionarioDatos['UPGRADE'])

                # Consultar si existen productos adicionales
                productos_adicionales = ['TELEFONIA', 'TELEVISION', 'ROUTER', 'STREAMING']
                hay_productos_adicionales = any(producto in diccionarioDatos for producto in productos_adicionales)

                if not hay_productos_adicionales:
                    # Generar y ejecutar el query si no hay productos adicionales
                    query = generar_query(data_to_insert)
                    success = db.insert_data(query)

                    if not success:
                        return jsonify({'Error': 'Error al insertar datos en la tabla principal.'}), 400
                else:
                    # Manejar los productos adicionales si existen
                    for producto in productos_adicionales:
                        if producto in diccionarioDatos:
                            # Insertar datos para cada producto adicional
                            data_to_insert['PRODUCTOSADICIONALES'] = json.dumps(diccionarioDatos[producto])

                            # Generar y ejecutar el query
                            query = generar_query(data_to_insert)
                            success = db.insert_data(query)
                            if not success:
                                return jsonify({'Error': 'Error al insertar datos en la tabla principal.'}), 400

                            # Limpiar el campo de PRODUCTOSADICIONALES para el siguiente producto
                            data_to_insert['PRODUCTOSADICIONALES'] = None

                # Cerrar la conexión a la base de datos
                db.close()
                return jsonify({'Message': 'Datos insertados exitosamente.'}), 200
        except Exception as e:
            print("--------------------------------------------------------------------")
            print("FASE DE ESCUCHA - InjectionPostController | Error detectado: ", e)
            print("--------------------------------------------------------------------")
            return jsonify({'Error': str(e)}), 400
