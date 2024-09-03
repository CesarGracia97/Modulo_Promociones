import requests
from flask import Blueprint, jsonify, request

from config.config import config

backp_bp = Blueprint('rapi_backp_GET', __name__)
bpost_bp = Blueprint('rapi_backpost', __name__)
__URL_BKP__ = config.get('URL', 'URL_BACKENDPOINT')


def check_missing_args(data, required_args):
    return [arg for arg in required_args if arg not in data]


# Función para verificar argumentos faltantes en una lista de diccionarios
def check_missing_args_nested(data_dict, required_args):
    missing_args_info = []
    for key, item in data_dict.items():
        missing_args = [arg for arg in required_args if arg not in item]
        if missing_args:
            missing_args_info.append({
                'iteracion': key,
                'faltantes': missing_args
            })
    return missing_args_info


class BackEndpointController:
    def __init__(self):
        self.__URL_Lugares = config.get('URL', 'URL_PLACE', 'URL_BASE')
        self.__Lugares = config.get('LISTAS', 'Lugares')
        self.__URL_Planes = config.get('URL', 'URL_PLANES', 'URL_BASE')
        self.__Planes = config.get('LISTAS', 'Planes')
        self.__URL_Finanzas = config.get('URL', 'URL_FINANCE', 'URL_BASE')
        self.__Finanzas = config.get('LISTAS', 'Finanzas')

    @staticmethod
    def make_request(endpoint, payload):
        try:
            response = requests.get(endpoint, params=payload)
            response.raise_for_status()
            return response.json(), response.status_code
        except requests.exceptions.RequestException as e:
            print("Error en la solicitud:", e)
            return {'error': e}, 500

    @backp_bp.route(__URL_BKP__, methods=["GET", "POST"])
    def back_endpoint():
        controller = BackEndpointController()
        try:
            if request.method == "GET":
                referer = request.headers.get('Referer')
                if referer:
                    if any((controller.__URL_Lugares + ruta) in referer for ruta in controller.__Lugares):
                        print("--------------------------------------------------------------------")
                        print("- BackendPoint: Fase de Escucha ACTIVO GET PLACE - Lugares         -")
                        print("--------------------------------------------------------------------")
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
                                return BackEndpointController.make_request(
                                    'http://localhost:5011/api/ms/peticionPlaces',
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
                                return BackEndpointController.make_request(
                                    'http://localhost:5011/api/ms/peticionPlaces',
                                    payload)

                            elif _type in _sectores and not request.args.get('MASIVE'):
                                if 'id_City' in request.args:
                                    payload['_V1'] = request.args.get('id_City')
                                    if 'TARIFFPLANVARIANT' in request.args:
                                        payload['_V2'] = request.args.get('TARIFFPLANVARIANT')
                                if 'TARIFFPLANVARIANT' in request.args and '_V1' not in payload:
                                    payload['_V1'] = request.args.get('TARIFFPLANVARIANT')
                                return BackEndpointController.make_request(
                                    'http://localhost:5011/api/ms/peticionPlaces',
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
                                return BackEndpointController.make_request(
                                    'http://localhost:5011/api/ms/peticionPlaces',
                                    payload)
                            else:
                                return jsonify({'error': ' BACK ENDPOINT - Tipo de petición no válido'}), 400
                        else:
                            return jsonify({'error': 'BACK ENDPOINT - Tipo no proporcionado'}), 400

                    elif any((controller.__URL_Planes + ruta) in referer for ruta in controller.__Planes):
                        print("--------------------------------------------------------------------")
                        print("- BackendPoint: Fase de Escucha ACTIVO GET PLANS - Planes          -")
                        print("--------------------------------------------------------------------")
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

                    elif any((controller.__URL_Finanzas + ruta) in referer for ruta in controller.__Finanzas):
                        print("--------------------------------------------------------------------")
                        print("- BackendPoint: Fase de Escucha ACTIVO GET FINANCE - Finance       -")
                        print("--------------------------------------------------------------------")
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
                                return BackEndpointController.make_request(
                                    'http://localhost:5011/api/ms/peticionFinance', payload)

                    else:
                        print("La solicitud proviene de una URL desconocida")
                else:
                    print("No se proporcionó el encabezado Referer")
            if request.method == "POST":
                print("--------------------------------------------------------------------")
                print("- BackendPoint: Fase de Escucha ACTIVO POST                        -")
                print("--------------------------------------------------------------------")
                REQUIRED_ARGS = [
                    'Buro', 'Ciudades', 'Dias Gozados', 'Fecha Finalizacion Promocion',
                    'Fecha Inicio Promocion', 'Forma de Pago', 'Nombre Promocion',
                    'Plan_Id', 'Producto_Id', 'Sectores', 'Servicio', 'Variant_Id',
                    'Mes Fin Promocion', 'Mes Inicio Promocion', 'Precio Referencial',
                    'Precio Promocional'
                ]
                REQUIRED_ARGS_ST = [
                    'Paquete', 'Precio Referencial', 'Precio Promocional', 'Mes Inicio', 'Mes Fin'
                ]
                REQUIRED_ARGS_TF = [
                    'Plan', 'Precio Referencial', 'Cantidad', 'Precio Promocional', 'Mes Inicio', 'Mes Fin'
                ]
                REQUIRED_ARGS_TV = [
                    'Plan', 'Precio Referencial', 'Cantidad', 'Precio Promocional', 'Mes Inicio', 'Mes Fin'
                ]
                REQUIRED_ARGS_RT = [
                    'Modelo', 'Precio Referencial', 'Cantidad', 'Precio Promocional', 'Mes Inicio', 'Mes Fin'
                ]
                data = request.json
                missing_args = check_missing_args(data, REQUIRED_ARGS)

                if missing_args:
                    return jsonify({
                        "Error": "Argumentos faltantes",
                        "Faltantes": missing_args
                    }), 400

                additional_errors = {}

                if 'STREAMING' in data:
                    missing_streaming_args = check_missing_args_nested(data['STREAMING'], REQUIRED_ARGS_ST)
                    if missing_streaming_args:
                        additional_errors['STREAMING'] = missing_streaming_args

                if 'TELEFONIA' in data:
                    missing_telefonia_args = check_missing_args(data['TELEFONIA'], REQUIRED_ARGS_TF)
                    if missing_telefonia_args:
                        additional_errors['TELEFONIA'] = missing_telefonia_args

                if 'TELEVISION' in data:
                    missing_television_args = check_missing_args(data['TELEVISION'], REQUIRED_ARGS_TV)
                    if missing_television_args:
                        additional_errors['TELEVISION'] = missing_television_args

                if 'ROUTER' in data:
                    missing_router_args = check_missing_args(data['ROUTER'], REQUIRED_ARGS_RT)
                    if missing_router_args:
                        additional_errors['ROUTER'] = missing_router_args

                if additional_errors:
                    print("Errores encontrados por faltante de Argumentos: ")
                    return jsonify({
                        "Error": "Argumentos faltantes en diccionarios adicionales",
                        "Detalles": additional_errors
                    }), 400

                try:
                    response = requests.post('http://localhost:5011/api/ms/postDatos', json=data)
                    response.raise_for_status()
                    return response.json(), response.status_code
                except requests.exceptions.RequestException as e:
                    print(f"Error al enviar la solicitud a la segunda URL: {e}")
                    return jsonify({'Error': 'Error al enviar la solicitud a la segunda URL'}), 500
        except Exception as e:
            print("--------------------------------------------------------------------")
            print("back_endpoint - back_endpoint | Error Detectado: ", e)
            print("--------------------------------------------------------------------")
            return jsonify({'Error': 'Error interno'}), 500
