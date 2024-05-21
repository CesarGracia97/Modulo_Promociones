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

    @backp_bp.route('/api/ra/plnback_endpoint', methods=['GET'])
    def back_endpoint():
        try:
            print("\nFase de Escucha | BACK-ENDPOINT ACTIVADO")
            print("BACK ENDPOINT ACTIVO\n")
            if request.args.get('type') == 'ALL_DATA':
                valid_stype = {'OFER', 'SERV', 'TECN', 'TISE'}
                params = {}
                stype_valid = {'AD_TARIFFPLAN', 'AD_TARIFFPLANVARIANT', 'AD_TARIFFPLAN_TARIFFPLANVARIANT',
                               'AD_TARIFFPLANVARIANT_PRODUCTO_ADICIONAL'}
                if request.args.get('stype') in valid_stype:
                    params = {'type': request.args.get('type'), 'stype': request.args.get('stype')}

                elif request.args.get('stype') in stype_valid:
                    if '_V1' in request.args:
                        params['_V1'] = request.args.get('_V1')
                        if '_V2' in request.args:
                            params['_V2'] = request.args.get('_V2')
                return BackEndpointController.make_request('http://localhost:5011/api/ms/peticionPlanes',
                                                           params)
            elif request.args.get('type') == 'COMBO':
                return BackEndpointController.make_request('http://localhost:5011/api/ms/peticionPlanes',
                                                           request.args)
        except Exception as e:
            print("--------------------------------------------------------------------")
            print("back_endpoint - BackEndpointController | Error Detectado: ", e)
            print("--------------------------------------------------------------------")
            return jsonify({'Error': e})
