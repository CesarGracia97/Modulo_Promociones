from flask import Blueprint, request, jsonify
import requests

burop_bp = Blueprint('rapi_burop_GET', __name__)
mpagp_bp = Blueprint('rapi_mpagp_GET', __name__)


class FrontEndpointController:
    @burop_bp.route('/api/ra/fncburo_endpoint', methods=['GET'])
    def burop_endpoint():
        try:
            print("\nFinancial - Buro")
            print("Fase de Escucha | FRONT-ENDPOINT ACTIVADO")
            print("COMBO ENDPOINT ACTIVO\n")
            _type = request.args.get('type')
            if _type and _type.upper() == 'ALL_BURO':
                params = {'type': 'ALL_BURO'}
                response = requests.get('http://localhost:5013/api/ra/plcback_endpoint', params=params)
                return response.text, response.status_code
            else:
                print("burop_endpoint - FrontEndpointController | Tipo de Petición no válido")
                return jsonify({'error': 'Tipo de petición no válido'}), 400
        except Exception as e:
            print("--------------------------------------------------------------------")
            print("burop_endpoint - FrontEndpointController | Error Detectado: ", e)
            print("--------------------------------------------------------------------")
            return jsonify({'Error': e})

    @mpagp_bp.route('/api/ra/fncmpag_endpoint', methods=['GET'])
    def mpagp_endpoint():
        try:
            print("\nFinancial - Modos de Pago")
            print("Fase de Escucha | FRONT-ENDPOINT ACTIVADO")
            print("COMBO ENDPOINT ACTIVO\n")
            _type = request.args.get('type')
            if _type and _type.upper() == 'ALL_MPAGOS':
                params = {'type': 'ALL_MPAGOS'}
                response = requests.get('http://localhost:5013/api/ra/plcback_endpoint', params=params)
                return response.text, response.status_code
            else:
                print("mpagp_endpoint - FrontEndpointController | Tipo de Petición no válido")
                return jsonify({'error': 'Tipo de petición no válido'}), 400
        except Exception as e:
            print("--------------------------------------------------------------------")
            print("mpagp_endpoint - FrontEndpointController | Error Detectado: ", e)
            print("--------------------------------------------------------------------")
            return jsonify({'Error': e})