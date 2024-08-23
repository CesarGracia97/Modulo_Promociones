import connexion
from flask import jsonify
from swagger_server.models.request_get_planes import RequestGetPlanes  # noqa: E501
from swagger_server.repository.planes_Repository import planes_Repository
from swagger_server.uses_cases.FormattedPlans import FormattedPlans


def get_planes(body=None):  # noqa: E501
    """get_planes Consulta de Datos de Provincias segun sus parametros. # noqa: E501 """
    _type = None
    try:
        if connexion.request.is_json:
            stype_valid = {'SERV', 'TECN', 'TISE', 'OFER'}
            valid_stype = {'AD_TARIFFPLAN', 'AD_TARIFFPLANVARIANT', 'AD_TARIFFPLAN_TARIFFPLANVARIANT',
                           'AD_TARIFFPLANVARIANT_PRODUCTO_ADICIONAL'}

            frt = FormattedPlans()
            repository = planes_Repository()
            body = RequestGetPlanes.from_dict(connexion.request.get_json())  # noqa: E501
            if body.channel == 'api-modulos-promocionales-planes':
                print("*** FASE DE ESCUCHA ACTIVA ***")
                print(body.type)
                _type = body.type
                _diccionario = {}
                if body.type == 'ALL_DATA':
                    print(body.stype)
                    stype_valid = {'SERV', 'TECN', 'TISE', 'OFER'}
                    valid_stype = {'AD_TARIFFPLAN', 'AD_TARIFFPLANVARIANT', 'AD_TARIFFPLAN_TARIFFPLANVARIANT',
                                   'AD_TARIFFPLANVARIANT_PRODUCTO_ADICIONAL'}
                    _diccionario['popcion'] = body.stype

                    if body.stype in stype_valid:
                        _diccionario['sopcion'] = body.stype
                        data = repository.getData_Planes(_diccionario)
                        dt_ = frt.formated_TypeALL(body.stype, data)
                        return jsonify(dt_), 200

                    if body.stype in valid_stype:
                        _diccionario['sopcion'] = body.stype
                        if body.v1 is not None:
                            _diccionario['_V1'] = body.v1
                            if '_V2' is not None:
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
                    return jsonify({'error': 'El valor del campo "tipo" no es válido'}), 400

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
