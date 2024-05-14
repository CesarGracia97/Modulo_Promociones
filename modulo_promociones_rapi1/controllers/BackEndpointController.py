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
            print("PLACE - Lugares")
            print("BACK ENDPOINT ACTIVO\n")

            _type = request.args.get('type')

            if _type:

                _provincias = {"ALL_PROVS", "PROVINCIAS_ESPECIFICASxTFV"}
                _ciudades = {"ALL_CITIES", "CIUDADES_ESPECIFICASxPROV", "CIUDADES_ESPECIFICASxTFV",
                             "CIUDADES_ESPECIFICASxPROVxTFV"}
                _sectores = {"ALL_SECTORS", "SECTORES_ESPECIFICOSxCITY", "SECTORES_ESPECIFICOSxTFV",
                             "SECTORES_ESPECIFICOSxCITYxTFV"}
                _masive = {"CIUDADES_ESPECIFICASxPROVxTFV", "SECTORES_ESPECIFICOSxCITYxTFV"}
                payload = {"type": _type}

                if _type in _provincias:
                    if 'TARIFFPLANVARIANT' in request.args:
                        payload['_V1'] = request.args.get('TARIFFPLANVARIANT')
                    return BackEndpointController.make_request('http://localhost:5011/api/ms/peticionPlaces',
                                                               payload)
                elif _type in _ciudades and not request.args.get('MASIVE'):
                    if 'id_Prov' in request.args:
                        payload['_V1'] = request.args.get('id_Prov')
                        if 'TARIFFPLANVARIANT' in request.args:
                            payload['_V2'] = request.args.get('TARIFFPLANVARIANT')
                    if 'TARIFFPLANVARIANT' in request.args and '_V1' not in payload:
                        payload['_V1'] = request.args.get('TARIFFPLANVARIANT')
                    return BackEndpointController.make_request('http://localhost:5011/api/ms/peticionPlaces',
                                                               payload)

                elif _type in _sectores and not request.args.get('MASIVE'):
                    if 'id_City' in request.args:
                        payload['_V1'] = request.args.get('id_City')
                        if 'TARIFFPLANVARIANT' in request.args:
                            payload['_V2'] = request.args.get('TARIFFPLANVARIANT')
                    if 'TARIFFPLANVARIANT' in request.args and '_V1' not in payload:
                        payload['_V1'] = request.args.get('TARIFFPLANVARIANT')
                    return BackEndpointController.make_request('http://localhost:5011/api/ms/peticionPlaces',
                                                               payload)

                elif _type in _masive and request.args.get('MASIVE'):
                    if 'id_Provs' in request.args:
                        payload['id_Provs'] = request.args.getlist('id_Provs')
                    if 'id_Cities' in request.args:
                        payload['id_Cities'] = request.args.getlist('id_Cities')
                    payload['_V2'] = request.args.get('TARIFFPLANVARIANT')
                    payload['MASIVE'] = request.args.get('MASIVE')
                    return BackEndpointController.make_request('http://localhost:5011/api/ms/peticionPlaces',
                                                               payload)
                else:
                    return jsonify({'error': ' BACK ENDPOINT - Tipo de petición no válido'}), 400
            else:
                return jsonify({'error': 'BACK ENDPOINT - Tipo no proporcionado'}), 400
        except Exception as e:
            print("--------------------------------------------------------------------")
            print("back_endpoint - back_endpoint | Error Detectado: ", e)
            print("--------------------------------------------------------------------")
            return jsonify({'Error': 'Error interno'}), 500
