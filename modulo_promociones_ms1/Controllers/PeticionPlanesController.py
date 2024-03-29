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
            data = request.json
            _type = data.get('type')
            print(_type)
            if _type is None:
                return jsonify({'error': 'El campo "type" es requerido'}), 400
            if _type.upper() == 'ALL_DATA':
                _stype = data.get('stype')
                print(_stype)
                if _stype.upper() == 'OFER':
                    _ttype = data.get('ttype')
                    if _ttype == '1':
                        _diccionario = {
                            "popcion": "ALL_DATA",
                            "sopcion": "OFER"
                        }
                        data_dtofe = repository.getData_Planes(_diccionario)
                        dt_dtofe = frt.formated_ADOferta(data_dtofe)
                        return jsonify(dt_dtofe), 200
                if _stype.upper() == 'SERV':
                    _ttype = data.get('ttype')
                    if _ttype == '1':
                        _diccionario = {
                            "popcion": "ALL_DATA",
                            "sopcion": "SERV"
                        }
                        data_dtof = repository.getData_Planes(_diccionario)
                        dt_dtof = frt.formated_ADServicio(data_dtof)
                        return jsonify(dt_dtof), 200
                if _stype.upper() == 'TECN':
                    _ttype = data.get('ttype')
                    if _ttype == '1':
                        _diccionario = {
                            "popcion": "ALL_DATA",
                            "sopcion": "TECN"
                        }
                        data_dttec = repository.getData_Planes(_diccionario)
                        dt_dttec = frt.formated_ADTecnologia(data_dttec)
                        return jsonify(dt_dttec), 200
                if _stype.upper() == 'TISE':
                    _ttype = data.get('ttype')
                    if _ttype == '1':
                        _diccionario = {
                            "popcion": "ALL_DATA",
                            "sopcion": "TISE"
                        }
                        data_dttis = repository.getData_Planes(_diccionario)
                        dt_dttis = frt.formated_ADTipoServicio(data_dttis)
                        return jsonify(dt_dttis), 200
                if _stype.upper() == 'PLAN':
                    _ttype = data.get('ttype')
                    if _ttype == '1':
                        _diccionario = {
                            "popcion": "ALL_DATA",
                            "sopcion": "PLAN",
                            "topcion": 1
                        }
                        data_dtpl1 = repository.getData_Planes(_diccionario)
                        dt_dtpl1 = frt.formated_ADPlan(data_dtpl1, 1)
                        return jsonify(dt_dtpl1), 200
                    if _ttype == '2':
                        _V1 = data.get('_V1')
                        _V2 = data.get('_V2')
                        _V3 = data.get('_V3')
                        _diccionario = {
                            "popcion": "ALL_DATA",
                            "sopcion": "PLAN",
                            "topcion": 2,
                            "_V1": _V1,
                            "_V2": _V2,
                            "_V3": _V3
                        }
                        data_dtpl2 = repository.getData_Planes(_diccionario)
                        dt_dtpl2 = frt.formated_ADPlan(data_dtpl2, 2)
                        return jsonify(dt_dtpl2), 200
                    if _ttype == '3':
                        _diccionario = {
                            "popcion": "ALL_DATA",
                            "sopcion": "PLAN",
                            "topcion": 3
                        }
                        data_dtpl3 = repository.getData_Planes(_diccionario)
                        dt_dtpl3 = frt.formated_ADPlan(data_dtpl3, 3)
                        return jsonify(dt_dtpl3), 200
            elif _type.upper() == 'COMBO':
                _stype = data.get('stype')
                if _stype.upper() == 'TIPO_SERVICIOS':
                    _V1 = data.get('_V1')
                    _diccionario = {
                        "popcion": "COMBO",
                        "sopcion": 1,
                        "_V1": _V1
                    }
                    data_cts = repository.getData_Planes(_diccionario)
                    dt_cts = frt.formated_COTipoServicio(data_cts)
                    return jsonify(dt_cts), 200
                if _stype.upper() == 'RED_TECNOLOGIA':
                    _V1 = data.get('_V1')
                    _V2 = data.get('_V2')
                    _diccionario = {
                        "popcion": "COMBO",
                        "sopcion": 2,
                        "_V1": _V1,
                        "_V2": _V2
                    }
                    data_crt = repository.getData_Planes(_diccionario)
                    dt_crt = frt.formated_CORedTecnologia(data_crt)
                    return jsonify(dt_crt), 200

                if _stype.upper() == 'PLANES':
                    _V1 = data.get('_V1')
                    _V2 = data.get('_V2')
                    _V3 = data.get('_V3')
                    _diccionario = {
                        "popcion": "COMBO",
                        "sopcion": 3,
                        "_V1": _V1,
                        "_V2": _V2,
                        "_V3": _V3
                    }
                    data_cpl = repository.getData_Planes(_diccionario)
                    dt_cpl = frt.formated_COPlanes(data_cpl)
                    return jsonify(dt_cpl), 200

                if _stype.upper() == 'PROVINCIA':
                    _V1 = data.get('_V1')
                    _V2 = data.get('_V2')
                    _V3 = data.get('_V3')
                    _V4 = data.get('_V4')
                    _diccionario = {
                        "popcion": "COMBO",
                        "sopcion": 4,
                        "_V1": _V1,
                        "_V2": _V2,
                        "_V3": _V3,
                        "_V4": _V4
                    }
                    data_cpr = repository.getData_Planes(_diccionario)
                    dt_cpr = frt.formated_COProvincia(data_cpr)
                    return jsonify(dt_cpr), 200
                if _stype.upper() == 'CIUDAD':
                    _V1 = data.get('_V1')
                    _V2 = data.get('_V2')
                    _V3 = data.get('_V3')
                    _V4 = data.get('_V4')
                    _V5 = data.get('_V5')
                    _diccionario = {
                        "popcion": "COMBO",
                        "sopcion": 5,
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
                    _V1 = data.get('_V1')
                    _V2 = data.get('_V2')
                    _V3 = data.get('_V3')
                    _V4 = data.get('_V4')
                    _V5 = data.get('_V5')
                    _V6 = data.get('_V6')
                    _diccionario = {
                        "popcion": "COMBO",
                        "sopcion": 6,
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

            else:
                return jsonify({'error': 'El valor del campo "tipo" no es válido'}), 400

        except Exception as e:
            print("--------------------------------------------------------------------")
            print("faseEscucha - PeticionPlanesController | Error detectado: ", e)
            print("--------------------------------------------------------------------")
            return jsonify({'Error PlanesController': str(e)}), 400
