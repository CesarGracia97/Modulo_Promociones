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

        except Exception as e:
            print("--------------------------------------------------------------------")
            print("faseEscucha - PeticionFinanController | Error detectado: ", e)
            print("--------------------------------------------------------------------")
            return jsonify({'Error': str(e)}), 400
