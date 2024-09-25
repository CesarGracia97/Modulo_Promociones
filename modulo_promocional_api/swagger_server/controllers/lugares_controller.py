import connexion
import requests
from flask import jsonify

from swagger_server.config.config import ReaderJSON
from swagger_server.models.request_get_ciudades import RequestGetCiudades  # noqa: E501
from swagger_server.models.request_get_provincia import RequestGetProvincia  # noqa: E501
from swagger_server.models.request_get_sectores import RequestGetSectores  # noqa: E501from swagger_server.utils.logs.logging import Log
from swagger_server.utils.transactions.transaction import TransactionId

reader = ReaderJSON()
internal = TransactionId()


def get_provincias(body=None):  # noqa: E501
    """get_provincias Consulta de Datos de Provincias segun sus parametros. # noqa: E501 """
    if connexion.request.is_json:
        body = RequestGetProvincia.from_dict(connexion.request.get_json())  # noqa: E501
        internal_transaction_id: str = internal.generate_internal_transaction_id()
        params_lugares = {'channel': 'api-modulos-promocionales-lugares'}
        try:
            if body.channel == 'web-modulos-promocionales':
                print("*** FASE DE ESCUCHA ACTIVA ***")
                print(body.type)
                if body.type in set(reader.get_type_list('PROVINCIAS')):
                    params_lugares['type'] = body.type
                    params_lugares['externalTransactionId'] = body.external_transaction_id
                    params_lugares['internalTransactionId'] = internal_transaction_id
                    if body.tariffplanvariant is not None:
                        params_lugares['_V1'] = body.tariffplanvariant
                    response = requests.post(reader.get_base_url() + '/get/Lugares', json=params_lugares)
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


def get_ciudades(body=None):  # noqa: E501
    """get_ciudades Consulta de Datos de Ciudades # noqa: E501 """
    if connexion.request.is_json:
        body = RequestGetCiudades.from_dict(connexion.request.get_json())  # noqa: E501
        internal_transaction_id: str = internal.generate_internal_transaction_id()
        params_lugares = {'channel': 'api-modulos-promocionales-lugares'}
        try:
            if body.channel == 'web-modulos-promocionales':
                print("*** FASE DE ESCUCHA ACTIVA ***")
                print(body.type)
                params_lugares['type'] = body.type
                params_lugares['externalTransactionId'] = body.external_transaction_id
                params_lugares['internalTransactionId'] = internal_transaction_id
                if body.type in set(reader.get_type_list('CIUDADES')):
                    if body.id_prov is not None:
                        params_lugares['_V1'] = body.id_prov
                        if body.tariffplanvariant is not None:
                            params_lugares['_V2'] = body.tariffplanvariant
                    if body.tariffplanvariant is not None and '_V1' not in params_lugares:
                        params_lugares['_V1'] = body.tariffplanvariant
                        if body.productoid is not None:
                            params_lugares['_V2'] = body.productoid
                    print("variant: ", body.tariffplanvariant)
                    print("producto: ", body.productoid)
                if body.type in set(reader.get_type_list('CIUDADESM')):
                    if body.id_prov is not None:
                        params_lugares['_V1'] = body.id_provs
                        if body.tariffplanvariant is not None:
                            params_lugares['_V2'] = body.tariffplanvariant
                    if body.tariffplanvariant is not None and '_V1' not in params_lugares:
                        params_lugares['_V1'] = body.tariffplanvariant
                        if body.productoid is not None:
                            params_lugares['_V2'] = body.productoid
                response = requests.post(reader.get_base_url() + '/get/Lugares', json=params_lugares)
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


def get_sectores(body=None):  # noqa: E501
    """get_sectores Consulta de Datos de Sectores # noqa: E501 """
    if connexion.request.is_json:
        body = RequestGetSectores.from_dict(connexion.request.get_json())  # noqa: E501
        internal_transaction_id: str = internal.generate_internal_transaction_id()
        params_lugares = {'channel': 'api-modulos-promocionales-lugares'}
        try:
            if body.channel == 'web-modulos-promocionales':
                print("*** FASE DE ESCUCHA ACTIVA ***")
                print(body.type)
                params_lugares['type'] = body.type
                params_lugares['externalTransactionId'] = body.external_transaction_id
                params_lugares['internalTransactionId'] = internal_transaction_id
                if body.type in set(reader.get_type_list('SECTORES')):
                    _type = body.type
                    if body.id_city is not None:
                        params_lugares['_V1'] = body.id_city
                    if body.tariffplanvariant is not None and '_V1' not in params_lugares:
                        params_lugares['_V1'] = body.tariffplanvariant
                if body.type in set(reader.get_type_list('SECTORESM')):
                    _type = body.type
                    if body.id_cities is not None:
                        params_lugares['id_Cities'] = body.id_cities
                        if body.tariffplanvariant is not None:
                            params_lugares['_V2'] = body.tariffplanvariant
                            if body.productoid is not None:
                                params_lugares['_V3'] = body.productoid
                response = requests.post(reader.get_base_url() + '/get/Lugares', json=params_lugares)
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


