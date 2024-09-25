import connexion
import requests
from flask import jsonify
from swagger_server.config.config import ReaderJSON
from swagger_server.models import RequestGetBuro, RequestGetDiasGozados, RequestGetFormasPago, RequestGetPrecioRegular
from swagger_server.models.request_get_upgrade import RequestGetUpgrade  # noqa: E501
from swagger_server.utils.transactions.transaction import TransactionId

reader = ReaderJSON()
internal = TransactionId()


def get_buro(body=None):  # noqa: E501
    """get_buro Consulta de Buro # noqa: E501 """
    if connexion.request.is_json:
        body = RequestGetBuro.from_dict(connexion.request.get_json())  # noqa: E501
        internal_transaction_id: str = internal.generate_internal_transaction_id()
        params_financiero = {'channel': 'api-modulos-promocionales-financiero'}
        try:
            if body.channel == 'web-modulos-promocionales':
                print("*** FASE DE ESCUCHA ACTIVA ***")
                print(body.type)
                params_financiero['type'] = body.type
                params_financiero['externalTransactionId'] = body.external_transaction_id
                params_financiero['internalTransactionId'] = internal_transaction_id
                response = requests.post(reader.get_base_url() + '/get/Financiero', json=params_financiero)
                response.raise_for_status()
                return response.json(), response.status_code
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
            print("Tipo de Peticion: ", body.type)
            print("Error: ", http_err.response.status_code, http_err.response.text)
            print("--------------------------------------------------------------------")
            response = {
                'errorCode': http_err.response.status_code,
                'message': http_err.response.text,
                'externalTransactionId': body.external_transaction_id,
                'internalTransactionId': internal_transaction_id
            }
            return jsonify(response), 400


def get_diasgozados(body=None):  # noqa: E501
    """get_diasgozados Consulta de Dias Gozados # noqa: E501 """
    if connexion.request.is_json:
        body = RequestGetDiasGozados.from_dict(connexion.request.get_json())  # noqa: E501
        internal_transaction_id: str = internal.generate_internal_transaction_id()
        params_financiero = {'channel': 'api-modulos-promocionales-financiero'}
        try:
            if body.channel == 'web-modulos-promocionales':
                print("*** FASE DE ESCUCHA ACTIVA ***")
                print(body.type)
                params_financiero['type'] = body.type
                params_financiero['externalTransactionId'] = body.external_transaction_id
                params_financiero['internalTransactionId'] = internal_transaction_id
                response = requests.post(reader.get_base_url() + '/get/Financiero', json=params_financiero)
                response.raise_for_status()
                return response.json(), response.status_code
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
            print("Tipo de Peticion: ", body.type)
            print("Error: ", http_err.response.status_code, http_err.response.text)
            print("--------------------------------------------------------------------")
            response = {
                'errorCode': http_err.response.status_code,
                'message': http_err.response.text,
                'externalTransactionId': body.external_transaction_id,
                'internalTransactionId': internal_transaction_id
            }
            return jsonify(response), 400


def get_modospago(body=None):  # noqa: E501
    """get_modospago Consulta de Modos de Pago # noqa: E501 """
    if connexion.request.is_json:
        body = RequestGetFormasPago.from_dict(connexion.request.get_json())  # noqa: E501
        internal_transaction_id: str = internal.generate_internal_transaction_id()
        params_financiero = {'channel': 'api-modulos-promocionales-financiero'}
        try:
            if body.channel == 'web-modulos-promocionales':
                print("*** FASE DE ESCUCHA ACTIVA ***")
                print(body.type)
                params_financiero['type'] = body.type
                params_financiero['externalTransactionId'] = body.external_transaction_id
                params_financiero['internalTransactionId'] = internal_transaction_id
                response = requests.post(reader.get_base_url() + '/get/Financiero', json=params_financiero)
                response.raise_for_status()
                return response.json(), response.status_code
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
            print("Tipo de Peticion: ", body.type)
            print("Error: ", http_err.response.status_code, http_err.response.text)
            print("--------------------------------------------------------------------")
            response = {
                'errorCode': http_err.response.status_code,
                'message': http_err.response.text,
                'externalTransactionId': body.external_transaction_id,
                'internalTransactionId': internal_transaction_id
            }
            return jsonify(response), 400


def get_precioregular(body=None):  # noqa: E501
    """get_precioregular Consulta de Precios de Productos # noqa: E501 """
    if connexion.request.is_json:
        body = RequestGetPrecioRegular.from_dict(connexion.request.get_json())
        internal_transaction_id: str = internal.generate_internal_transaction_id()
        params_financiero = {'channel': 'api-modulos-promocionales-financiero'}
        try:
            if body.channel == 'web-modulos-promocionales':
                print("*** FASE DE ESCUCHA ACTIVA ***")
                print(body.type)
                params_financiero['type'] = body.type
                params_financiero['_V1'] = body.tariffplanvariant
                params_financiero['_V2'] = body.id_prod
                params_financiero['externalTransactionId'] = body.external_transaction_id
                params_financiero['internalTransactionId'] = internal_transaction_id
                response = requests.post(reader.get_base_url() + '/get/Financiero', json=params_financiero)
                response.raise_for_status()
                return response.json(), response.status_code
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
            print("Tipo de Peticion: ", body.type)
            print("Error: ", http_err.response.status_code, http_err.response.text)
            print("--------------------------------------------------------------------")
            response = {
                'errorCode': http_err.response.status_code,
                'message': http_err.response.text,
                'externalTransactionId': body.external_transaction_id,
                'internalTransactionId': internal_transaction_id
            }
            return jsonify(response), 400


def get_upgrade(body=None):  # noqa: E501
    """get_upgrade Consulta de Datos Upgrade # noqa: E501 """
    if connexion.request.is_json:
        body = RequestGetUpgrade.from_dict(connexion.request.get_json())  # noqa: E501
        internal_transaction_id: str = internal.generate_internal_transaction_id()
        params_financiero = {'channel': 'api-modulos-promocionales-financiero'}
        try:
            if body.channel == 'web-modulos-promocionales':
                print("*** FASE DE ESCUCHA ACTIVA ***")
                print(body.type)
                params_financiero['type'] = body.type
                params_financiero['_V1'] = body.tariffplan
                params_financiero['_V2'] = body.tariffplanvariant
                params_financiero['externalTransactionId'] = body.external_transaction_id
                params_financiero['internalTransactionId'] = internal_transaction_id
                response = requests.post(reader.get_base_url() + '/get/Financiero', json=params_financiero)
                response.raise_for_status()
                return response.json(), response.status_code
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
            print("Tipo de Peticion: ", body.type)
            print("Error: ", http_err.response.status_code, http_err.response.text)
            print("--------------------------------------------------------------------")
            response = {
                'errorCode': http_err.response.status_code,
                'message': http_err.response.text,
                'externalTransactionId': body.external_transaction_id,
                'internalTransactionId': internal_transaction_id
            }
            return jsonify(response), 400
