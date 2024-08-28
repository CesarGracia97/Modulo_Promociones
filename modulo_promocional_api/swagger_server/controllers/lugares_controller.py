import connexion
import six
from flask import jsonify

from swagger_server.config.config import config
from swagger_server.models.request_get_ciudades import RequestGetCiudades  # noqa: E501
from swagger_server.models.request_get_provincia import RequestGetProvincia  # noqa: E501
from swagger_server.models.request_get_sectores import RequestGetSectores  # noqa: E501
from swagger_server.models.response_error import ResponseError  # noqa: E501
from swagger_server.models.response_get_ciudad_data import ResponseGetCiudadData  # noqa: E501
from swagger_server.models.response_get_provincia_data import ResponseGetProvinciaData  # noqa: E501
from swagger_server.models.response_get_sectores_data import ResponseGetSectoresData  # noqa: E501
from swagger_server import util


__URL__ = config.get('URL', 'URL_PLACE', 'URL_BASE')
params_lugares = {
    'channel': 'api-modulos-promocionales-lugares'
}


def __init__(self):
    self.__BASE = config.get('URL', 'URL_BASE')
    self.__BACK = config.get('URL', 'URL_BACKENDPOINT')


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
                _ciudades = {"ALL_CITIES", "CIUDADES_ESPECIFICASxPROV", "CIUDADES_ESPECIFICASxTFV",
                             "CIUDADES_ESPECIFICASxPROVxTFV", "CIUDADES_ESPECIFICASxTFVxPROD"}
                _ciudadesM = {"CIUDADES_M_ESPECIFICASxPROVxTFV"}
                if body.type in _ciudades:
                    print(body.type)
                    _type = body.type
                    params_lugares['type'] = body.type
                    if body.id_prov is not None:
                        params_lugares['_V1'] = body.id_prov
                        if body.tariffplanvariant is not None:
                            params_lugares['_V2'] = body.tariffplanvariant
                    if body.tariffplanvariant is not None and '_V1' not in params_lugares:
                        params_lugares['_V1'] = body.tariffplanvariant
                        if body.productoid is not None:
                            params_lugares['_V1'] = body.productoid
                if body.type in _ciudadesM:
                    print(body.type)
                    _type = body.type
                    params_lugares['type'] = body.type
                    if body.id_prov is not None:
                        params_lugares['_V1'] = body.id_provs
                        if body.tariffplanvariant is not None:
                            params_lugares['_V2'] = body.tariffplanvariant
                    if body.tariffplanvariant is not None and '_V1' not in params_lugares:
                        params_lugares['_V1'] = body.tariffplanvariant
                        if body.productoid is not None:
                            params_lugares['_V2'] = body.productoid

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
                _provincias = {"ALL_PROV", "PROVINCIAS_ESPECIFICASxTFV"}
                _type = body.type
                if body.type in _provincias:
                    params_lugares['type'] = body.type
                    if body.tariffplanvariant is not None:
                        params_lugares['_V1'] = body.tariffplanvariant
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
                _sectores = {"ALL_SECTORS", "SECTORES_ESPECIFICOSxCITY", "SECTORES_ESPECIFICOSxTFV",
                             "SECTORES_ESPECIFICOSxCITYxTFV"}
                _sectoresM = {"SECTORES_M_ESPECIFICOSxCITYxTFV", "SECTORES_M_ESPECIFICOSxCITYxTFVxPROD"}
                if body.type in _sectores:
                    _type = body.type
                    if body.id_city is not None:
                        params_lugares['_V1'] = body.id_city
                    if body.tariffplanvariant is not None and '_V1'not in params_lugares:
                        params_lugares['_V1'] = body.tariffplanvariant
                if body.type in _sectoresM:
                    _type = body.type
                    if body.id_cities is not None:
                        params_lugares['id_Cities'] = body.id_cities
                        if body.tariffplanvariant is not None:
                            params_lugares['_V2'] = body.tariffplanvariant
                            if body.productoid is not None:
                                params_lugares['_V3'] = body.productoid
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
