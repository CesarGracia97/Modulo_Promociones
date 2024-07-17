from datetime import datetime
from flask import jsonify, Blueprint, request, json
from Resources.database.connectionbd import connectionb

receptor_bpost = Blueprint('ms_injectionPost', __name__)


class InjectionPostController:
    @receptor_bpost.route('/api/ms/postDatos', methods=['POST'])
    def IngresoDatos():
        try:
            if request.method == "POST":
                diccionarioDatos = request.json

                # Crear la conexión a la base de datos
                db = connectionb()
                db.connect()

                # Generar el valor para IDREGISTRO
                id_registro = generate_id_registro(diccionarioDatos.get('Id Registro'),
                                                   diccionarioDatos.get('Fecha Generacion Registro'))

                # Preparar el diccionario de datos para la tabla principal
                data_to_insert = moduloprin_data(diccionarioDatos, id_registro)

                # Generar y ejecutar el query para la tabla principal
                query = generate_query_modpromo(data_to_insert)
                success = db.insert_data(query)

                if not success:
                    db.close()
                    return jsonify({'Error': 'Error al insertar datos en la tabla principal.'}), 400

                # Insertar datos en la tabla de promociones adicionales
                success = handle_promociones_adicionales(db, diccionarioDatos, id_registro)

                # Cerrar la conexión a la base de datos
                db.close()

                if not success:
                    return jsonify({'Error': 'Error al insertar datos en la tabla de promociones adicionales.'}), 400

                return jsonify({'Message': 'Datos insertados exitosamente.'}), 200
        except Exception as e:
            print("--------------------------------------------------------------------")
            print("FASE DE ESCUCHA - InjectionPostController | Error detectado: ", e)
            print("--------------------------------------------------------------------")
            return jsonify({'Error': str(e)}), 400


def convert_to_date(date_str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        return datetime.strptime(date_str, "%Y-%m-%d")


def generate_id_registro(id_registro, fecha_generacion_registro):
    fecha_obj = convert_to_date(fecha_generacion_registro)
    fecha_str = fecha_obj.strftime('%d%m%y:%H%M')
    return f"MODP-{id_registro}-{fecha_str}"


def moduloprin_data(diccionarioDatos, id_registro):
    return {
        "IDREGISTRO": id_registro,
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
        "MESFINPROMOCION": diccionarioDatos.get('Mes Fin Promocion'),
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
        "UPGRADE": json.dumps(diccionarioDatos.get('UPGRADE', None))
    }


def generate_query_modpromo(data):
    columns = ', '.join(data.keys())
    values_list = []
    for v in data.values():
        if v is None:
            values_list.append('NULL')
        elif isinstance(v, str):
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
    squery = "INSERT INTO YTBL_MODULOPROMOPRIN ({}) VALUES ({})".format(columns, values)
    return squery


def handle_promociones_adicionales(db, diccionarioDatos, id_registro):
    productos_adicionales = ['STREAMING', 'TELEVISION', 'TELEFONIA', 'ROUTER']
    for producto in productos_adicionales:
        if producto in diccionarioDatos:
            if producto == 'STREAMING':
                for streaming_data in diccionarioDatos['STREAMING']:
                    data_to_insert = {
                        "IDREGISTRO": id_registro,
                        "PRODUCTO": 'STREAMING',
                        "PLANPAQUETEMODELO": streaming_data.get('Paquete'),
                        "CANTIDAD": 0,
                        "PRECIOREGULAR": float(streaming_data.get('Precio Referencial', 0.0)),
                        "PRECIOPROMOCIONAL": float(streaming_data.get('Precio Promocional', 0.0)),
                        "MESINICIAL": int(streaming_data.get('Mes Inicio', 0)),
                        "MESFINAL": int(streaming_data.get('Mes Fin', 0))
                    }
                    query = generate_query_modpromo_adic(data_to_insert)
                    if not db.insert_data(query):
                        return False
            else:
                data_to_insert = {
                    "IDREGISTRO": id_registro,
                    "PRODUCTO": producto,
                    "PLANPAQUETEMODELO": diccionarioDatos[producto].get('Modelo' if producto == 'ROUTER' else 'Planes'),
                    "CANTIDAD": int(diccionarioDatos[producto].get('Cantidad', 0)),
                    "PRECIOREGULAR": float(diccionarioDatos[producto].get('Precio Referencial', 0.0)),
                    "PRECIOPROMOCIONAL": float(diccionarioDatos[producto].get('Precio Promocional', 0.0)),
                    "MESINICIAL": int(diccionarioDatos[producto].get('Mes Inicio', 0)),
                    "MESFINAL": int(diccionarioDatos[producto].get('Mes Fin', 0))
                }
                query = generate_query_modpromo_adic(data_to_insert)
                if not db.insert_data(query):
                    return False
    return True


def generate_query_modpromo_adic(data):
    columns = ', '.join(data.keys())
    values_list = []
    for v in data.values():
        if v is None:
            values_list.append('NULL')
        elif isinstance(v, str):
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
    squery = "INSERT INTO YTBL_MODULOPROMOADIC ({}) VALUES ({})".format(columns, values)
    return squery
