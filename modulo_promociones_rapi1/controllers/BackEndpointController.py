import requests
from flask import Blueprint, jsonify, request

backp_bp = Blueprint('rapi_backp_GET', __name__)
URL_BASE = 'http://127.0.0.1:5012/'

URL_Lugares = 'rest/getdata-modulos-promocionales-api/v1.0/places'
Lugares = ['/provincias', '/ciudades', '/sectores', '/masivo']

URL_Planes = 'rest/getdata-modulos-promocionales-api/v1.0/planes'
Planes = ['/ofertas', '/servicios', '/combos', '/planes']

URL_Finanzas = 'rest/getdata-modulos-promocionales-api/v1.0/finance'
Finanzas = ['/buro', '/modos-pago', '/datos-promocionales']


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
            referer = request.headers.get('Referer')

            if referer:
                if any((URL_BASE + URL_Lugares + ruta) in referer for ruta in Lugares):
                    print("\nFase de Escucha | ENDPOINT ACTIVADO")
                    print("PLACE - Lugares")
                    print("BACK ENDPOINT ACTIVO\n")
                    _type = request.args.get('type')
                    if _type:
                        _provincias = {"ALL_PROVS", "PROVINCIAS_ESPECIFICASxTFV"}
                        _ciudades = {"ALL_CITIES", "CIUDADES_ESPECIFICASxPROV", "CIUDADES_ESPECIFICASxTFV",
                                     "CIUDADES_ESPECIFICASxPROVxTFV", "CIUDADES_ESPECIFICASxTFVxPROD"}
                        _sectores = {"ALL_SECTORS", "SECTORES_ESPECIFICOSxCITY", "SECTORES_ESPECIFICOSxTFV",
                                     "SECTORES_ESPECIFICOSxCITYxTFV"}
                        _masive = {"CIUDADES_ESPECIFICASxPROVxTFV", "CIUDADES_ESPECIFICASxTFVxPROD"
                                                                    "SECTORES_ESPECIFICOSxCITYxTFV",
                                   "SECTORES_ESPECIFICOSxCITYxTFVxPROD"}
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
                                if 'PRODUCTOID' in request.args:
                                    payload['_V2'] = request.args.get('PRODUCTOID')
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
                                if 'TARIFFPLANVARIANT' in request.args:
                                    payload['_V2'] = request.args.get('TARIFFPLANVARIANT')
                                if 'PRODUCTOID' in request.args:
                                    payload['_V3'] = request.args.get('PRODUCTOID')
                            payload['MASIVE'] = request.args.get('MASIVE')
                            return BackEndpointController.make_request('http://localhost:5011/api/ms/peticionPlaces',
                                                                       payload)
                        else:
                            return jsonify({'error': ' BACK ENDPOINT - Tipo de petición no válido'}), 400
                    else:
                        return jsonify({'error': 'BACK ENDPOINT - Tipo no proporcionado'}), 400

                elif any((URL_BASE + URL_Planes + ruta) in referer for ruta in Planes):
                    print("\nFase de Escucha | BACK-ENDPOINT ACTIVADO")
                    print("PLANS - Planes")
                    print("BACK ENDPOINT ACTIVO\n")

                    if request.args.get('type') == 'ALL_DATA':
                        valid_stype = {'OFER', 'SERV', 'TECN', 'TISE'}
                        params = {}
                        stype_valid = {'AD_TARIFFPLAN', 'AD_TARIFFPLANVARIANT', 'AD_TARIFFPLAN_TARIFFPLANVARIANT',
                                       'AD_TARIFFPLANVARIANT_PRODUCTO_ADICIONAL'}
                        if request.args.get('stype') in valid_stype:
                            params = {'type': request.args.get('type'), 'stype': request.args.get('stype')}

                        elif request.args.get('stype') in stype_valid:
                            params['type'] = request.args.get('type')
                            params['stype'] = request.args.get('stype')
                            if '_V1' in request.args:
                                params['_V1'] = request.args.get('_V1')
                                if '_V2' in request.args:
                                    params['_V2'] = request.args.get('_V2')
                        return BackEndpointController.make_request('http://localhost:5011/api/ms/peticionPlanes',
                                                                   params)
                    elif request.args.get('type') == 'COMBO':
                        return BackEndpointController.make_request('http://localhost:5011/api/ms/peticionPlanes',
                                                                   request.args)

                elif any((URL_BASE + URL_Finanzas + ruta) in referer for ruta in Finanzas):
                    print("\nFase de Escucha | BACK-ENDPOINT ACTIVADO")
                    print("FINANCE - Finance")
                    print("BACK ENDPOINT ACTIVO\n")
                    _type = request.args.get('type')
                    if _type:
                        _type = _type.upper()
                        valid_type = {"ALL_MPAGOS", "ALL_BURO", "DIAS_GOZADOS", "PRECIO_REGULAR", "UPGRADE"}
                        payload = {"type": _type}
                        if _type in valid_type:
                            if '_V1' in request.args:
                                payload['_V1'] = request.args.get('_V1')
                                if '_V2' in request.args:
                                    payload['_V2'] = request.args.get('_V2')
                            return BackEndpointController.make_request('http://localhost:5011/api/ms/peticionFinance',
                                                                       payload)

                else:
                    print("La solicitud proviene de una URL desconocida")
            else:
                print("No se proporcionó el encabezado Referer")
        except Exception as e:
            print("--------------------------------------------------------------------")
            print("back_endpoint - back_endpoint | Error Detectado: ", e)
            print("--------------------------------------------------------------------")
            return jsonify({'Error': 'Error interno'}), 500
