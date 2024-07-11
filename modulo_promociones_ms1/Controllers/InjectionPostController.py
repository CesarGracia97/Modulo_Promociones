from flask import jsonify, Blueprint, request
from Resources.database.connectionbd import connectionb

receptor_bpost = Blueprint('ms_injectionPost', __name__)

class InjectionPostController:
    @receptor_bpost.route('/api/ms/postDatos', methods=['POST'])
    def IngresoDatos():
        try:
            if request.method == "POST":
                db = connectionb()
                db.connect()
                print("--------------------------------------------------------------------")
                print("IngresoDatos - InjectionPostController | FASE DE ESCUCHA ")
                print("--------------------------------------------------------------------")
                diccionarioDatos = request.json

                # Crear el diccionario base para insertar datos
                data_to_insert = {
                    "IDREGISTRO": diccionarioDatos.get('Id Registro'),
                    "FGENERACIONREGISTRO": diccionarioDatos.get('Fecha Generacion Registro'),
                    "NOMBREPROMOCION": diccionarioDatos.get('Nombre Promocion'),
                    "FINICIOCONTRATACION": diccionarioDatos.get('Fecha Inicio Promocion'),
                    "FFINCONTRATACION": diccionarioDatos.get('Fecha Finalizacion Promocion'),
                    "FFINANTICIPADACONTRATACION": None,
                    "ISVALID": 'Y',
                    "PRODUCTOID": diccionarioDatos.get('Producto_Id'),
                    "VARIANTID": diccionarioDatos.get('Variant_Id'),
                    "REDID": None,
                    "CANALID": diccionarioDatos.get('CanalId'),
                    "EXCEPCION": None,
                    "MESINICIOPROMOCION": diccionarioDatos.get('Mes Inicio Promocion'),
                    "MESFINPROMOCION": diccionarioDatos.get('Mes Fin Promocion'),
                    "FFINPROMOCION": None,
                    "DIASGOZADOS": diccionarioDatos.get('Dias Gozados'),
                    "PRECIOPROMOCIONAL": diccionarioDatos.get('Precio Promocional'),
                    "PRECIOREFERENCIAL": diccionarioDatos.get('Precio Referencial'),
                    "FCADUCIDADANTICIPADAREGISTRO": None,
                    "BURO": ','.join(map(str, diccionarioDatos.get('Buro', []))),
                    "FORMADEPAGO": ','.join(map(str, diccionarioDatos.get('Forma de Pago', []))),
                    "ENTIDADBANCARIA": None,
                    "EMISORTARJETA": None,
                    "CIUDADES": ','.join(map(str, diccionarioDatos.get('Ciudades', []))),
                    "SECTORES": str(diccionarioDatos.get('Sectores', [])),
                    "SUBSECTORES": str(diccionarioDatos.get('Sectores', [])),
                    "UPGRADES": None,
                    "PRODUCTOSADICIONALES": None
                }

                # Construir el query de inserción
                query = """
                    INSERT INTO YTBL_EXAMPLETABLEBD (
                        IDREGISTRO, FGENERACIONREGISTRO, NOMBREPROMOCION, FINICIOCONTRATACION, 
                        FFINCONTRATACION, FFINANTICIPADACONTRATACION, ISVALID, PRODUCTOID, 
                        VARIANTID, REDID, CANALID, EXCEPCION, MESINICIOPROMOCION, MESFINPROMOCION, 
                        FFINPROMOCION, DIASGOZADOS, PRECIOPROMOCIONAL, PRECIOREFERENCIAL, 
                        FCADUCIDADANTICIPADAREGISTRO, BURO, FORMADEPAGO, ENTIDADBANCARIA, 
                        EMISORTARJETA, CIUDADES, SECTORES, SUBSECTORES, UPGRADES, PRODUCTOSADICIONALES
                    ) VALUES (
                        :IDREGISTRO, :FGENERACIONREGISTRO, :NOMBREPROMOCION, :FINICIOCONTRATACION, 
                        :FFINCONTRATACION, :FFINANTICIPADACONTRATACION, :ISVALID, :PRODUCTOID, 
                        :VARIANTID, :REDID, :CANALID, :EXCEPCION, :MESINICIOPROMOCION, :MESFINPROMOCION, 
                        :FFINPROMOCION, :DIASGOZADOS, :PRECIOPROMOCIONAL, :PRECIOREFERENCIAL, 
                        :FCADUCIDADANTICIPADAREGISTRO, :BURO, :FORMADEPAGO, :ENTIDADBANCARIA, 
                        :EMISORTARJETA, :CIUDADES, :SECTORES, :SUBSECTORES, :UPGRADES, :PRODUCTOSADICIONALES
                    )
                """

                # Manejar el campo UPGRADE si existe
                if 'UPGRADE' in diccionarioDatos:
                    data_to_insert['UPGRADES'] = diccionarioDatos['UPGRADE']

                # Consultar si existen productos adicionales
                productos_adicionales = ['TELEFONIA', 'TELEVISION', 'ROUTER', 'STREAMING']
                hay_productos_adicionales = any(producto in diccionarioDatos for producto in productos_adicionales)

                if not hay_productos_adicionales:
                    # Enviar el query y el diccionario data_to_insert si no hay productos adicionales
                    success = db.insert_data(query, data_to_insert)
                    if not success:
                        print("Error en insertar datos")
                        return jsonify({'Error': 'Error al insertar datos en la tabla principal.'}), 400
                else:
                    # Manejar los productos adicionales si existen
                    for producto in productos_adicionales:
                        if producto in diccionarioDatos:
                            # Insertar datos para cada producto adicional
                            product_data = diccionarioDatos[producto]
                            data_to_insert['PRODUCTOSADICIONALES'] = product_data

                            # Ejecutar la inserción
                            success = db.insert_data(query, data_to_insert)
                            if not success:
                                print("Error en insertar datos")
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
