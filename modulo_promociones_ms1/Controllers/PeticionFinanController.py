from flask import Blueprint, jsonify, request
from Repository.FinancialRepository import FinancialRepository
from Services.FormattedFinancial import FormattedFinance

receptor_bfinan = Blueprint('ms_peticionFinance', __name__)


class PeticionFinanController:

    @receptor_bfinan.route('/api/ms/peticionFinance', methods=['GET'])
    def faseEscucha():
        try:
            print("\n*** FASE DE ESCUCHA ACTIVA ***\n")
            frt = FormattedFinance()
            repository = FinancialRepository()
            _type = request.args.get('type')
            print(_type)
            if _type is None:
                return jsonify({'error': 'El campo "type" es requerido'}), 400
            if _type.upper() == 'ALL_BURO':
                _diccionario = {
                    "popcion": "ALL_BURO",
                    "sopcion": 1
                }
                data_fnc = repository.getData_Financial(_diccionario)
                dt_financ = frt.formatted_buro(data_fnc)
                return jsonify(dt_financ), 200
            if _type.upper() == 'ALL_MPAGOS':
                _diccionario = {
                    "popcion": "ALL_MPAGOS",
                    "sopcion": 1
                }
                data_fnc = repository.getData_Financial(_diccionario)
                dt_financ = frt.formatted_mpagos(data_fnc)
                return jsonify(dt_financ), 200
            if _type.upper() == 'UPGRADE' or _type.upper() == 'PRECIO_REGULAR' or _type.upper() == 'DIAS_GOZADOS':
                _diccionario = {"popcion": _type}
                if '_V1' in request.args:
                    _diccionario['_V1'] = request.args.get('_V1')
                    if '_V2' in request.args:
                        _diccionario['_V2'] = request.args.get('_V2')
                data_fnc = repository.getData_Financial(_diccionario)
                if _type.upper() == 'UPGRADE':
                    dt_ = frt.formatted_upgrade(data_fnc)
                    return jsonify(dt_), 200
                if _type.upper() == 'PRECIO_REGULAR':
                    dt_ = frt.formatted_pregular(data_fnc)
                    return jsonify(dt_), 200
                if _type.upper() == 'DIAS_GOZADOS':
                    dt_ = frt.formatted_dgozados(data_fnc)
                    return jsonify(dt_), 200
        except Exception as e:
            print("--------------------------------------------------------------------")
            print("faseEscucha - PeticionFinanController | Error detectado: ", e)
            print("--------------------------------------------------------------------")
            return jsonify({'Error': str(e)}), 400
