import connexion
import requests
from flask import jsonify

from swagger_server.models.request_get_financiero import RequestGetFinanciero  # noqa: E501
from swagger_server.repository.financiero_Repository import financiero_Repository
from swagger_server.uses_cases.FormattedFinancial import FormattedFinance
from swagger_server.utils.Readers.ReaderType import ReaderType
from swagger_server.utils.transactions.transaction import TransactionId

internal = TransactionId()
reader = ReaderType()


def get_financiero(body: None):  # noqa: E501
    """get_financiero"""
    if connexion.request.is_json:
        body = RequestGetFinanciero.from_dict(connexion.request.get_json())  # noqa: E501
        internal_transaction_id: str = internal.generate_internal_transaction_id()
        try:
            if body.channel == 'api-modulos-promocionales-financiero':
                print(body.type)
                repository = financiero_Repository()
                frt = FormattedFinance()
                _diccionario = {}
                if body.type in set(reader.get_type_list('FINANCIERO')):
                    _diccionario['name_Query'] = body.type
                    if body.v1 is not None:
                        _diccionario['_V1'] = body.v1
                        if body.v2 is not None:
                            _diccionario['_V2'] = body.v2
                    data = repository.getData_Financial(_diccionario)
                    dt = frt.formatted_financial(body.type, data)
                    return jsonify(dt), 200
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
            print("faseEscucha - financiero_Controller | Error detectado")
            print("Peticion: ", body.type)
            print("Error: ", http_err.response.status_code, http_err.response.text)
            print("--------------------------------------------------------------------")
            error_respuesta = {
                'errorCode': http_err.response.status_code,
                'message': http_err.response.text,
                'externalTransactionId': body.external_transaction_id,
                'internalTransactionId': internal_transaction_id
            }
            return jsonify(error_respuesta), 400
