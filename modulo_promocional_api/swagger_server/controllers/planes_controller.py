import connexion
from flask import jsonify

from swagger_server.models.request_get_combos import RequestGetCombos  # noqa: E501
from swagger_server.models.request_get_ofertas import RequestGetOfertas  # noqa: E501
from swagger_server.models.request_get_planes import RequestGetPlanes  # noqa: E501
from swagger_server.models.request_get_servicios import RequestGetServicios  # noqa: E501
from swagger_server.models.response_combos_data import ResponseCombosData  # noqa: E501
from swagger_server.models.response_error import ResponseError  # noqa: E501
from swagger_server.models.response_get_planes_data import ResponseGetPlanesData  # noqa: E501
from swagger_server.models.response_ofertas_data import ResponseOfertasData  # noqa: E501
from swagger_server.models.response_servicios_data import ResponseServiciosData  # noqa: E501
from swagger_server import util


params_planes = {
    'channel': 'api-modulos-promocionales-planes'
}


def get_combos(body=None):  # noqa: E501
    """get_combos
    Consulta de Datos de Combos # noqa: E501
    """
    _type = None
    try:
        if connexion.request.is_json:
            body = RequestGetCombos.from_dict(connexion.request.get_json())  # noqa: E501
            if body.channel == 'api-modulos-promocionales-web':
                print("*** FASE DE ESCUCHA ACTIVA ***")
                print(body.type)
                _type = body.type

        return 'do some magic!'
    except Exception as e:
        print("--------------------------------------------------------------------")
        print("faseEscucha - planes_Controller | Error detectado")
        print("Tipo de Peticion: ", _type)
        print("Error: ", e)
        print("--------------------------------------------------------------------")
        error_respuesta = {
            'errorCode': -1,
            'message': e,
            'externalTransactionId': 0,
            'internalTransactionId': 0
        }
        return jsonify(error_respuesta), 400


def get_ofertas(body=None):  # noqa: E501
    """get_ofertas
    Consulta de Datos de Ofertas # noqa: E501
    """
    _type = None
    try:
        if connexion.request.is_json:
            body = RequestGetOfertas.from_dict(connexion.request.get_json())  # noqa: E501
            if body.channel == 'api-modulos-promocionales-web':
                print("*** FASE DE ESCUCHA ACTIVA ***")
                print(body.type)
                _type = body.type

        return 'do some magic!'
    except Exception as e:
        print("--------------------------------------------------------------------")
        print("faseEscucha - planes_Controller | Error detectado")
        print("Tipo de Peticion: ", _type)
        print("Error: ", e)
        print("--------------------------------------------------------------------")
        error_respuesta = {
            'errorCode': -1,
            'message': e,
            'externalTransactionId': 0,
            'internalTransactionId': 0
        }
        return jsonify(error_respuesta), 400


def get_planes(body=None):  # noqa: E501
    """get_planes
    Consulta de Datos de Planes # noqa: E501
    """
    _type = None
    try:
        if connexion.request.is_json:
            body = RequestGetPlanes.from_dict(connexion.request.get_json())  # noqa: E501
            if body.channel == 'api-modulos-promocionales-web':
                print("*** FASE DE ESCUCHA ACTIVA ***")
                print(body.type)
                _type = body.type

        return 'do some magic!'
    except Exception as e:
        print("--------------------------------------------------------------------")
        print("faseEscucha - planes_Controller | Error detectado")
        print("Tipo de Peticion: ", _type)
        print("Error: ", e)
        print("--------------------------------------------------------------------")
        error_respuesta = {
            'errorCode': -1,
            'message': e,
            'externalTransactionId': 0,
            'internalTransactionId': 0
        }
        return jsonify(error_respuesta), 400


def get_servicios(body=None):  # noqa: E501
    """get_servicios
    Consulta de Datos de Servicios # noqa: E501
    :rtype: ResponseServiciosData
    """
    _type = None
    try:
        if connexion.request.is_json:
            body = RequestGetServicios.from_dict(connexion.request.get_json())  # noqa: E501
            if body.channel == 'api-modulos-promocionales-web':
                print("*** FASE DE ESCUCHA ACTIVA ***")
                print(body.type)
                _type = body.type

        return 'do some magic!'
    except Exception as e:
        print("--------------------------------------------------------------------")
        print("faseEscucha - planes_Controller | Error detectado")
        print("Tipo de Peticion: ", _type)
        print("Error: ", e)
        print("--------------------------------------------------------------------")
        error_respuesta = {
            'errorCode': -1,
            'message': e,
            'externalTransactionId': 0,
            'internalTransactionId': 0
        }
        return jsonify(error_respuesta), 400
