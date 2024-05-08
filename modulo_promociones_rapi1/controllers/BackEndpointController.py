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
                _type = _type.upper()
                if _type == 'ALL_PROVS':
                    return BackEndpointController.make_request('http://localhost:5011/api/ms/peticionPlaces',
                                                               {"type": "ALL_PROVS"})
                elif _type == 'SPECIFIC_PROVXTT':
                    TARIFFPLANVARIANT = request.args.get('TARIFFPLANVARIANT')
                    return BackEndpointController.make_request('http://localhost:5011/api/ms/peticionPlaces',
                                                               {"type": _type,
                                                                "_V1": TARIFFPLANVARIANT})
                elif _type == 'ALL_CITIES':
                    return BackEndpointController.make_request('http://localhost:5011/api/ms/peticionPlaces',
                                                               {"type": "ALL_PROVS"})
                elif _type == 'CITY_SPECIFIC':
                    _idProv = request.args.get('id_Prov')
                    return BackEndpointController.make_request('http://localhost:5011/api/ms/peticionPlaces',
                                                               {"type": "CITY_SPECIFIC", "id_Prov": _idProv})
                elif _type == 'ALL_SECTORS':
                    return BackEndpointController.make_request('http://localhost:5011/api/ms/peticionPlaces',
                                                               {"type": "ALL_SECTORS"})
                elif _type == 'SECTOR_SPECIFIC':
                    _idCity = request.args.get('id_City')
                    return BackEndpointController.make_request('http://localhost:5011/api/ms/peticionPlaces',
                                                               {"type": "SECTOR_SPECIFIC", "id_City": _idCity})
                elif _type == 'SPECIFIC_CITYXTT':
                    _idProv = request.args.get('id_Prov')
                    TARIFFPLANVARIANT = request.args.get('TARIFFPLANVARIANT')
                    return BackEndpointController.make_request('http://localhost:5011/api/ms/peticionPlaces',
                                                               {"type": _type,
                                                                "id_Prov": _idProv,
                                                                "_V1": TARIFFPLANVARIANT})
                elif _type == 'ALL_SUB_SECTORS':
                    return BackEndpointController.make_request('http://localhost:5011/api/ms/peticionPlaces',
                                                               {"type": "ALL_SUB_SECTORS"})
                elif _type == 'SUB_SECTOR_SPECIFIC':
                    _idSector = request.args.get('id_Sector')
                    return BackEndpointController.make_request('http://localhost:5011/api/ms/peticionPlaces',
                                                               {"type": "SUB_SECTOR_SPECIFIC", "id_Sector": _idSector})
                elif _type == 'SPECIFIC_SECTXTT':
                    _idCity = request.args.get('id_City')
                    TECNOLOGIA = request.args.get('TECNOLOGIA')
                    TARIFFPLANVARIANT = request.args.get('TARIFFPLANVARIANT')
                    return BackEndpointController.make_request('http://localhost:5011/api/ms/peticionPlaces',
                                                               {"type": _type,
                                                                "id_City": _idCity,
                                                                "_V1": TARIFFPLANVARIANT})
                elif _type == 'SECTMXTT':
                    _idCities = request.args.getlist('id_Cities')
                    TARIFFPLANVARIANT = request.args.get('TARIFFPLANVARIANT')
                    return BackEndpointController.make_request('http://localhost:5011/api/ms/peticionPlaces',
                                                               {"type": _type,
                                                                "id_Cities": _idCities,
                                                                "_V1": TARIFFPLANVARIANT})
                else:
                    return jsonify({'error': ' BACK ENDPOINT - Tipo de petición no válido'}), 400
            else:
                return jsonify({'error': 'BACK ENDPOINT - Tipo no proporcionado'}), 400
        except Exception as e:
            print("--------------------------------------------------------------------")
            print("back_endpoint - back_endpoint | Error Detectado: ", e)
            print("--------------------------------------------------------------------")
            return jsonify({'Error': 'Error interno'}), 500
