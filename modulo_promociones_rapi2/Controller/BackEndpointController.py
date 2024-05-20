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
            _type = request.args.get('type')
            if _type:
                _type = _type.upper()
                if _type == 'ALL_DATA':
                    _stype = request.args.get('stype')
                    _stype = _stype.upper()
                    _ttype = request.args.get('ttype')
                    _ttype = _ttype.upper()
                    if (_stype in ['OFER', 'SERV', 'TECN', 'TISE'] or
                            (_stype == 'PLAN' and (_ttype == '1' or _ttype == '3' or _ttype == '4'))):
                        params = {'type': _type, 'stype': _stype, 'ttype': _ttype}
                        return BackEndpointController.make_request('http://localhost:5011/api/ms/peticionPlanes',
                                                                   params)
                    elif _stype == 'PLAN' and _ttype == '2':
                        _V1 = request.args.get('_V1')
                        _V2 = request.args.get('_V2')
                        _V3 = request.args.get('_V3')
                        params = {'type': _type, 'stype': _stype, 'ttype': _ttype, '_V1': _V1, '_V2': _V2, '_V3': _V3}
                        return BackEndpointController.make_request('http://localhost:5011/api/ms/peticionPlanes',
                                                                   params)
                    else:
                        return jsonify({'error': ' BACK ENDPOINT - Tipo de petición no válido'}), 400
                elif _type == 'COMBO':
                    return BackEndpointController.make_request('http://localhost:5011/api/ms/peticionPlanes',
                                                               request.args)
                else:
                    return jsonify({'error': ' BACK ENDPOINT - Tipo de petición no válido'}), 400
        except Exception as e:
            print("--------------------------------------------------------------------")
            print("back_endpoint - BackEndpointController | Error Detectado: ", e)
            print("--------------------------------------------------------------------")
            return jsonify({'Error': e})


