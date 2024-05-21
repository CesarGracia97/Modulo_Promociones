import json
import os


class ReaderJSON:
    def __init__(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self._PATH = os.path.join(current_dir, "..", "Utils", "JSON", "Query.json")

    def getQuery(self, _diccionario: dict):
        _type = ""
        try:
            if "popcion" in _diccionario:
                _popcion = _diccionario["popcion"]
                with open(self._PATH, 'r') as file:
                    data = json.load(file)
                if _popcion == "Places":
                    if "sopcion" in _diccionario:
                        _sopcion = _diccionario["sopcion"]
                        if _sopcion == "ALL_DATA":
                            _type = _nameQuery = _diccionario["name_Query"]
                            return (data["Type_Queries"][_popcion][_sopcion]
                                    .get(_nameQuery, f"Consulta no encontrada en {_popcion}, {_sopcion}"))
                        if _sopcion == "SPECIFIC_DATA":
                            _type = _nameQuery = _diccionario["name_Query"]
                            _V1 = _diccionario["_V1"]
                            if "_V2" in _diccionario:
                                _V2 = _diccionario["_V2"]
                                return (data["Type_Queries"][_popcion][_sopcion]
                                        .get(_nameQuery, f"Consulta no encontrada en {_popcion}, {_sopcion}").replace
                                        ("_V1", _V1).replace("_V2", str(_V2)))
                            return (data["Type_Queries"][_popcion][_sopcion]
                                    .get(_nameQuery, f"Consulta no encontrada en {_popcion}, {_sopcion}")
                                    .replace("_V1", str(_V1)))
                        if _sopcion == "MASIVE_DATA":
                            _type = _nameQuery = _diccionario["name_Query"]
                            _V1_values = [_diccionario[key] for key in _diccionario if key.startswith('_V1_')]
                            _V1 = ', '.join(map(str, _V1_values))
                            _V2 = _diccionario["_V2"]
                            return (data["Type_Queries"][_popcion][_sopcion]
                                    .get(_nameQuery, f"Consulta no encontrada en {_popcion}, {_sopcion}").replace
                                    ("_V1", _V1).replace("_V2", str(_V2)))
                if _popcion == "Planes":
                    if "sopcion" in _diccionario:
                        _type = _sopcion = _diccionario["sopcion"]
                        if _sopcion == "ALL_DATA":
                            if "topcion" in _diccionario:
                                _topcion = _diccionario["topcion"]
                                valid_topcions = {'OFER', 'SERV', 'TECN', 'TISE', 'AD_TARIFFPLAN',
                                                  'AD_TARIFFPLANVARIANT', 'AD_TARIFFPLANVARIANT',
                                                  'AD_TARIFFPLAN_TARIFFPLANVARIANT',
                                                  'AD_TARIFFPLANVARIANT_PRODUCTO_ADICIONAL'}
                                if _diccionario["topcion"] in valid_topcions:
                                    if 'name_Query' in _diccionario:
                                        _nameQuery = _diccionario["name_Query"]
                                        return (data["Type_Queries"][_popcion][_sopcion][_topcion]
                                                .get(_nameQuery,
                                                f"Consulta no encontrada en {_popcion},{_sopcion},{_topcion}"))
                                    if 'name_Query' not in _diccionario:
                                        _nameQuery = _diccionario["topcion"]
                                        if '_V1' in _diccionario:
                                            _V1 = _diccionario["_V1"]
                                            if '_V2' in _diccionario:
                                                _V2 = _diccionario["_V2"]
                                                return (data["Type_Queries"][_popcion][_sopcion][_topcion]
                                                        .get(_nameQuery,
                                                             f"Consulta no encontrada en {_popcion},{_sopcion},{_topcion}")
                                                        .replace("_V1", str(_V1))
                                                        .replace("_V2", str(_V2)))
                                            return (data["Type_Queries"][_popcion][_sopcion][_topcion]
                                                    .get(_nameQuery,
                                                         f"Consulta no encontrada en {_popcion},{_sopcion},{_topcion}")
                                                    .replace("_V1", str(_V1)))
                                        return (data["Type_Queries"][_popcion][_sopcion][_topcion]
                                                .get(_nameQuery, f"Consulta no encontrada en {_popcion},{_sopcion},{_topcion}"))
                                else:
                                    raise ValueError(f"Valor de _topcion '{_topcion}' no es válido.")

                        if _sopcion == "COMBO":
                            if "name_Query" in _diccionario:
                                valid_topcions = {"COMBO_PLAN", "COMBO_PLANVARIANT", "COMBO_PRODUCTO",
                                                  "COMBO_TIPO_SERVICIO"}
                                _type = _nameQuery = _diccionario["name_Query"]
                                if _nameQuery in valid_topcions:
                                    _nameQuery = _diccionario["name_Query"]
                                    _V1 = _diccionario["_V1"]
                                    if _V1 is not None:
                                        return (data["Type_Queries"][_popcion][_sopcion]
                                                .get(_nameQuery, f"Consulta no encontrada en {_popcion}, {_sopcion}")
                                                .replace("_V1", str(_V1)))
                                    else:
                                        raise ValueError("Se requiere un parámetro para esta consulta específica.")
                if _popcion == "Finance":
                    if 'name_Query' in _diccionario:
                        _type = _nameQuery = _diccionario["name_Query"]
                        if "_V1" in _diccionario:
                            _V1 = _diccionario["_V1"]
                            if "_V2" in _diccionario:
                                _V2 = _diccionario["_V2"]
                                return (data["Type_Queries"][_popcion]
                                        .get(_nameQuery, f"Consulta no encontrada en "f"{_popcion}")
                                        .replace("_V1", str(_V1)).replace("_V2", str(_V2)))

                            return (data["Type_Queries"][_popcion]
                                    .get(_nameQuery, f"Consulta no encontrada en "f"{_popcion}")
                                    .replace("_V1", str(_V1)))

                        return (data["Type_Queries"][_popcion]
                                .get(_nameQuery, f"Consulta no encontrada en " f"{_popcion}"))
        except Exception as e:
            print("----------------------------------------------")
            print("getQuery - ReaderJSON | "+_type)
            print("Error Detectado:", e)
            print("----------------------------------------------")
