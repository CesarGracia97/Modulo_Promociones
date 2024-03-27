import json
import os


class ReaderJSON:
    def __init__(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self._PATH = os.path.join(current_dir, "..", "Utils", "JSON", "Query.json")

    def getQuery(self, _diccionario: dict):
        try:
            if "popcion" in _diccionario:
                _popcion = _diccionario["popcion"]
                with open(self._PATH, 'r') as file:
                    data = json.load(file)
                if _popcion == "Places":
                    if "sopcion" in _diccionario:
                        _sopcion = _diccionario["sopcion"]
                        if _sopcion == "ALL_DATA":
                            _nameQuery = _diccionario["name_Query"]
                            return data["Type_Queries"][_popcion][_sopcion].get(_nameQuery,
                                                                                f"Consulta no encontrada en "
                                                                                f"{_popcion}, {_sopcion}")
                        if _sopcion == "PARAMETRE_DATA":
                            _nameQuery = _diccionario["name_Query"]
                            _parametro = _diccionario["id"]
                            if _nameQuery.startswith("SPECIFIC_") and _parametro is None:
                                raise ValueError("Se requiere un parámetro para esta consulta específica.")
                            if _nameQuery.startswith("SPECIFIC_"):
                                return data["Type_Queries"][_popcion][_sopcion].get(_nameQuery,
                                                                                    f"Consulta no encontrada en "
                                                                                    f"{_popcion}, {_sopcion}").replace(
                                    "?", str(_parametro))
                if _popcion == "Planes":
                    if "sopcion" in _diccionario:
                        _sopcion = _diccionario["sopcion"]
                        if _sopcion == "ALL_DATA":
                            if "topcion" in _diccionario:
                                _topcion = _diccionario["topcion"]
                                if _topcion == "OFER":
                                    _nameQuery = _diccionario["name_Query"]
                                    return (data["Type_Queries"][_popcion][_sopcion][_topcion]
                                            .get(_nameQuery,
                                                 f"Consulta no encontrada en {_popcion},{_sopcion},{_topcion}"))
                                if _topcion == "SERV":
                                    _nameQuery = _diccionario["name_Query"]
                                    return (data["Type_Queries"][_popcion][_sopcion][_topcion]
                                            .get(_nameQuery,
                                                 f"Consulta no encontrada en {_popcion},{_sopcion},{_topcion}"))
                                if _topcion == "TECN":
                                    _nameQuery = _diccionario["name_Query"]
                                    return (data["Type_Queries"][_popcion][_sopcion][_topcion]
                                            .get(_nameQuery,
                                                 f"Consulta no encontrada en {_popcion},{_sopcion},{_topcion}"))
                                if _topcion == "TISE":
                                    _nameQuery = _diccionario["name_Query"]
                                    return (data["Type_Queries"][_popcion][_sopcion][_topcion]
                                            .get(_nameQuery,
                                                 f"Consulta no encontrada en {_popcion},{_sopcion},{_topcion}"))
                                if _topcion == "PLAN":
                                    _nameQuery = _diccionario["name_Query"]
                                    if _nameQuery == 'AD_TARIFFPLANVARIANT':
                                        _V1 = _diccionario["_V1"]
                                        _V2 = _diccionario["_V2"]
                                        _V3 = _diccionario["_V3"]
                                        if _V1 and _V2 and _V3 is not None:
                                            return (data["Type_Queries"][_popcion][_sopcion][_topcion]
                                                    .get(_nameQuery,
                                                         f"Consulta no encontrada en {_popcion},{_sopcion},{_topcion}")
                                                    .replace("_V1", str(_V1))
                                                    .replace("_V2", str(_V2))
                                                    .replace("_V3", str(_V3)))
                                        else:
                                            return (data["Type_Queries"][_popcion][_sopcion][_topcion]
                                                    .get(_nameQuery,
                                                         f"Consulta no encontrada en {_popcion},{_sopcion},{_topcion}"))
                        if _sopcion == "COMBO":
                            if "name_Query" in _diccionario:
                                _nameQuery = _diccionario["name_Query"]
                                if _nameQuery == "COMBO_TIPO_SERVICIOS":
                                    _nameQuery = _diccionario["name_Query"]
                                    _V1 = _diccionario["_V1"]
                                    if _V1 is not None:
                                        return (data["Type_Queries"][_popcion][_sopcion]
                                                .get(_nameQuery, f"Consulta no encontrada en {_popcion}, {_sopcion}")
                                                .replace("_V1", str(_V1)))
                                    else:
                                        raise ValueError("Se requiere un parámetro para esta consulta específica.")

                                if _nameQuery == "COMBO_RED_TECNOLOGIA":
                                    _nameQuery = _diccionario["name_Query"]
                                    _V1 = _diccionario["_V1"]
                                    _V2 = _diccionario["_V2"]
                                    if _V1 and _V2 is not None:
                                        return (data["Type_Queries"][_popcion][_sopcion]
                                                .get(_nameQuery,f"Consulta no encontrada en {_popcion}, {_sopcion}")
                                                .replace("_V1", str(_V1))
                                                .replace("_V2", str(_V2)))
                                    else:
                                        raise ValueError(
                                            "Se requieren todos los parametros para esta consulta específica.")
                                if _nameQuery == "COMBO_PLANES":
                                    _nameQuery = _diccionario["name_Query"]
                                    _V1 = _diccionario["_V1"]
                                    _V2 = _diccionario["_V2"]
                                    _V3 = _diccionario["_V3"]
                                    if _V1 and _V2 and _V3 is not None:
                                        return (data["Type_Queries"][_popcion][_sopcion]
                                                .get(_nameQuery, f"Consulta no encontrada en {_popcion}, {_sopcion}")
                                                .replace("_V1", str(_V1))
                                                .replace("_V2", str(_V2))
                                                .replace("_V3",str(_V3)))
                                    else:
                                        raise ValueError(
                                            "Se requieren todos los parametros para esta consulta específica.")
                                if _nameQuery == "COMBO_PROVINCIA":
                                    _nameQuery = _diccionario["name_Query"]
                                    _V1 = _diccionario["_V1"]
                                    _V2 = _diccionario["_V2"]
                                    _V3 = _diccionario["_V3"]
                                    _V4 = _diccionario["_V4"]
                                    if _V1 and _V2 and _V3 and _V4 is not None:
                                        return (data["Type_Queries"][_popcion][_sopcion]
                                                .get(_nameQuery,f"Consulta no encontrada en {_popcion}, {_sopcion}")
                                                .replace("_V1", str(_V1))
                                                .replace("_V2", str(_V2))
                                                .replace("_V3", str(_V3))
                                                .replace("_V4", str(_V4)))
                                    else:
                                        raise ValueError(
                                            "Se requieren todos los parametros para esta consulta específica.")
                                if _nameQuery == "COMBO_CIUDAD":
                                    _nameQuery = _diccionario["name_Query"]
                                    _V1 = _diccionario["_V1"]
                                    _V2 = _diccionario["_V2"]
                                    _V3 = _diccionario["_V3"]
                                    _V4 = _diccionario["_V4"]
                                    _V5 = _diccionario["_V5"]
                                    if _V1 and _V2 and _V3 and _V4 and _V5 is not None:
                                        return (data["Type_Queries"][_popcion][_sopcion]
                                                .get(_nameQuery,f"Consulta no encontrada en {_popcion}, {_sopcion}")
                                                .replace("_V1", str(_V1))
                                                .replace("_V2", str(_V2))
                                                .replace("_V3", str(_V3))
                                                .replace("_V4", str(_V4))
                                                .replace("_V5", str(_V5)))
                                    else:
                                        raise ValueError(
                                            "Se requieren todos los parametros para esta consulta específica.")
                                if _nameQuery == "COMBO_SECTOR":
                                    _nameQuery = _diccionario["name_Query"]
                                    _V1 = _diccionario["_V1"]
                                    _V2 = _diccionario["_V2"]
                                    _V3 = _diccionario["_V3"]
                                    _V4 = _diccionario["_V4"]
                                    _V5 = _diccionario["_V5"]
                                    _V6 = _diccionario["_V6"]
                                    if _V1 and _V2 and _V3 and _V4 and _V5 and _V6 is not None:
                                        return (data["Type_Queries"][_popcion][_sopcion]
                                                .get(_nameQuery, f"Consulta no encontrada en {_popcion}, {_sopcion}")
                                                .replace("_V1", str(_V1))
                                                .replace("_V2", str(_V2))
                                                .replace("_V3", str(_V3))
                                                .replace("_V4", str(_V4))
                                                .replace("_V5", str(_V5))
                                                .replace("_V6", str(_V6)))
                                    else:
                                        raise ValueError(
                                            "Se requieren todos los parametros para esta consulta específica.")
        except Exception as e:
            print("----------------------------------------------")
            print("getQuery - ReaderJSON | Error Detectado:", e)
            print("----------------------------------------------")
