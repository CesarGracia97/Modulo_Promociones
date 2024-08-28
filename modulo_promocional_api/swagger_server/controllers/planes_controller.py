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
                _stype_v = {"TIPO_SERVICIO", "PLAN", "PLANVARIANT", "PRODUCTO", "PRODUCTO_ROUTER"}
                params_planes['type'] = body.type
                params_planes['stype'] = body.stype
                if body.stype in _stype_v:
                    if body.v1 is not None:
                        params_planes['_V1'] = body.v1
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
                params_planes['type'] = body.type
                params_planes['stype'] = body.stype
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
                params_planes['type'] = body.type
                params_planes['stype'] = body.stype
                s_nvl_1 = {"AD_TARIFFPLAN", "AD_TARIFFPLAN_TARIFFPLANVARIANT"}
                s_nvl_2 = {"AD_TARIFFPLANVARIANT_PRODUCTO_ADICIONAL", "AD_TARIFFPLANVARIANT"}
                if body.stype in s_nvl_1:
                    return 'ooowwww.... are you witch'
                if body.stype in s_nvl_2:
                    if body.servicio is not None:
                        params_planes['_V1'] = body.servicio
                        if body.tipo_servicio is not None:
                            params_planes['_V2'] = body.tipo_servicio
                    return 'ooowwww.... are you witch'
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
                params_planes['type'] = body.type
                params_planes['stype'] = body.stype
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
