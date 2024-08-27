import connexion
import six
from flask import jsonify

from swagger_server.models.inline_response2002 import InlineResponse2002  # noqa: E501
from swagger_server.models.request_get_financiero import RequestGetFinanciero  # noqa: E501
from swagger_server.models.response_error import ResponseError  # noqa: E501
from swagger_server import util
from swagger_server.repository.financiero_Repository import financiero_Repository
from swagger_server.uses_cases.FormattedFinancial import FormattedFinance


def get_financiero(body=None):  # noqa: E501
    """get_financiero"""
    _type = None
    try:
        if connexion.request.is_json:
            _financial = {"ALL_BURO", "ALL_MPAGOS", "UPGRADE", "PRECIO_REGULAR", "DIAS_GOZADOS"}
            body = RequestGetFinanciero.from_dict(connexion.request.get_json())  # noqa: E501
            if body.channel == 'api-modulos-promocionales-financiero':
                print("*** FASE DE ESCUCHA ACTIVA ***")
                print(body.type)
                _type = body.type
                repository = financiero_Repository()
                frt = FormattedFinance()
                _diccionario = {}
                if _type in _financial:
                    _diccionario['name_Query'] = _type
                    if body.v1 is not None:
                        _diccionario['_V1'] = body.v1
                        if body.v2 is not None:
                            _diccionario['_V2'] = body.v2
                    data = repository.getData_Financial(_diccionario)
                    dt = frt.formatted_financial(_type, data)
                    return jsonify(dt), 200
    except Exception as e:
        print("--------------------------------------------------------------------")
        print("faseEscucha - financiero_Controller | Error detectado")
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
