import connexion
import requests
from flask import jsonify

from swagger_server.models.resquest_post_diccionario_datos import ResquestPostDiccionarioDatos  # noqa: E501
from swagger_server.utils.transactions.transaction import TransactionId

internal = TransactionId()


def get_modulo_promocional(body=None):  # noqa: E501
    """get_modulo_promocional  # noqa: E501"""
    if connexion.request.is_json:
        body = ResquestPostDiccionarioDatos.from_dict(connexion.request.get_json())  # noqa: E501
        internal_transaction_id: str = internal.generate_internal_transaction_id()
        try:
            if body.channel == 'modulos-promocionales-api':
                diccionario_datos = body.data
                diccionario_datos.telefonia.

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

    return 'do some magic!'
