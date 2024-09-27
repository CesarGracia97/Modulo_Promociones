import connexion
import requests
from flask import jsonify
from swagger_server.models.request_get_planes import RequestGetPlanes  # noqa: E501
from swagger_server.repository.planes_Repository import planes_Repository
from swagger_server.uses_cases.FormattedPlans import FormattedPlans
from swagger_server.utils.Readers.ReaderType import ReaderType
from swagger_server.utils.transactions.transaction import TransactionId

internal = TransactionId()
reader = ReaderType()


def get_planes(body=None):  # noqa: E501
    """get_planes Consulta de Datos de Provincias segun sus parametros. # noqa: E501 """
    if connexion.request.is_json:
        body = RequestGetPlanes.from_dict(connexion.request.get_json())  # noqa: E501
        internal_transaction_id: str = internal.generate_internal_transaction_id()
        try:
            if body.channel == 'api-modulos-promocionales-planes':
                print(body.type)
                _diccionario = {}
                frt = FormattedPlans()
                repository = planes_Repository()
                if body.type == 'ALL_DATA':
                    _diccionario['popcion'] = body.type

                    if body.stype in set(reader.get_type_list('PLANES_TD1')):
                        _diccionario['sopcion'] = body.stype
                        data = repository.getData_Planes(_diccionario)
                        dt_ = frt.formated_TypeALL(body.stype, data)
                        return jsonify(dt_), 200

                    if body.stype in set(reader.get_type_list('PLANES_TD2')):
                        _diccionario['sopcion'] = body.stype
                        if body.v1 is not None:
                            _diccionario['_V1'] = body.v1
                            if body.v2 is not None:
                                _diccionario['_V2'] = body.v2

                        data = repository.getData_Planes(_diccionario)
                        dt_ = frt.formated_ADPlan(data, body.stype)
                        return jsonify(dt_), 200
                elif body.type == 'COMBO':
                    if body.stype == 'PLAN':
                        _V1 = body.v1
                        _diccionario = {
                            "popcion": "COMBO",
                            "sopcion": 1,
                            "_V1": _V1
                        }
                        data_cpl = repository.getData_Planes(_diccionario)
                        dt_cpl = frt.formated_COPlan(data_cpl)
                        return jsonify(dt_cpl), 200
                    if body.stype == 'PLANVARIANT':
                        _V1 = body.v1
                        _diccionario = {
                            "popcion": "COMBO",
                            "sopcion": 2,
                            "_V1": _V1
                        }
                        data_cpl = repository.getData_Planes(_diccionario)
                        dt_cpl = frt.formated_COPlanVariant(data_cpl)
                        return jsonify(dt_cpl), 200

                    if body.stype == 'PRODUCTO':
                        _V1 = body.v1
                        _diccionario = {
                            "popcion": "COMBO",
                            "sopcion": 3,
                            "_V1": _V1
                        }
                        data_prd = repository.getData_Planes(_diccionario)
                        dt_prd = frt.formated_COProducto(data_prd)
                        return jsonify(dt_prd), 200

                    if body.stype == 'TIPO_SERVICIO':
                        _V1 = body.v1
                        _diccionario = {
                            "popcion": "COMBO",
                            "sopcion": 4,
                            "_V1": _V1
                        }
                        data_cts = repository.getData_Planes(_diccionario)
                        dt_cts = frt.formated_COTipoServicio(data_cts)
                        return jsonify(dt_cts), 200

                    if body.stype == 'PRODUCTO_ROUTER':
                        _V1 = body.v1
                        _diccionario = {
                            "popcion": "COMBO",
                            "sopcion": 8
                        }
                        data_prd = repository.getData_Planes(_diccionario)
                        dt_prd = frt.formated_COProducto(data_prd)
                        return jsonify(dt_prd), 200
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
            response = {
                'errorCode': http_err.response.status_code,
                'message': http_err.response.text,
                'externalTransactionId': body.external_transaction_id,
                'internalTransactionId': internal_transaction_id
            }
            return jsonify(response), 400
