import connexion
import six
from flask import jsonify

from swagger_server.models.request_get_buro import RequestGetBuro  # noqa: E501
from swagger_server.models.request_get_dias_gozados import RequestGetDiasGozados  # noqa: E501
from swagger_server.models.request_get_formas_pago import RequestGetFormasPago  # noqa: E501
from swagger_server.models.request_get_precio_regular import RequestGetPrecioRegular  # noqa: E501
from swagger_server.models.request_get_upgrade import RequestGetUpgrade  # noqa: E501
from swagger_server.models.response_error import ResponseError  # noqa: E501
from swagger_server.models.response_get_buro_data import ResponseGetBuroData  # noqa: E501
from swagger_server.models.response_get_dias_gozados_data import ResponseGetDiasGozadosData  # noqa: E501
from swagger_server.models.response_get_formas_pago_data import ResponseGetFormasPagoData  # noqa: E501
from swagger_server.models.response_get_precio_regular_data import ResponseGetPrecioRegularData  # noqa: E501
from swagger_server.models.response_get_upgrade_data import ResponseGetUpgradeData  # noqa: E501
from swagger_server import util


params_financiero = {
    'channel': 'api-modulos-promocionales-financiero'
}


def get_buro(body=None):  # noqa: E501
    """get_buro
    Consulta de Buro # noqa: E501
    """
    _type = None
    try:
        if connexion.request.is_json:
            body = RequestGetUpgrade.from_dict(connexion.request.get_json())  # noqa: E501
            if body.channel == 'api-modulos-promocionales-web':
                print("*** FASE DE ESCUCHA ACTIVA ***")
                print(body.type)
                _type = body.type
                params_financiero['type'] = body.type
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


def get_diasgozados(body=None):  # noqa: E501
    """get_diasgozados
    Consulta de Dias Gozados # noqa: E501
    """
    _type = None
    try:
        if connexion.request.is_json:
            body = RequestGetUpgrade.from_dict(connexion.request.get_json())  # noqa: E501
            if body.channel == 'api-modulos-promocionales-web':
                print("*** FASE DE ESCUCHA ACTIVA ***")
                print(body.type)
                _type = body.type
                params_financiero['type'] = body.type
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


def get_modospago(body=None):  # noqa: E501
    """get_modospago
    Consulta de Modos de Pago # noqa: E501
    """
    _type = None
    try:
        if connexion.request.is_json:
            body = RequestGetUpgrade.from_dict(connexion.request.get_json())  # noqa: E501
            if body.channel == 'api-modulos-promocionales-web':
                print("*** FASE DE ESCUCHA ACTIVA ***")
                print(body.type)
                _type = body.type
                params_financiero['type'] = body.type
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


def get_precioregular(body=None):  # noqa: E501
    """get_precioregular
    Consulta de Precios de Productos # noqa: E501}
    """
    _type = None
    try:
        if connexion.request.is_json:
            body = RequestGetUpgrade.from_dict(connexion.request.get_json())  # noqa: E501
            if body.channel == 'api-modulos-promocionales-web':
                print("*** FASE DE ESCUCHA ACTIVA ***")
                print(body.type)
                _type = body.type
                params_financiero['type'] = body.type
                params_financiero['_V1'] = body.tariffplan
                params_financiero['_V2'] = body.tariffplanvariant
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


def get_upgrade(body=None):  # noqa: E501
    """get_upgrade
    Consulta de Datos Upgrade # noqa: E501
    """
    _type = None
    try:
        if connexion.request.is_json:
            body = RequestGetUpgrade.from_dict(connexion.request.get_json())  # noqa: E501
            if body.channel == 'api-modulos-promocionales-web':
                print("*** FASE DE ESCUCHA ACTIVA ***")
                print(body.type)
                _type = body.type
                params_financiero['type'] = body.type
                params_financiero['_V1'] = body.tariffplan
                params_financiero['_V2'] = body.tariffplanvariant
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
