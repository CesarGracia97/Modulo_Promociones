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
                valid_type = {"ALL_MPAGOS", "ALL_BURO", "DIAS_GOZADOS", "PRECIO_REGULAR",
                              "UPGRADE"}
                if _type.upper() in valid_type:
                    if '_V1' in request.args:
                        _V1 = request.args.get('_V1')
                        if '_V2' in request.args:
                            _V2 = request.args.get('_V2')
                            return BackEndpointController.make_request('http://localhost:5011/api/ms/peticionFinance',
                                                                       {"type": _type, "_V1": _V1, "_V2": _V2})
                        return BackEndpointController.make_request('http://localhost:5011/api/ms/peticionFinance',
                                                                   {"type": _type, "_V1": _V1})
                    return BackEndpointController.make_request('http://localhost:5011/api/ms/peticionFinance',
                                                               {"type": _type})
        except Exception as e:
            print("--------------------------------------------------------------------")
            print("back_endpoint - back_endpoint | Error Detectado: ", e)
            print("--------------------------------------------------------------------")
            return jsonify({'Error': 'Error interno'}), 500
