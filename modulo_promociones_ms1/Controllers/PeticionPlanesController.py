from flask import Blueprint, jsonify, request
from Repository.PlansRepository import PlansRepository
from Services.FormattedPlans import FormattedPlans

receptor_bpln = Blueprint('ms_peticionPlanes', __name__)


class PeticionPlanesController:
    @receptor_bpln.route('/api/ms/peticionPlanes', methods=['GET'])
    def faseEscucha():
        try:
            print("\n*** FASE DE ESCUCHA ACTIVA ***\n")
            frt = FormattedPlans()
            repository = PlansRepository()
            print(request.args.get('type'))
            _diccionario = {}
            if request.args.get('type') == 'ALL_DATA':
                print(request.args.get('stype'))
                stype_valid = {'SERV', 'TECN', 'TISE', 'OFER'}
                valid_stype = {'AD_TARIFFPLAN', 'AD_TARIFFPLANVARIANT', 'AD_TARIFFPLAN_TARIFFPLANVARIANT',
                               'AD_TARIFFPLANVARIANT_PRODUCTO_ADICIONAL'}
                _diccionario['popcion'] = request.args.get('type')

                if request.args.get('stype') in stype_valid:
                    _diccionario['sopcion'] = request.args.get('stype')
                    data = repository.getData_Planes(_diccionario)
                    dt_ = frt.formated_TypeALL(request.args.get('stype'), data)
                    return jsonify(dt_), 200

                if request.args.get('stype') in valid_stype:
                    _diccionario['sopcion'] = request.args.get('stype')
                    if '_V1' in request.args:
                        _diccionario['_V1'] = request.args.get('_V1')
                        if '_V2' in request.args:
                            _diccionario['_V2'] = request.args.get('_V2')

                    data = repository.getData_Planes(_diccionario)
                    dt_ = frt.formated_ADPlan(data, request.args.get('stype'))
                    return jsonify(dt_), 200
            elif request.args.get('type') == 'COMBO':
                _stype = request.args.get('stype')
                if _stype.upper() == 'PLAN':
                    _V1 = request.args.get('_V1')
                    _diccionario = {
                        "popcion": "COMBO",
                        "sopcion": 1,
                        "_V1": _V1
                    }
                    data_cpl = repository.getData_Planes(_diccionario)
                    dt_cpl = frt.formated_COPlan(data_cpl)
                    return jsonify(dt_cpl), 200
                if _stype.upper() == 'PLANVARIANT':
                    _V1 = request.args.get('_V1')
                    _diccionario = {
                        "popcion": "COMBO",
                        "sopcion": 2,
                        "_V1": _V1
                    }
                    data_cpl = repository.getData_Planes(_diccionario)
                    dt_cpl = frt.formated_COPlanVariant(data_cpl)
                    return jsonify(dt_cpl), 200

                if _stype.upper() == 'PRODUCTO':
                    _V1 = request.args.get('_V1')
                    _diccionario = {
                        "popcion": "COMBO",
                        "sopcion": 3,
                        "_V1": _V1
                    }
                    data_prd = repository.getData_Planes(_diccionario)
                    dt_prd = frt.formated_COProducto(data_prd)
                    return jsonify(dt_prd), 200

                if _stype.upper() == 'TIPO_SERVICIO':
                    _V1 = request.args.get('_V1')
                    _diccionario = {
                        "popcion": "COMBO",
                        "sopcion": 4,
                        "_V1": _V1
                    }
                    data_cts = repository.getData_Planes(_diccionario)
                    dt_cts = frt.formated_COTipoServicio(data_cts)
                    return jsonify(dt_cts), 200

                if _stype.upper() == 'PROVINCIA':
                    _V1 = request.args.get('_V1')
                    _V2 = request.args.get('_V2')
                    _V3 = request.args.get('_V3')
                    _V4 = request.args.get('_V4')
                    _diccionario = {
                        "popcion": "COMBO",
                        "sopcion": 5,
                        "_V1": _V1,
                        "_V2": _V2,
                        "_V3": _V3,
                        "_V4": _V4
                    }
                    data_cpr = repository.getData_Planes(_diccionario)
                    dt_cpr = frt.formated_COProvincia(data_cpr)
                    return jsonify(dt_cpr), 200

                if _stype.upper() == 'CIUDAD':
                    _V1 = request.args.get('_V1')
                    _V2 = request.args.get('_V2')
                    _V3 = request.args.get('_V3')
                    _V4 = request.args.get('_V4')
                    _V5 = request.args.get('_V5')
                    _diccionario = {
                        "popcion": "COMBO",
                        "sopcion": 6,
                        "_V1": _V1,
                        "_V2": _V2,
                        "_V3": _V3,
                        "_V4": _V4,
                        "_V5": _V5
                    }
                    data_cct = repository.getData_Planes(_diccionario)
                    dt_cct = frt.formated_COCiudad(data_cct)
                    return jsonify(dt_cct), 200

                if _stype.upper() == 'SECTOR':
                    _V1 = request.args.get('_V1')
                    _V2 = request.args.get('_V2')
                    _V3 = request.args.get('_V3')
                    _V4 = request.args.get('_V4')
                    _V5 = request.args.get('_V5')
                    _V6 = request.args.get('_V6')
                    _diccionario = {
                        "popcion": "COMBO",
                        "sopcion": 7,
                        "_V1": _V1,
                        "_V2": _V2,
                        "_V3": _V3,
                        "_V4": _V4,
                        "_V5": _V5,
                        "_V6": _V6
                    }
                    data_cst = repository.getData_Planes(_diccionario)
                    dt_cst = frt.formated_COSector(data_cst)
                    return jsonify(dt_cst), 200
                if _stype.upper() == 'PRODUCTO_ROUTER':
                    _V1 = request.args.get('_V1')
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
            print("faseEscucha - PeticionPlanesController | Error detectado: ", e)
            print("--------------------------------------------------------------------")
            return jsonify({'Error PlanesController': str(e)}), 400
