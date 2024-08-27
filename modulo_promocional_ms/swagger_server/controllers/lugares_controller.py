import connexion
from flask import jsonify
from swagger_server.models.request_get_lugares import RequestGetLugares  # noqa: E501
from swagger_server.repository.lugares_Repository import lugares_Repository
from swagger_server.uses_cases.FormattedPlace import FormattedPlace


def get_lugares(body=None):  # noqa: E501
    """ get_lugares Consulta de Datos de Provincias segun sus parametros. # noqa: E501 """
    _type = None
    try:
        if connexion.request.is_json:
            _valid_type_AD = {"ALL_PROV", "ALL_CITIES", "ALL_SECTORS"}
            _valid_type_SD = {"CIUDADES_ESPECIFICASxPROV", "SECTORES_ESPECIFICOSxCITY", "PROVINCIAS_ESPECIFICASxTFV",
                              "CIUDADES_ESPECIFICASxTFV", "SECTORES_ESPECIFICOSxTFV", "CIUDADES_ESPECIFICASxPROVxTFV",
                              "CIUDADES_ESPECIFICASxTFVxPROD", "SECTORES_ESPECIFICOSxCITYxTFV"}
            _valid_type_MD = {"CIUDADES_M_ESPECIFICASxPROVxTFV", "SECTORES_M_ESPECIFICOSxCITYxTFV",
                              "SECTORES_M_ESPECIFICOSxCITYxTFVxPROD"}
            body = RequestGetLugares.from_dict(connexion.request.get_json())
            if body.channel == 'api-modulos-promocionales-lugares':
                print("*** FASE DE ESCUCHA ACTIVA ***")
                print(body.type)
                _type = body.type
                repository = lugares_Repository()
                frt = FormattedPlace()
                if body.type in _valid_type_AD:
                    _diccionario = {"popcion": "ALL_DATA", "name_Query": body.type}
                    data = repository.getData_Places(_diccionario)
                    dt = frt.formated_placeSIMPLEDATA(data, body.type)
                    return jsonify(dt), 200
                if body.type in _valid_type_SD:
                    _diccionario = {"popcion": "SPECIFIC_DATA", "name_Query": _type, "_V1": body.v1}
                    if body.v2 is not None:
                        _diccionario["_V2"] = body.v2
                    data = repository.getData_Places(_diccionario)
                    dt = frt.formated_placeMIXDATA(data, _type)
                    return jsonify(dt), 200
                if body.type in _valid_type_MD:
                    _diccionario = {"popcion": "MASIVE_DATA", "name_Query": _type}
                    if body.id_provs is not None:
                        _diccionario['_V1'] = body.id_provs
                    if body.id_cities is not None:
                        _diccionario['_V1'] = body.id_cities
                        if body.v2 is not None:
                            _diccionario['_V2'] = body.v2
                        if body.v3 is not None:
                            _diccionario['_V3'] = body.v3
                    data = repository.getData_Places(_diccionario)
                    dt = frt.formated_placeMIXDATA(data, _type)
                    return jsonify(dt), 200

    except Exception as e:
        print("--------------------------------------------------------------------")
        print("faseEscucha - planes_Controller | Error detectado")
        print("Tipo de Peticion: ", _type)
        print("Error: ", e)
        print("--------------------------------------------------------------------")
        error_respuesta = {
            'errorCode': -1,
            'message': e,
            'externalTransactionId': 0,
            'internalTransactionId': 0
        }
        return jsonify(error_respuesta), 400
