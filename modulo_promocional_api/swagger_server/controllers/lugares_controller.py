import connexion
import six
from flask import jsonify

from swagger_server.models.request_get_ciudades import RequestGetCiudades  # noqa: E501
from swagger_server.models.request_get_provincia import RequestGetProvincia  # noqa: E501
from swagger_server.models.request_get_sectores import RequestGetSectores  # noqa: E501
from swagger_server.models.response_error import ResponseError  # noqa: E501
from swagger_server.models.response_get_ciudad_data import ResponseGetCiudadData  # noqa: E501
from swagger_server.models.response_get_provincia_data import ResponseGetProvinciaData  # noqa: E501
from swagger_server.models.response_get_sectores_data import ResponseGetSectoresData  # noqa: E501
from swagger_server import util


params_lugares = {
    'channel': 'api-modulos-promocionales-lugares'
}


def get_ciudades(body=None):  # noqa: E501
    """get_ciudades
    Consulta de Datos de Ciudades # noqa: E501
    """
    _type = None
    try:
        if connexion.request.is_json:
            body = RequestGetCiudades.from_dict(connexion.request.get_json())  # noqa: E501
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


def get_provincias(body=None):  # noqa: E501
    """get_provincias
    Consulta de Datos de Provincias segun sus parametros. # noqa: E501
    """
    _type = None
    try:
        if connexion.request.is_json:
            body = RequestGetProvincia.from_dict(connexion.request.get_json())  # noqa: E501
            if body.channel == 'api-modulos-promocionales-web':
                print("*** FASE DE ESCUCHA ACTIVA ***")
                print(body.type)
                _type = body.type
                _provincias = {"ALL_PROV", "PROVINCIAS_ESPECIFICASxTFV"}

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


def get_sectores(body=None):  # noqa: E501
    """get_sectores
    Consulta de Datos de Sectores # noqa: E501
    """
    _type = None
    try:
        if connexion.request.is_json:
            body = RequestGetSectores.from_dict(connexion.request.get_json())  # noqa: E501
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
