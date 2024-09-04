import connexion
import requests
from flask import jsonify

from swagger_server.config.config import ReaderJSON
from swagger_server.models.resquest_post_diccionario_datos import ResquestPostDiccionarioDatos  # noqa: E501
from swagger_server.utils.transactions.transaction import TransactionId

reader = ReaderJSON()
internal = TransactionId()
params_post = {'channel': 'api-modulos-promocionales-post'}


def validate_attributes(data, attributes, external_transaction_id, internal_transaction_id, section_name):
    """Valida que los atributos no sean nulos o vacíos."""
    for attribute in set(reader.get_type_list(attributes)):
        value = getattr(data, attribute, None)
        if value is None or (isinstance(value, str) and not value.strip()):
            response = {
                'errorCode': -2,
                'message': f'Atributo faltante o nulo en {section_name}: {attribute}',
                'externalTransactionId': external_transaction_id,
                'internalTransactionId': internal_transaction_id
            }
            return jsonify(response), 400
    return None


def post_modulopromocional(body=None):  # noqa: E501
    """post_modulopromocional Envio de Datos a Base de Datos # noqa: E501"""
    if connexion.request.is_json:
        body = ResquestPostDiccionarioDatos.from_dict(connexion.request.get_json())  # noqa: E501
        internal_transaction_id: str = internal.generate_internal_transaction_id()
        try:
            if body.channel == 'modulos-promocionales-web':
                dic = body.diccionario_datos

                # Validaciones generales
                validation_response = validate_attributes(dic, 'ATRIBUTOS_POST', body.external_transaction_id,
                                                          internal_transaction_id, 'Diccionario de Datos')
                if validation_response:
                    return validation_response

                # Validaciones específicas
                if dic.upgrade is not None:
                    validation_response = validate_attributes(dic.upgrade, 'UPGRADE', body.external_transaction_id,
                                                              internal_transaction_id, 'Upgrade')
                    if validation_response:
                        return validation_response

                if dic.telefonia is not None:
                    validation_response = validate_attributes(dic.telefonia, 'TELEFONIA', body.external_transaction_id,
                                                              internal_transaction_id, 'Telefonia')
                    if validation_response:
                        return validation_response

                if dic.television is not None:
                    validation_response = validate_attributes(dic.television, 'TELEVISION', body.external_transaction_id,
                                                              internal_transaction_id, 'Television')
                    if validation_response:
                        return validation_response

                if dic.router is not None:
                    validation_response = validate_attributes(dic.router, 'ROUTER', body.external_transaction_id,
                                                              internal_transaction_id, 'Router')
                    if validation_response:
                        return validation_response
                params_post['externalTransactionId'] = internal_transaction_id
                params_post['data'] = dic
                response = requests.post(reader.get_base_url() + '/post/modulo-promocional', json=dic)
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
            print("Tipo de Peticion: POST")
            print("Error: ", http_err.response.status_code, http_err.response.text)
            print("--------------------------------------------------------------------")
            response = {
                'errorCode': http_err.response.status_code,
                'message': http_err.response.text,
                'externalTransactionId': body.external_transaction_id,
                'internalTransactionId': internal_transaction_id
            }
            return jsonify(response), 400
