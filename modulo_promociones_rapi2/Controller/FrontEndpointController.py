from flask import Blueprint, request, jsonify
import requests

combp_bp = Blueprint('rapi_combp_GET', __name__)
oferp_bp = Blueprint('rapi_oferp_GET', __name__)
servp_bp = Blueprint('rapi_servp_GET', __name__)
tecnp_bp = Blueprint('rapi_tecnp_GET', __name__)
tisep_bp = Blueprint('rapi_tisep_GET', __name__)
planp_bp = Blueprint('rapi_planp_GET', __name__)


class FrontEndpointController:

    @combp_bp.route('/api/ra/plncomb_endpoint', methods=['GET'])
    def combp_endpoint():
        try:
            print("\nPLANS - PLANES")
            print("Fase de Escucha | FRONT-ENDPOINT ACTIVADO")
            print("COMBO ENDPOINT ACTIVO\n")
            _type = request.args.get('type')
            if _type.upper() == 'COMBO':
                _stype = request.args.get('stype')
                if _stype.upper() == 'TIPO_SERVICIOS':
                    _V1 = request.args.get('_V1')
                    params = {'type': _type,
                              'stype': _stype,
                              '_V1': _V1}
                    response = requests.get('http://localhost:5013/api/ra/plnback_endpoint', params=params)
                    return response.text, response.status_code

                elif _stype.upper() == 'RED_TECNOLOGIA':
                    _V1 = request.args.get('_V1')
                    _V2 = request.args.get('_V2')
                    params = {'type': _type,
                              'stype': _stype,
                              '_V1': _V1,
                              '_V2': _V2}
                    response = requests.get('http://localhost:5013/api/ra/plnback_endpoint', params=params)
                    return response.text, response.status_code

                elif _stype.upper() == 'PLANES':
                    _V1 = request.args.get('_V1')
                    _V2 = request.args.get('_V2')
                    _V3 = request.args.get('_V3')
                    params = {'type': _type,
                              'stype': _stype,
                              '_V1': _V1,
                              '_V2': _V2,
                              '_V3': _V3}
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
                print("prov_endpoint - FrontEndpointController | Tipo de Peticion no valido")
                return jsonify({'error': 'Tipo de petición no válido'}), 400
        except Exception as e:
            print("--------------------------------------------------------------------")
            print("combp_endpoint - FrontEndpointController | Error Detectado: ", e)
            print("--------------------------------------------------------------------")
            return jsonify({'Error': e})

    @oferp_bp.route('/api/ra/plnofer_endpoint', methods=['GET'])
    def oferp_enpoint():
        try:

            print("\nOFERTAS - PLANES")
            print("Fase de Escucha | ENDPOINT - F ACTIVADO")
            print("OFERTAS ENDPOINT ACTIVO\n")
            _type = request.args.get('type')
            if _type.upper() == 'ALL_DATA':
                _stype = request.args.get('stype')
                if _stype.upper() == 'OFER':
                    params = {
                        'type': _type,
                        'stype': _stype,
                        'ttype': 1
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

    @servp_bp.route('/api/ra/plnserv_endpoint', methods=['GET'])
    def servp_enpoint():
        try:
            print("\nSERVICIOS - PLANES")
            print("Fase de Escucha | FRONT-ENDPOINT - F ACTIVADO")
            print("SERVICIOS ENDPOINT ACTIVO\n")
            _type = request.args.get('type')
            if _type.upper() == 'ALL_DATA':
                _stype = request.args.get('stype')
                if _stype.upper() == 'SERV':
                    params = {
                        'type': _type,
                        'stype': _stype,
                        'ttype': 1
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

    @tecnp_bp.route('/api/ra/plntecn_endpoint', methods=['GET'])
    def tecnp_enpoint():
        try:
            print("\nTECNOLOGIAS - PLANES")
            print("Fase de Escucha | ENDPOINT - F ACTIVADO")
            print("TECNOLOGIAS ENDPOINT ACTIVO\n")
            _type = request.args.get('type')
            if _type.upper() == 'ALL_DATA':
                _stype = request.args.get('stype')
                if _stype.upper() == 'TECN':
                    params = {
                        'type': _type,
                        'stype': _stype,
                        'ttype': 1
                    }
                    response = requests.get('http://localhost:5013/api/ra/plnback_endpoint', params=params)
                    return response.text, response.status_code

                elif _stype.upper() != 'TECN' and (
                        _stype.upper() == 'OFER' or _stype.upper() == 'TISE' or _stype.upper() == 'SERV' or _stype.upper() == 'PLAN'):
                    mensaje = f"La peticion esta siendo enviada por un canal incorrecto {_stype}"
                    return jsonify({'error': mensaje}), 400

            elif _type.upper() != 'ALL_DATA' and _type.upper() == 'COMBO':
                mensaje = f"La peticion esta siendo enviada por un canal incorrecto {_type}"
                return jsonify({'error': mensaje}), 400

            else:
                print("tecnp_enpoint - FrontEndpointController | Tipo de Peticion no valido")
                return jsonify({'error': 'Tipo de petición no válido'}), 400

        except Exception as e:
            print("--------------------------------------------------------------------")
            print("tecnp_enpoint - FrontEndpointController | Error Detectado: ", e)
            print("--------------------------------------------------------------------")
            return jsonify({'Error': e})

    @tisep_bp.route('/api/ra/plntise_endpoint', methods=['GET'])
    def tisep_enpoint():
        try:
            print("\nTIPO DE SERVICIOS - PLANES")
            print("Fase de Escucha | ENDPOINT - F ACTIVADO")
            print("TIPO DE SERVICIOS ENDPOINT ACTIVO\n")
            _type = request.args.get('type')
            if _type.upper() == 'ALL_DATA':
                _stype = request.args.get('stype')
                if _stype.upper() == 'TISE':
                    params = {
                        'type': _type,
                        'stype': _stype,
                        'ttype': 1
                    }
                    response = requests.get('http://localhost:5013/api/ra/plnback_endpoint', params=params)
                    return response.text, response.status_code

                elif _stype.upper() != 'TISE' and (
                        _stype.upper() == 'OFER' or _stype.upper() == 'TECN' or _stype.upper() == 'SERV' or _stype.upper() == 'PLAN'):
                    mensaje = f"La peticion esta siendo enviada por un canal incorrecto {_stype}"
                    return jsonify({'error': mensaje}), 400

            elif _type.upper() != 'ALL_DATA' and _type.upper() == 'COMBO':
                mensaje = f"La peticion esta siendo enviada por un canal incorrecto {_type}"
                return jsonify({'error': mensaje}), 400

            else:
                print("tisep_enpoint - FrontEndpointController | Tipo de Peticion no valido")
                return jsonify({'error': 'Tipo de petición no válido'}), 400

        except Exception as e:
            print("--------------------------------------------------------------------")
            print("tisep_enpoint - FrontEndpointController | Error Detectado: ", e)
            print("--------------------------------------------------------------------")
            return jsonify({'Error': e})

    @planp_bp.route('/api/ra/plnplan_endpoint', methods=['GET'])
    def planp_enpoint():
        try:
            print("\nPLANES - PLANES")
            print("Fase de Escucha | ENDPOINT - F ACTIVADO")
            print("PLANES ENDPOINT ACTIVO\n")
            _type = request.args.get('type')
            if _type.upper() == 'ALL_DATA':
                _stype = request.args.get('stype')
                if _stype.upper() == 'PLAN':
                    _ttype = request.args.get('ttype')
                    if _ttype == 1 or _ttype == '1':
                        params = {
                            'type': _type,
                            'stype': _stype,
                            'ttype': _ttype
                        }
                        response = requests.get('http://localhost:5013/api/ra/plnback_endpoint', params=params)
                        return response.text, response.status_code

                    if _ttype == 2 or _ttype == '2':
                        params = {
                            'type': _type,
                            'stype': _stype,
                            'ttype': _ttype
                        }
                        response = requests.get('http://localhost:5013/api/ra/plnback_endpoint', params=params)
                        return response.text, response.status_code

                    if _ttype == 3 or _ttype == '1':
                        params = {
                            'type': _type,
                            'stype': _stype,
                            'ttype': _ttype
                        }
                        response = requests.get('http://localhost:5013/api/ra/plnback_endpoint', params=params)
                        return response.text, response.status_code
                elif _stype.upper() != 'PLAN' and (
                        _stype.upper() == 'OFER' or _stype.upper() == 'TECN' or _stype.upper() == 'SERV' or _stype.upper() == 'TISE'):
                    mensaje = f"La peticion esta siendo enviada por un canal incorrecto {_stype}"
                    return jsonify({'error': mensaje}), 400

            elif _type.upper() != 'ALL_DATA' and _type.upper() == 'COMBO':
                mensaje = f"La peticion esta siendo enviada por un canal incorrecto {_type}"
                return jsonify({'error': mensaje}), 400

            else:
                print("planp_enpoint - FrontEndpointController | Tipo de Peticion no valido")
                return jsonify({'error': 'Tipo de petición no válido'}), 400

        except Exception as e:
            print("--------------------------------------------------------------------")
            print("planp_enpoint - FrontEndpointController | Error Detectado: ", e)
            print("--------------------------------------------------------------------")
            return jsonify({'Error': e})
