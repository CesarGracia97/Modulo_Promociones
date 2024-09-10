from flask import Blueprint, jsonify, request
from Repository.PlaceRepository import PlaceRepository
from Services.FormattedPlace import FormattedPlace

receptor_bplc = Blueprint('ms_peticionPlaces', __name__)


class PeticionPlacesController:
    @receptor_bplc.route('/api/ms/peticionPlaces', methods=['GET'])
    def faseEscucha():
        _valid_type_AD = {"ALL_PROV", "ALL_CITIES", "ALL_SECTORS"}
        _valid_type_SD = {"CIUDADES_ESPECIFICASxPROV", "SECTORES_ESPECIFICOSxCITY", "PROVINCIAS_ESPECIFICASxTFV",
                          "CIUDADES_ESPECIFICASxTFV", "SECTORES_ESPECIFICOSxTFV", "CIUDADES_ESPECIFICASxPROVxTFV",
                          "CIUDADES_ESPECIFICASxTFVxPROD", "SECTORES_ESPECIFICOSxCITYxTFV"}
        _valid_type_MD = {"CIUDADES_M_ESPECIFICASxPROVxTFV", "SECTORES_M_ESPECIFICOSxCITYxTFV",
                          "SECTORES_M_ESPECIFICOSxCITYxTFVxPROD"}
        try:
            print("\n*** FASE DE ESCUCHA ACTIVA ***\n")
            frt = FormattedPlace()
            repository = PlaceRepository()
            _type = request.args.get('type')
            if _type is None:
                return jsonify({'error': 'El campo "type" es requerido'}), 400

            if _type in _valid_type_AD:
                _diccionario = {"popcion": "ALL_DATA", "name_Query": _type}
                data = repository.getData_Places(_diccionario)
                dt = frt.formated_placeSIMPLEDATA(data, _type)
                return jsonify(dt), 200

            if _type in _valid_type_SD and not request.args.get('MASIVE'):
                _diccionario = {"popcion": "SPECIFIC_DATA", "name_Query": _type, "_V1": request.args.get('_V1')}
                if '_V2' in request.args:
                    _diccionario["_V2"] = request.args.get('_V2')
                data = repository.getData_Places(_diccionario)
                dt = frt.formated_placeMIXDATA(data, _type)
                return jsonify(dt), 200

            if _type in _valid_type_MD and request.args.get('MASIVE') == "YES":
                _diccionario = {"popcion": "MASIVE_DATA", "name_Query": _type}
                if 'id_Provs' in request.args:
                    _V1 = request.args.get('id_Provs')
                    if _V1:
                        _V1 = _V1.split(',')
                    _diccionario['_V1'] = _V1
                if 'id_Cities' in request.args:
                    _V1 = request.args.get('id_Cities')
                    if _V1:
                        _V1 = _V1.split(',')
                    _diccionario['_V1'] = _V1
                    if '_V2' in request.args:
                        _diccionario['_V2'] = request.args.get('_V2')
                    if '_V3' in request.args:
                        _diccionario['_V3'] = request.args.get('_V3')
                data = repository.getData_Places(_diccionario)
                dt = frt.formated_placeMIXDATA(data, _type)
                return jsonify(dt), 200

            else:
                return jsonify({'error': 'El valor del campo "tipo" no es válido'}), 400

        except Exception as e:
            print("--------------------------------------------------------------------")
            print("faseEscucha - PeticionPlacesController | Error detectado: ", e)
            print("--------------------------------------------------------------------")
            return jsonify({'Error': str(e)}), 400
