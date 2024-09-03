import connexion
import requests
from flask import jsonify

from swagger_server.config.config import ReaderJSON
from swagger_server.models.resquest_post_diccionario_datos import ResquestPostDiccionarioDatos  # noqa: E501
from swagger_server.utils.transactions.transaction import TransactionId

reader = ReaderJSON()
internal = TransactionId()


def post_modulopromocional(body=None):  # noqa: E501
    """post_modulopromocional Envio de Datos a Base de Datos # noqa: E501"""
    if connexion.request.is_json:
        body = ResquestPostDiccionarioDatos.from_dict(connexion.request.get_json())  # noqa: E501
        internal_transaction_id: str = internal.generate_internal_transaction_id()
        try:
            if body.channel == 'modulos-promocionales-web':
                dic = body.diccionario_datos
                streaming = dic.streaming
                upgrade = dic.upgrade
                telefonia = dic.telefonia
                television = dic.television
                router = dic.router

                u_upgrade = upgrade.upgrade
                u_mesinicio = upgrade.mes_inicio_upgrade
                u_mesfin = upgrade.mes_fin_upgrade
                tf_plan = telefonia.plan
                tf_precioreferencial = telefonia.precio_referencial
                tf_preciopromocional = telefonia.precio_promocional
                tf_cantidad = telefonia.cantidad
                tf_mesinicio = telefonia.mes_inicio
                tf_mesfin = telefonia.mes_fin
                tv_plan = television.plan
                tv_precioreferencial = television.precio_referencial
                tv_preciopromocional = television.precio_promocional
                tv_cantidad = television.cantidad
                tv_mesinicio = television.mes_inicio
                tv_mesfin = television.mes_fin
                rt_modelo = router.modelo
                rt_precioreferencial = router.precio_referencial
                rt_preciopromocional = router.precio_promocional
                rt_cantidad = router.cantidad
                rt_mesinicio = router.mes_inicio
                rt_mesfin = router.mes_fin


                # Verificación de que los atributos no sean nulos
                required_attributes = [
                    'buro', 'ciudades', 'dias_gozados', 'fecha_finalizacion_promocion',
                    'fecha_inicio_promocion', 'formas_de_pago', 'nombre_promocion',
                    'plan_id', 'producto_id', 'sectores', 'servicio', 'variant_id',
                    'mes_fin_promocion', 'mes_inicio_promocion', 'precio_referencial',
                    'precio_promocional'
                ]

                for attribute in required_attributes:
                    value = getattr(dic, attribute, None)
                    if value is None or (isinstance(value, str) and not value.strip()):
                        response = {
                            'errorCode': -2,
                            'message': f'Atributo faltante o nulo: {attribute}',
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
