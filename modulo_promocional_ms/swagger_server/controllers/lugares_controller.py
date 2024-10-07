import connexion
import requests
from flask import jsonify
from swagger_server.models.request_get_lugares import RequestGetLugares  # noqa: E501
from swagger_server.repository.lugares_Repository import lugares_Repository
from swagger_server.uses_cases.FormattedPlace import FormattedPlace
from swagger_server.utils.transactions.transaction import TransactionId
from swagger_server.utils.Readers.ReaderType import ReaderType
from loguru import logger

internal = TransactionId()
reader = ReaderType()


def get_lugares(body=None):  # noqa: E501
    """ get_lugares Consulta de Datos de Provincias segun sus parametros. # noqa: E501 """
    message = f"start get_lugares"
    if connexion.request.is_json:
        body = RequestGetLugares.from_dict(connexion.request.get_json())
        internal_transaction_id: str = internal.generate_internal_transaction_id()
        logger.info(message, internal = internal_transaction_id, external = body.external_transaction_id)
        try:
            if body.channel == 'api-modulos-promocionales-lugares':
                print(body.type)
                repository = lugares_Repository()
                frt = FormattedPlace()
                if body.type in set(reader.get_type_list('LUGARES_AD')):
                    _diccionario = {"popcion": "ALL_DATA", "name_Query": body.type}
                    data = repository.getData_Places(_diccionario)
                    dt = frt.formated_placeSIMPLEDATA(data, body.type)
                    return jsonify(dt), 200
                if body.type in set(reader.get_type_list('LUGARES_SD')):
                    _diccionario = {"popcion": "SPECIFIC_DATA", "name_Query": body.type, "_V1": body.v1}
                    if body.v2 is not None:
                        _diccionario["_V2"] = body.v2
                    print("TFV: ", body.v1)
                    print("Prod ", body.v2)
                    data = repository.getData_Places(_diccionario)
                    dt = frt.formated_placeMIXDATA(data, body.type)
                    return jsonify(dt), 200
                if body.type in  set(reader.get_type_list('LUGARES_MD')):
                    _diccionario = {"popcion": "MASIVE_DATA", "name_Query": body.type}
                    if body.id_provs is not None:
                        _diccionario['_V1'] = body.id_provs
                    if body.id_cities is not None:
                        _diccionario['_V1'] = body.id_cities
                        if body.v2 is not None:
                            _diccionario['_V2'] = body.v2
                        if body.v3 is not None:
                            _diccionario['_V3'] = body.v3
                    data = repository.getData_Places(_diccionario)
                    dt = frt.formated_placeMIXDATA(data, body.type)
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
            print("faseEscucha - planes_Controller | Error detectado")
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
