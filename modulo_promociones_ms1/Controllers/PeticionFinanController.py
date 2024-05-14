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
            if _type is None:
                return jsonify({'error': 'El campo "type" es requerido'}), 400

            _financial = {"ALL_BURO", "ALL_MPAGOS", "UPGRADE", "PRECIO_REGULAR", "DIAS_GOZADOS"}
            _diccionario = {}
            if _type in _financial:
                _diccionario['name_Query'] = _type
                if '_V1' in request.args:
                    _diccionario['_V1'] = request.args.get('_V1')
                    if '_V2' in request.args:
                        _diccionario['_V2'] = request.args.get('_V2')
                data = repository.getData_Financial(_diccionario)
                dt = frt.formatted_financial(_type, data)
                return jsonify(dt), 200

        except Exception as e:
            print("--------------------------------------------------------------------")
            print("faseEscucha - PeticionFinanController | Error detectado: ", e)
            print("--------------------------------------------------------------------")
            return jsonify({'Error': str(e)}), 400
