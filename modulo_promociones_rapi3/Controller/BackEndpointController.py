import requests
from flask import Blueprint, jsonify, request

backp_bp = Blueprint('rapi_backp_GET', __name__)


class BackEndpointController:
    @staticmethod
    def make_request(endpoint, payload):
        try:
            response = requests.get(endpoint, params=payload)
            response.raise_for_status()
            return response.json(), response.status_code
        except requests.exceptions.RequestException as e:
            print("Error en la solicitud:", e)
            return {'error': e}, 500

    @backp_bp.route('/api/ra/plcback_endpoint', methods=['GET'])
    def back_endpoint():
        try:
            print("\nFase de Escucha | ENDPOINT ACTIVADO")
            print("PLACE - Finance")
            print("BACK ENDPOINT ACTIVO\n")
            _type = request.args.get('type')
            if _type:
                _type = _type.upper()
                if _type == 'ALL_MPAGOS':
                    return BackEndpointController.make_request('http://localhost:5011/api/ms/peticionFinance',
                                                               {"type": "ALL_MPAGOS"})
                elif _type == 'ALL_BURO':
                    return BackEndpointController.make_request('http://localhost:5011/api/ms/peticionFinance',
                                                               {"type": "ALL_BURO"})
        except Exception as e:
            print("--------------------------------------------------------------------")
            print("back_endpoint - back_endpoint | Error Detectado: ", e)
            print("--------------------------------------------------------------------")
            return jsonify({'Error': 'Error interno'}), 500
