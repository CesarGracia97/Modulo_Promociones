import requests
from flask import Blueprint, jsonify, request

provp_bp = Blueprint('provincias_GET', __name__)
cityp_bp = Blueprint('ciudades_GET', __name__)
sectp_bp = Blueprint('sectores_GET', __name__)
infmv_bp = Blueprint('masivos_GET', __name__)

__URL__ = 'rest/getdata-modulos-promocionales-api/v1.0/places'


class PlacesEndopointController:
    @provp_bp.route(__URL__ + '/provincias', methods=['GET'])
    def provincias_endpoint():
        try:
            print("PLACES - LUGARES")
            print("\nFase de Escucha | ENDPOINT - F ACTIVADO")
            print("PROVS ENDPOINT ACTIVO\n")

            _type = request.args.get('type')
            _provincias = {"ALL_PROVS", "PROVINCIAS_ESPECIFICASxTFV"}

            if _type.upper() in _provincias:
                params = {'type': _type}
                if 'TARIFFPLANVARIANT' in request.args:
                    params['TARIFFPLANVARIANT'] = request.args.get('TARIFFPLANVARIANT')
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

    @cityp_bp.route(__URL__ + '/ciudades', methods=['GET'])
    def city_endpoint():
        try:
            print("PLACES - LUGARES")
            print("\nFase de Escucha | ENDPOINT - F ACTIVADO")
            print("CITY ENDPOINT ACTIVO\n")

            _type = request.args.get('type')
            _ciudades = {"ALL_CITIES", "CIUDADES_ESPECIFICASxPROV", "CIUDADES_ESPECIFICASxTFV",
                         "CIUDADES_ESPECIFICASxPROVxTFV", "CIUDADES_ESPECIFICASxTFVxPROD"}

            if _type in _ciudades:
                params = {'type': _type}
                if 'id_Prov' in request.args:
                    params['id_Prov'] = request.args.get('id_Prov')
                if 'TARIFFPLANVARIANT' in request.args:
                    params['TARIFFPLANVARIANT'] = request.args.get('TARIFFPLANVARIANT')
                if 'PRODUCTOID' in request.args:
                    params['PRODUCTOID'] = request.args.get('PRODUCTOID')
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

    @sectp_bp.route(__URL__ + '/sectores', methods=['GET'])
    def sector_endpoint():
        try:
            print("PLACES - LUGARES")
            print("\nFase de Escucha | ENDPOINT - F ACTIVADO")
            print("SECTOR ENDPOINT ACTIVO\n")

            _type = request.args.get('type')
            _sectores = {"ALL_SECTORS", "SECTORES_ESPECIFICOSxCITY", "SECTORES_ESPECIFICOSxTFV",
                         "SECTORES_ESPECIFICOSxCITYxTFV", "SECTORES_ESPECIFICOSxCITYxTFVxPROD"}

            if _type.upper() in _sectores:
                params = {'type': _type}
                if 'id_City' in request.args:
                    params['id_City'] = request.args.get('id_City')
                if 'TARIFFPLANVARIANT' in request.args:
                    params['TARIFFPLANVARIANT'] = request.args.get('TARIFFPLANVARIANT')
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

    @infmv_bp.route(__URL__ + '/masivo', methods=['GET'])
    def infomasiva_endpoint():
        try:
            print("PLACES - LUGARES")
            print("\nFase de Escucha | ENDPOINT - F ACTIVADO")
            print("INFORMACION MASIVA ENDPOINT ACTIVO\n")

            _type = request.args.get('type')
            _masivos = {"CIUDADES_ESPECIFICASxPROVxTFV", "SECTORES_ESPECIFICOSxCITYxTFV",
                        "SECTORES_ESPECIFICOSxCITYxTFVxPROD"}

            if _type in _masivos:
                print("Tipo de Peticion: " + _type)
                params = {'type': _type}
                if 'id_Provs' in request.args:
                    params['id_Provs'] = request.args.getlist('id_Provs')
                if 'id_Cities' in request.args:
                    params['id_Cities'] = request.args.getlist('id_Cities')
                if 'TARIFFPLANVARIANT' in request.args:
                    params['TARIFFPLANVARIANT'] = request.args.get('TARIFFPLANVARIANT')
                if 'PRODUCTOID' in request.args:
                    params['PRODUCTOID'] = request.args.get('PRODUCTOID')
                params['MASIVE'] = "YES"
                response = requests.get('http://localhost:5012/api/ra/plcback_endpoint', params=params)
                return response.text, response.status_code

            else:
                print("infomasiva_endpoint - FrontEndpointController | Tipo de Peticion no valido")
                return jsonify({'error': 'Tipo de petición no válido'}), 400
        except Exception as e:
            print("--------------------------------------------------------------------")
            print("infomasiva_endpoint - FrontEndpointController | Error Detectado: ", e)
            print("--------------------------------------------------------------------")
            return jsonify({'Error': e})
