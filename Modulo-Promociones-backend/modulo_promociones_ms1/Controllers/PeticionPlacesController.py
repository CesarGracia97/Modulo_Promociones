from flask import Blueprint, jsonify, request
from Repository.PlaceRepository import PlaceRepository
from Services.FormattedPlace import FormattedPlace

receptor_bplc = Blueprint('ms_peticionPlaces', __name__)


class PeticionPlacesController:
    @receptor_bplc.route('/api/ms/peticionPlaces', methods=['GET'])
    def faseEscucha():
        try:
            print("\n*** FASE DE ESCUCHA ACTIVA ***\n")
            frt = FormattedPlace()
            repository = PlaceRepository()
            data = request.json
            _type = data.get('type')
            print(_type)
            if _type is None:
                return jsonify({'error': 'El campo "type" es requerido'}), 400

            if _type.upper() == 'ALL_PROVS':
                _diccionario = {
                    "popcion": "ALL_DATA",
                    "sopcion": 1
                }
                data_prv = repository.getData_Places(_diccionario)
                dt_prv = frt.formated_provinces(data_prv)
                return jsonify(dt_prv), 200

            elif _type.upper() == "ALL_CITIES":
                _diccionario = {
                    "popcion": "ALL_DATA",
                    "sopcion": 2
                }
                data_cts = repository.getData_Places(_diccionario)
                dt_cts = frt.formated_cities(data_cts)
                return jsonify(dt_cts), 200

            elif _type.upper() == "ALL_SECTORS":
                _diccionario = {
                    "popcion": "ALL_DATA",
                    "sopcion": 3
                }
                data_sts = repository.getData_Places(_diccionario)
                dt_sct = frt.formated_sectors(data_sts)
                return jsonify(dt_sct), 200

            elif _type.upper() == "ALL_SUB_SECTORS":
                _diccionario = {
                    "popcion": "ALL_DATA",
                    "sopcion": 4
                }
                data_sst = repository.getData_Places(_diccionario)
                dt_sst = frt.formated_sub_sectors(data_sst)
                return jsonify(dt_sst), 200

            elif _type.upper() == "CITY_SPECIFIC":
                _idProv = data.get('id_Prov')
                _diccionario = {
                    "popcion": "PARAMETRE_DATA",
                    "sopcion": 1,
                    "id_Prov": _idProv
                }
                data_scts = repository.getData_Places(_diccionario)
                dt_scts = frt.formated_specific_city(data_scts)
                return jsonify(dt_scts), 200

            elif _type.upper() == "SECTOR_SPECIFIC":
                _idCity = data.get('id_City')
                _diccionario = {
                    "popcion": "PARAMETRE_DATA",
                    "sopcion": 2,
                    "id_City": _idCity
                }
                data_ssct = repository.getData_Places(_diccionario)
                dt_ssct = frt.formated_specific_sector(data_ssct)
                return jsonify(dt_ssct), 200

            elif _type.upper() == "SUB_SECTOR_SPECIFIC":
                _idSector = data.get('id_Sector')
                _diccionario = {
                    "popcion": "PARAMETRE_DATA",
                    "sopcion": 3,
                    "id_Sector": _idSector
                }
                data_ssst = repository.getData_Places(_diccionario)
                dt_ssst = frt.formated_specific_sub_sector(data_ssst)
                return jsonify(dt_ssst), 200
            else:
                return jsonify({'error': 'El valor del campo "tipo" no es válido'}), 400

        except Exception as e:
            print("--------------------------------------------------------------------")
            print("faseEscucha - PeticionPlacesController | Error detectado: ", e)
            print("--------------------------------------------------------------------")
            return jsonify({'Error': str(e)}), 400
