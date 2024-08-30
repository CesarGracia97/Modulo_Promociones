import connexion
import requests
from flask import jsonify

from swagger_server.config.config import ReaderJSON
from swagger_server.models.request_get_combos import RequestGetCombos  # noqa: E501
from swagger_server.models.request_get_ofertas import RequestGetOfertas  # noqa: E501
from swagger_server.models.request_get_planes import RequestGetPlanes  # noqa: E501
from swagger_server.models.request_get_servicios import RequestGetServicios  # noqa: E501from swagger_server.models.response_servicios_data import ResponseServiciosData  # noqa: E501
from swagger_server.utils.transactions.transaction import TransactionId

params_planes = {'channel': 'api-modulos-promocionales-planes'}
reader = ReaderJSON()
internal = TransactionId()


def get_combos(body=None):  # noqa: E501
    """Consulta de Datos de Combos"""
    if connexion.request.is_json:
        body = RequestGetCombos.from_dict(connexion.request.get_json())  # noqa: E501
        internal_transaction_id: str = internal.generate_internal_transaction_id()
        try:
            if body.channel == 'api-modulos-promocionales-web':
                print("*** FASE DE ESCUCHA ACTIVA ***")
                print(body.type)
                _stype_v = {"TIPO_SERVICIO", "PLAN", "PLANVARIANT", "PRODUCTO", "PRODUCTO_ROUTER"}
                params_planes['type'] = body.type
                params_planes['stype'] = body.stype
                if body.stype in _stype_v:
                    if body.v1 is not None:
                        params_planes['_V1'] = body.v1
                response = requests.post(reader.get_base_url() + '/get/Planes', json=params_planes)
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


def get_ofertas(body=None):  # noqa: E501
    """Consulta de Datos de Ofertas"""
    if connexion.request.is_json:
        body = RequestGetOfertas.from_dict(connexion.request.get_json())  # noqa: E501
        internal_transaction_id: str = internal.generate_internal_transaction_id()
        try:
            if body.channel == 'modulos-promocionales-web':
                print("*** FASE DE ESCUCHA ACTIVA ***")
                print(body.type)
                _type = body.type
                params_planes['type'] = body.type
                params_planes['stype'] = body.stype
                response = requests.post(reader.get_base_url() + '/get/Planes', json=params_planes)
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


def get_planes(body=None):  # noqa: E501
    """Consulta de Datos de Planes"""
    if connexion.request.is_json:
        body = RequestGetPlanes.from_dict(connexion.request.get_json())  # noqa: E501
        internal_transaction_id: str = internal.generate_internal_transaction_id()
        try:
            if body.channel == 'api-modulos-promocionales-web':
                print("*** FASE DE ESCUCHA ACTIVA ***")
                print(body.type)
                params_planes['type'] = body.type
                params_planes['stype'] = body.stype
                s_nvl_1 = {"AD_TARIFFPLAN", "AD_TARIFFPLAN_TARIFFPLANVARIANT"}
                s_nvl_2 = {"AD_TARIFFPLANVARIANT_PRODUCTO_ADICIONAL", "AD_TARIFFPLANVARIANT"}
                if body.stype in s_nvl_1:
                    print("Que dios me libre si entra aqui")
                elif body.stype in s_nvl_2:
                    if body.servicio is not None:
                        params_planes['_V1'] = body.servicio
                        if body.tipo_servicio is not None:
                            params_planes['_V2'] = body.tipo_servicio
                response = requests.post(reader.get_base_url() + '/get/Planes', json=params_planes)
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


def get_servicios(body=None):  # noqa: E501
    """Consulta de Datos de Servicios"""
    if connexion.request.is_json:
        body = RequestGetServicios.from_dict(connexion.request.get_json())  # noqa: E501
        internal_transaction_id: str = internal.generate_internal_transaction_id()
        try:
            if body.channel == 'modulos-promocionales-web':
                print("*** FASE DE ESCUCHA ACTIVA ***")
                print(body.type)
                params_planes['type'] = body.type
                params_planes['stype'] = body.stype
                response = requests.post(reader.get_base_url() + '/get/Planes', json=params_planes)
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
