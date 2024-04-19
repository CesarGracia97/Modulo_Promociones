from flask import Blueprint, jsonify, request

receptor_bfinan = Blueprint('ms_peticionFinance', __name__)


class PeticionFinanController:

    @receptor_bfinan.route('/api/ms/peticionFinance', methods=['GET'])
    def faseEscucha():
        try:
            print("\n*** FASE DE ESCUCHA ACTIVA ***\n")

        except Exception as e:
            print("--------------------------------------------------------------------")
            print("faseEscucha - PeticionFinanController | Error detectado: ", e)
            print("--------------------------------------------------------------------")
            return jsonify({'Error': str(e)}), 400
