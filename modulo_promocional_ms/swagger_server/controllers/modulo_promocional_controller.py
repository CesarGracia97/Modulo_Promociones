from datetime import datetime

import connexion
import requests
from flask import jsonify, json

from swagger_server.models.resquest_post_diccionario_datos import ResquestPostDiccionarioDatos  # noqa: E501
from swagger_server.resources.database.connection import connection
from swagger_server.utils.transactions.transaction import TransactionId

internal = TransactionId()


def get_modulo_promocional(body=None):  # noqa: E501
    """get_modulo_promocional  # noqa: E501"""
    if connexion.request.is_json:
        body = ResquestPostDiccionarioDatos.from_dict(connexion.request.get_json())  # noqa: E501
        internal_transaction_id: str = internal.generate_internal_transaction_id()
        try:
            if body.channel == 'api-modulos-promocionales-post':
                dic = body.data
                id_registro = generate_id_registro(dic.id_registro, dic.fecha_generacion_registro, body, internal_transaction_id)
                data_to_insert = moduloprin_data(dic, id_registro)  # Extrae datos para la tabla principal
                query = generate_query_modpromo(data_to_insert)  # Genera el query de inserción
                db = connection()  # Inserta los datos en la base de datos
                db.connect()
                success = db.insert_data(query)
                if not success:
                    db.close()
                    return jsonify({
                        'errorCode': -2,
                        'message': 'Fallo en el guardado de datos',
                        'externalTransactionId': body.external_transaction_id,
                        'internalTransactionId': internal_transaction_id
                    }), 500
                success = handle_promociones_adicionales(db, dic, id_registro)  # Inserción de productos adicionales
                if not success:
                    db.close()
                    return jsonify({
                        'errorCode': -3,
                        'message': 'Fallo en el guardado de productos adicionales',
                        'externalTransactionId': body.external_transaction_id,
                        'internalTransactionId': internal_transaction_id
                    }), 500
                db.close()
                return jsonify({
                    'message': 'Inserción exitosa',
                    'externalTransactionId': body.external_transaction_id,
                    'internalTransactionId': internal_transaction_id
                }), 200
            else:
                response = {
                    'errorCode': -1,
                    'message': 'Canal Invalido',
                    'externalTransactionId': body.external_transaction_id,
                    'internalTransactionId': internal_transaction_id
                }
                return jsonify(response), 400
        except requests.exceptions.HTTPError as http_err:
            print("--------------------------------------------------------------------")
            print("get_modulo_promocional - modulo_promocional_controller | Error detectado")
            print("Tipo de Peticion: POST")
            print("Error: ", http_err.response.status_code, http_err.response.text)
            print("--------------------------------------------------------------------")
            response = {
                'errorCode': http_err.response.status_code,
                'message': http_err.response.text,
                'externalTransactionId': body.external_transaction_id,
                'internalTransactionId': internal_transaction_id
            }
            return jsonify(response), 400


def convert_to_date(date_str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        return datetime.strptime(date_str, "%Y-%m-%d")


def generate_id_registro(id_registro, fecha_generacion_registro, body, internal_transaction_id):
    try:
        fecha_obj = convert_to_date(fecha_generacion_registro)
        fecha_str = fecha_obj.strftime('%d%m%y:%H%M')
        return f"MODP-{id_registro}-{fecha_str}"
    except requests.exceptions.HTTPError as http_err:
        print("--------------------------------------------------------------------")
        print("generate_id_registro - get_modulo_promocional | Error detectado")
        print("Tipo de Peticion: POST")
        print("Error: ", http_err.response.status_code, http_err.response.text)
        print("--------------------------------------------------------------------")
        response = {
            'errorCode': http_err.response.status_code,
            'message': http_err.response.text,
            'externalTransactionId': body.external_transaction_id,
            'internalTransactionId': internal_transaction_id
        }
        return jsonify(response), 400


def moduloprin_data(dic, id_registro):
    return {
        "IDREGISTRO": id_registro,
        "FGENERACIONREGISTRO": convert_to_date(dic.fecha_generacion_registro),
        "NOMBREPROMOCION": dic.nombre_promocion,
        "FINICIOCONTRATACION": convert_to_date(dic.fecha_inicio_promocion),
        "FFINCONTRATACION": convert_to_date(dic.fecha_finalizacion_promocion),
        "FFINANTICIPADACONTRATACION": None,
        "ISVALID": 'Y',
        "PRODUCTOID": int(dic.producto_id),
        "VARIANTID": int(dic.variant_id),
        "REDID": None,
        "CANALID": int(dic.canal),
        "EXCEPCION": None,
        "MESINICIOPROMOCION": int(dic.mes_inicio_promocion),
        "MESFINPROMOCION": dic.mes_fin_promocion,
        "FFINPROMOCION": None,
        "DIASGOZADOS": dic.dias_gozados,
        "PRECIOPROMOCIONAL": float(dic.precio_promocional),
        "PRECIOREFERENCIAL": float(dic.precio_referencial),
        "FCADUCIDADANTICIPADAREGISTRO": None,
        "BURO": ','.join(map(str, dic.buro)),
        "FORMADEPAGO": ','.join(map(str, dic.forma_de_pago)),
        "ENTIDADBANCARIA": None,
        "EMISORTARJETA": None,
        "CIUDADES": json.dumps(dic.ciudades),
        "SECTORES": json.dumps(dic.sectores),
        "UPGRADE": json.dumps({
            "Upgrade": int(dic.upgrade.upgrade),
            "Mes Inicio Upgrade": int(dic.upgrade.mes_inicio_upgrade),
            "Mes Fin Upgrade": dic.upgrade.mes_fin_upgrade
        }) if dic.upgrade else None
    }


def generate_query_modpromo(data):
    columns = ', '.join(data.keys())
    values_list = []

    for v in data.values():
        if v is None:
            values_list.append('NULL')
        elif isinstance(v, str):
            sanitized_value = v.replace("'", "''")
            values_list.append(f"'{sanitized_value}'")
        elif isinstance(v, (int, float)):
            values_list.append(str(v))
        elif isinstance(v, datetime):
            formatted_date = v.strftime('%Y-%m-%d %H:%M:%S')
            values_list.append(f"TO_DATE('{formatted_date}', 'YYYY-MM-DD HH24:MI:SS')")
        elif isinstance(v, (list, dict)):
            json_value = json.dumps(v).replace("'", "''")
            values_list.append(f"'{json_value}'")

    values = ', '.join(values_list)
    query = f"INSERT INTO YTBL_MODULOPROMO_PRIN ({columns}) VALUES ({values})"
    return query


def handle_promociones_adicionales(db, dic, id_registro):
    productos_adicionales = ['telefonia', 'television', 'router', 'streaming']

    for producto in productos_adicionales:
        if getattr(dic, producto, None):
            if producto == 'streaming':
                for streaming_data_str in dic.streaming:  # Caso especial: streaming tiene múltiples entradas
                    streaming_data = json.loads(streaming_data_str)  # Convertir de string a JSON
                    data_to_insert = {
                        "IDREGISTRO": id_registro,
                        "PRODUCTO": 'STREAMING',
                        "PLANPAQUETEMODELO": int(streaming_data.get('Paquete', 0)),
                        "CANTIDAD": 0,
                        "PRECIOREGULAR": float(streaming_data.get('Precio Referencial', 0.0)),
                        "PRECIOPROMOCIONAL": float(streaming_data.get('Precio Promocional', 0.0)),
                        "MESINICIAL": int(streaming_data.get('Mes Inicio', 0)),
                        "MESFINAL": streaming_data.get('Mes Fin')
                    }
                    query = generate_query_modpromo_adic(data_to_insert)
                    if not db.insert_data(query):
                        return False
            else:
                # Telefonía, Televisión o Router
                data_to_insert = {
                    "IDREGISTRO": id_registro,
                    "PRODUCTO": producto.upper(),
                    "PLANPAQUETEMODELO": getattr(dic, producto).get('modelo' if producto == 'router' else 'plan'),
                    "CANTIDAD": int(getattr(dic, producto).get('cantidad', 0)),
                    "PRECIOREGULAR": float(getattr(dic, producto).get('precio_referencial', 0.0)),
                    "PRECIOPROMOCIONAL": float(getattr(dic, producto).get('precio_promocional', 0.0)),
                    "MESINICIAL": int(getattr(dic, producto).get('mes_inicio', 0)),
                    "MESFINAL": getattr(dic, producto).get('mes_fin')
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
            values_list.append(f"'{sanitized_value}'")
        elif isinstance(v, (int, float)):
            values_list.append(str(v))
    values = ', '.join(values_list)
    query = f"INSERT INTO YTBL_MODULOPROMO_ADIC ({columns}) VALUES ({values})"
    return query
