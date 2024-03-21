from flask import Blueprint, request, jsonify
import requests

provp_bp = Blueprint('rapi_provp_GET', __name__)
cityp_bp = Blueprint('rapi_cityp_GET', __name__)
sectp_bp = Blueprint('rapi_sectp_GET', __name__)
ssecp_bp = Blueprint('rapi_ssecp_GET', __name__)


class FrontEndpointController:

    @provp_bp.route('/api/ra/plcprov_endpoint', methods=['GET'])
    def prov_endpoint():
        try:
            print("PLACES - LUGARES")
            print("\nFase de Escucha | ENDPOINT - F ACTIVADO")
            print("PROVS ENDPOINT ACTIVO\n")
            # Obtener parámetros de consulta de la URL
            _type = request.args.get('type')

            if _type and _type.upper() == 'ALL_PROVS':
                params = {'type': 'ALL_PROVS'}
                response = requests.get('http://localhost:5012/api/ra/plcback_endpoint', params=params)
                return response.text, response.status_code
            else:
                print("prov_endpoint - FrontEndpointController | Tipo de Petición no válido")
                return jsonify({'error': 'Tipo de petición no válido'}), 400
        except Exception as e:
            print("--------------------------------------------------------------------")
            print("prov_endpoint - FrontEndpointController | Error Detectado: ", e)
            print("--------------------------------------------------------------------")
            return jsonify({'Error': e})

    @cityp_bp.route('/api/ra/plccity_endpoint', methods=['GET'])
    def city_endpoint():
        try:
            print("\nFase de Escucha | ENDPOINT - F ACTIVADO")
            print("CITY ENDPOINT ACTIVO\n")
            data = request.json
            _type = data.get('type')
            if _type.upper() == 'ALL_CITIES':
                params = {'type': 'ALL_CITIES'}
                response = requests.get('http://localhost:5012/api/ra/plcback_endpoint', params=params)
                return response.text, response.status_code
            if _type.upper() == 'CITY_SPECIFIC':
                print("CIUDAD ESPECIFICA POR PROVINCIA ENDPOINT ACTIVO\n")
                _idProv = data.get('id_Prov')
                params = {'type': 'CITY_SPECIFIC',
                          'id_Prov': _idProv}
                response = requests.get('http://localhost:5012/api/ra/plcback_endpoint', params=params)
                return response.text, response.status_code
            else:
                print("city_endpoint - FrontEndpointController | Tipo de Peticion no valido")
                return jsonify({'error': 'Tipo de petición no válido'}), 400
        except Exception as e:
            print("--------------------------------------------------------------------")
            print("city_endpoint - FrontEndpointController | Error Detectado: ", e)
            print("--------------------------------------------------------------------")
            return jsonify({'Error': e})

    @sectp_bp.route('/api/ra/plcsector_endpoint', methods=['GET'])
    def sector_endpoint():
        try:
            print("\nFase de Escucha | ENDPOINT - F ACTIVADO")
            print("SECTOR ENDPOINT ACTIVO\n")
            data = request.json
            _type = data.get('type')
            if _type.upper() == 'ALL_SECTORS':
                params = {'type': 'ALL_SECTORS'}
                response = requests.get('http://localhost:5012/api/ra/plcback_endpoint', params=params)
                return response.text, response.status_code
            elif _type.upper() == 'SECTOR_SPECIFIC':
                print("SECTOR ESPECIFICO POR CIUDAD ENDPOINT ACTIVO\n")
                _idCity = data.get('id_City')
                params = {'type': 'SECTOR_SPECIFIC',
                          'id_City': _idCity }
                response = requests.get('http://localhost:5012/api/ra/plcback_endpoint', params=params)
                return response.text, response.status_code
            else:
                print("sectors_endpoint - FrontEndpointController | Tipo de Peticion no valido")
                return jsonify({'error': 'Tipo de petición no válido'}), 400
        except Exception as e:
            print("--------------------------------------------------------------------")
            print("sectors_endpoint - FrontEndpointController | Error Detectado: ", e)
            print("--------------------------------------------------------------------")
            return jsonify({'Error': e})

    @ssecp_bp.route('/api/ra/plcssector_endpoint', methods=['GET'])
    def sub_sector_endpoint():
        try:
            print("\nFase de Escucha | ENDPOINT - F ACTIVADO")
            print("SUB SECTOR ENDPOINT ACTIVO\n")
            data = request.json
            _type = data.get('type')
            if _type.upper() == 'ALL_SUB_SECTORS':
                params = {'type': 'ALL_SUB_SECTORS'}
                response = requests.get('http://localhost:5012/api/ra/plcback_endpoint', params=params)
                return response.text, response.status_code
            elif _type.upper() == 'SUB_SECTOR_SPECIFIC':
                print("SUB SECTOR ESPECIFICO POR SECTOR ENDPOINT ACTIVO\n")
                _idSector = data.get('id_Sector')
                params = {'type': 'SUB_SECTOR_SPECIFIC',
                          'id_Sector': _idSector}
                response = requests.get('http://localhost:5012/api/ra/plcback_endpoint', params=params)
                return response.text, response.status_code
            else:
                print("sub_sectors_endpoint - FrontEndpointController | Tipo de Peticion no valido")
                return jsonify({'error': 'Tipo de petición no válido'}), 400
        except Exception as e:
            print("--------------------------------------------------------------------")
            print("sub_sectors_endpoint - FrontEndpointController | Error Detectado: ", e)
            print("--------------------------------------------------------------------")
            return jsonify({'Error': e})




