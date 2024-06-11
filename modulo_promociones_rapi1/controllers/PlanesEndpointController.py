import requests
from flask import Blueprint, request, jsonify

combp_bp = Blueprint('rapi_combp_GET', __name__)
oferp_bp = Blueprint('rapi_oferp_GET', __name__)
servp_bp = Blueprint('rapi_servp_GET', __name__)
planp_bp = Blueprint('rapi_planp_GET', __name__)

__URL__ = 'rest/getdata-modulos-promocionales-api/v1.0/planes'


class PlanesEndpointController:

    @oferp_bp.route(__URL__ + '/ofertas', methods=['GET'])
    def oferp_enpoint():
        try:
            print("\nOFERTAS - PLANES")
            print("Fase de Escucha | FRONT-ENDPOINT ACTIVADO")
            print("OFERTAS ENDPOINT ACTIVO\n")
            _type = request.args.get('type')
            if _type.upper() == 'ALL_DATA':
                _stype = request.args.get('stype')
                if _stype.upper() == 'OFER':
                    params = {
                        'type': _type,
                        'stype': _stype
                    }
                    response = requests.get('http://localhost:5013/api/ra/plnback_endpoint', params=params)
                    return response.text, response.status_code

                elif _stype.upper() != 'OFER' and (
                        _stype.upper() == 'SERV' or _stype.upper() == 'TECN' or _stype.upper() == 'TISE' or _stype.upper() == 'PLAN'):
                    mensaje = f"La peticion esta siendo enviada por un canal incorrecto {_stype}"
                    return jsonify({'error': mensaje}), 400

            elif _type.upper() != 'ALL_DATA' and _type.upper() == 'COMBO':
                mensaje = f"La peticion esta siendo enviada por un canal incorrecto {_type}"
                return jsonify({'error': mensaje}), 400

            else:
                print("oferp_enpoint - FrontEndpointController | Tipo de Peticion no valido")
                return jsonify({'error': 'Tipo de petición no válido'}), 400

        except Exception as e:
            print("--------------------------------------------------------------------")
            print("oferp_enpoint - FrontEndpointController | Error Detectado: ", e)
            print("--------------------------------------------------------------------")
            return jsonify({'Error': e})

    @servp_bp.route(__URL__ + '/servicios', methods=['GET'])
    def servp_enpoint():
        try:
            print("\nSERVICIOS - PLANES")
            print("Fase de Escucha | FRONT-ENDPOINT ACTIVADO")
            print("SERVICIOS ENDPOINT ACTIVO\n")
            _type = request.args.get('type')
            if _type.upper() == 'ALL_DATA':
                _stype = request.args.get('stype')
                if _stype.upper() == 'SERV':
                    params = {
                        'type': _type,
                        'stype': _stype
                    }
                    response = requests.get('http://localhost:5013/api/ra/plnback_endpoint', params=params)
                    return response.text, response.status_code

                elif _stype.upper() != 'SERV' and (
                        _stype.upper() == 'OFER' or _stype.upper() == 'TECN' or _stype.upper() == 'TISE' or _stype.upper() == 'PLAN'):
                    mensaje = f"La peticion esta siendo enviada por un canal incorrecto {_stype}"
                    return jsonify({'error': mensaje}), 400

            elif _type.upper() != 'ALL_DATA' and _type.upper() == 'COMBO':
                mensaje = f"La peticion esta siendo enviada por un canal incorrecto {_type}"
                return jsonify({'error': mensaje}), 400

            else:
                print("servp_enpoint - FrontEndpointController | Tipo de Peticion no valido")
                return jsonify({'error': 'Tipo de petición no válido'}), 400

        except Exception as e:
            print("--------------------------------------------------------------------")
            print("servp_enpoint - FrontEndpointController | Error Detectado: ", e)
            print("--------------------------------------------------------------------")
            return jsonify({'Error': e})

    @combp_bp.route(__URL__ + '/combos', methods=['GET'])
    def combp_endpoint():
        try:
            print("\nPLANES COMBOS - PLANES")
            print("Fase de Escucha | FRONT-ENDPOINT ACTIVADO")
            print("COMBO ENDPOINT ACTIVO\n")
            _type = request.args.get('type')
            if _type.upper() == 'COMBO':
                _stype = request.args.get('stype')
                valid_stype = {"PLAN", "PLANVARIANT", "PRODUCTO",
                               "TIPO_SERVICIO", "PRODUCTO_ROUTER"}
                if _stype.upper() in valid_stype:
                    params = {'type': _type,
                              'stype': _stype}
                    if '_V1' in request.args:
                        params['_V1'] = request.args.get('_V1')
                    response = requests.get('http://localhost:5013/api/ra/plnback_endpoint', params=params)
                    return response.text, response.status_code

                elif _stype.upper() == 'PROVINCIA':
                    _V1 = request.args.get('_V1')
                    _V2 = request.args.get('_V2')
                    _V3 = request.args.get('_V3')
                    _V4 = request.args.get('_V4')
                    params = {'type': _type,
                              'stype': _stype,
                              '_V1': _V1,
                              '_V2': _V2,
                              '_V3': _V3,
                              '_V4': _V4}
                    response = requests.get('http://localhost:5013/api/ra/plnback_endpoint', params=params)
                    return response.text, response.status_code

                elif _stype.upper() == 'CIUDAD':
                    _V1 = request.args.get('_V1')
                    _V2 = request.args.get('_V2')
                    _V3 = request.args.get('_V3')
                    _V4 = request.args.get('_V4')
                    _V5 = request.args.get('_V5')
                    params = {'type': _type,
                              'stype': _stype,
                              '_V1': _V1,
                              '_V2': _V2,
                              '_V3': _V3,
                              '_V4': _V4,
                              '_V5': _V5}
                    response = requests.get('http://localhost:5013/api/ra/plnback_endpoint', params=params)
                    return response.text, response.status_code

                elif _stype.upper() == 'SECTOR':
                    _V1 = request.args.get('_V1')
                    _V2 = request.args.get('_V2')
                    _V3 = request.args.get('_V3')
                    _V4 = request.args.get('_V4')
                    _V5 = request.args.get('_V5')
                    _V6 = request.args.get('_V6')
                    params = {'type': _type,
                              'stype': _stype,
                              '_V1': _V1,
                              '_V2': _V2,
                              '_V3': _V3,
                              '_V4': _V4,
                              '_V5': _V5,
                              '_V6': _V6}
                    response = requests.get('http://localhost:5013/api/ra/plnback_endpoint', params=params)
                    return response.text, response.status_code

                else:
                    mensaje = f"El valor de la peticion stype no se encuentra registrada: {_stype}"
                    return jsonify({'error': mensaje}), 400

            elif _type.upper() != 'COMBO' and _type.upper() == 'ALL_DATA':
                mensaje = f"La peticion esta siendo enviada por un canal incorrecto {_type}"
                return jsonify({'error': mensaje}), 400

            else:
                print("plncomb_endpoint - FrontEndpointController | Tipo de Peticion no valido")
                return jsonify({'error': 'Tipo de petición no válido'}), 400
        except Exception as e:
            print("--------------------------------------------------------------------")
            print("combp_endpoint - FrontEndpointController | Error Detectado: ", e)
            print("--------------------------------------------------------------------")
            return jsonify({'Error': e})

    @planp_bp.route(__URL__ + '/planes', methods=['GET'])
    def planp_enpoint():
        try:
            print("\nPLANES - PLANES")
            print("Fase de Escucha | FRONT-ENDPOINT ACTIVADO")
            print("PLANES ENDPOINT ACTIVO\n")
            if request.args.get('type') == 'ALL_DATA':
                stype_valided = {'AD_TARIFFPLAN', 'AD_TARIFFPLANVARIANT', 'AD_TARIFFPLAN_TARIFFPLANVARIANT',
                                 'AD_TARIFFPLANVARIANT_PRODUCTO_ADICIONAL'}
                params = {'type': request.args.get('type')}
                if request.args.get('stype') in stype_valided:
                    params['stype'] = request.args.get('stype')
                    if 'SERVICIO' in request.args:
                        params['_V1'] = request.args.get('SERVICIO')
                        if 'TIPO_SERVICIO' in request.args:
                            params['_V2'] = request.args.get('_V2')
                    response = requests.get('http://localhost:5013/api/ra/plnback_endpoint', params=params)
                    return response.text, response.status_code
                else:
                    mensaje = ("planp_enpoint - FrontEndpointController |"
                               " Segundo Tipo de Pecicion incorrecto")+request.args.get('stype')
                    print(mensaje)
                    return jsonify({'error': mensaje}), 400
            else:
                print("planp_enpoint - FrontEndpointController | Tipo de Peticion no valido")
                return jsonify({'error': 'Tipo de petición no válido: '+request.args.get('type')}), 400

        except Exception as e:
            print("--------------------------------------------------------------------")
            print("planp_enpoint - FrontEndpointController | Error Detectado: ", e)
            print("--------------------------------------------------------------------")
            return jsonify({'Error': e})
