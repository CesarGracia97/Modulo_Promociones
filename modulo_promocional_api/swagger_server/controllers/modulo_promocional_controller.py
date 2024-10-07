import connexion
import requests
from flask import jsonify
from datetime import datetime, date
from swagger_server.config.config import ReaderJSON
from swagger_server.models.resquest_post_diccionario_datos import ResquestPostDiccionarioDatos  # noqa: E501
from swagger_server.utils.transactions.transaction import TransactionId
from loguru import logger

reader = ReaderJSON()
internal = TransactionId()


def post_modulopromocional(body=None):  # noqa: E501
    """post_modulopromocional Envio de Datos a Base de Datos # noqa: E501"""
    message = f"start post_modulopromocional"
    if connexion.request.is_json:
        body = ResquestPostDiccionarioDatos.from_dict(connexion.request.get_json())  # noqa: E501
        internal_transaction_id: str = internal.generate_internal_transaction_id()
        logger.info(message, internal = internal_transaction_id, external = body.external_transaction_id)
        params_post = {'channel': 'api-modulos-promocionales-post', 'data': {}}
        try:
            if body.channel == 'web-modulos-promocionales':
                params_post['externalTransactionId'] = body.external_transaction_id
                params_post['internalTransactionId'] = internal_transaction_id
                dic = body.diccionario_datos
                if dic:
                    diccionario = {
                        "Id Registro": dic.id_registro,
                        "Fecha Generacion Registro": str(dic.fecha_generacion_registro),
                        "Nombre Promocion": dic.nombre_promocion,
                        "Fecha Inicio Promocion": str(dic.fecha_inicio_promocion),
                        "Fecha Finalizacion Promocion": str(dic.fecha_finalizacion_promocion),
                        "Servicio": dic.servicio,
                        "Producto_Id": int(dic.producto_id),
                        "Plan_Id": int(dic.plan_id),
                        "Variant_Id": int(dic.variant_id),
                        "Canal": int(dic.canal),
                        "Mes Inicio Promocion": int(dic.mes_inicio_promocion),
                        "Mes Fin Promocion": str(dic.mes_fin_promocion),
                        "Dias Gozados": dic.dias_gozados,
                        "Precio Promocional": float(dic.precio_promocional),
                        "Precio Referencial": float(dic.precio_referencial),
                        "Buro": dic.buro,
                        "Forma de Pago": dic.forma_de_pago,
                        "Ciudades": dic.ciudades,
                        "Sectores": dic.sectores,
                        "UPGRADE": None
                    }
                    if dic.upgrade:
                        upgrade = {
                            "UPGRADE": dic.upgrade.upgrade,
                            "Mes Inicio UPGRADE": dic.upgrade.mes_inicio_upgrade,
                            "Mes Fin UPGRADE": str(dic.upgrade.mes_fin_upgrade)
                        }
                        diccionario["UPGRADE"] = upgrade
                    if dic.router:
                        router = {
                            "Modelo": int(dic.router.modelo),
                            "Producto Adicional": dic.router.producto_adicional,
                            "Cantidad": int(dic.router.cantidad),
                            "Precio Referencial": float(dic.router.precio_referencial),
                            "Precio Promocional": float(dic.router.precio_promocional),
                            "Mes Inicio": int(dic.router.mes_inicio),
                            "Mes Fin": str(dic.router.mes_fin)
                        }
                        diccionario["ROUTER"] = router
                    if dic.telefonia:
                        telefonia = {
                            "Plan": int(dic.telefonia.plan),
                            "Producto Adicional": str(dic.telefonia.producto_adicional),
                            "Cantidad": int(dic.telefonia.cantidad),
                            "Precio Referencial": float(dic.telefonia.precio_referencial),
                            "Precio Promocional": float(dic.telefonia.precio_promocional),
                            "Mes Inicio": int(dic.telefonia.mes_inicio),
                            "Mes Fin": str(dic.telefonia.mes_fin)
                        }
                        diccionario["TELEFONIA"] = telefonia
                    if dic.television:
                        television = {
                            "Plan": int(dic.television.plan),
                            "Producto Adicional": str(dic.television.producto_adicional),
                            "Cantidad": int(dic.television.cantidad),
                            "Precio Referencial": float(dic.television.precio_referencial),
                            "Precio Promocional": float(dic.television.precio_promocional),
                            "Mes Inicio": int(dic.television.mes_inicio),
                            "Mes Fin": str(dic.television.mes_fin)
                        }
                        diccionario["TELEVISION"] = television
                    if dic.streaming:
                        diccionario["STREAMING"] = dic.streaming
                    params_post['data'] = diccionario
                    response = requests.post(reader.get_base_url() + '/post/modulo-promocional', json=params_post)
                    response.raise_for_status()
                    return response.json(), response.status_code
                else:
                    response = {
                        'errorCode': -3,
                        'message': 'Diccionario Vacio',
                        'externalTransactionId': body.external_transaction_id,
                        'internalTransactionId': internal_transaction_id
                    }
                    return jsonify(response), 400
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
            print("faseEscucha - planes_Controller | Error detectado")
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
