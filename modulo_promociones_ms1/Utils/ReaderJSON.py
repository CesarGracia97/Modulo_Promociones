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
                            # Caso para SECTMXTT
                            if _nameQuery == "SECTMXTT":
                                _V1_values = [_diccionario[key] for key in _diccionario if key.startswith('_V1_')]
                                _V1 = ', '.join(map(str, _V1_values))
                                _V2 = _diccionario["_V2"]
                                _V3 = _diccionario["_V3"]
                                return (data["Type_Queries"][_popcion][_sopcion]
                                        .get(_nameQuery, f"Consulta no encontrada en {_popcion}, {_sopcion}").replace
                                        ("_V1", _V1).replace("_V2", str(_V2)).replace("_V3", str(_V3)))

                            # Caso general para consultas que empiezan con "SPECIFIC_"
                            elif _nameQuery.startswith("SPECIFIC_"):
                                if "id" in _diccionario:
                                    # Caso donde existe el argumento "id"
                                    _parametro = _diccionario["id"]
                                    return (data["Type_Queries"][_popcion][_sopcion]
                                            .get(_nameQuery, f"Consulta no encontrada en {_popcion}, {_sopcion}")
                                            .replace("_V1", str(_parametro)))
                                else:
                                    # Preparación de parámetros comunes
                                    _V1 = _diccionario["_V1"]
                                    _V2 = _diccionario["_V2"]
                                    if "_V3" in _diccionario:
                                        # Caso donde existe el argumento "_V3"
                                        _V3 = _diccionario["_V3"]
                                        return (data["Type_Queries"][_popcion][_sopcion]
                                                .get(_nameQuery, f"Consulta no encontrada en {_popcion}, {_sopcion}")
                                                .replace("_V1", str(_V1)).replace("_V2", str(_V2)).replace("_V3",
                                                                                                           str(_V3)))
                                    else:
                                        # Retorno sin "_V3"
                                        return (data["Type_Queries"][_popcion][_sopcion]
                                                .get(_nameQuery, f"Consulta no encontrada en {_popcion}, {_sopcion}")
                                                .replace("_V1", str(_V1)).replace("_V2", str(_V2)))
                            else:
                                # Agregar manejo para otras posibles consultas o un error
                                raise ValueError(f"Consulta {_nameQuery} no es reconocida.")

                if _popcion == "Planes":
                    if "sopcion" in _diccionario:
                        _sopcion = _diccionario["sopcion"]
                        if _sopcion == "ALL_DATA":
                            if "topcion" in _diccionario:
                                _topcion = _diccionario["topcion"]
                                valid_topcions = {"OFER", "SERV", "TECN", "TISE"}
                                if _topcion in valid_topcions:
                                    _nameQuery = _diccionario["name_Query"]
                                    return (data["Type_Queries"][_popcion][_sopcion][_topcion]
                                            .get(_nameQuery,
                                                 f"Consulta no encontrada en {_popcion},{_sopcion},{_topcion}"))

                                elif _topcion == "PLAN":
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
                                else:
                                    raise ValueError(f"Valor de _topcion '{_topcion}' no es válido.")

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
                if _popcion == "Finance":
                    if "sopcion" in _diccionario:
                        _sopcion = _diccionario["sopcion"]
                        if _sopcion in data["Type_Queries"][_popcion]:  # Verificar si _sopcion es una clave válida
                            _nameQuery = _diccionario["name_Query"]
                            return data["Type_Queries"][_popcion].get(_nameQuery,
                                                                                f"Consulta no encontrada en "
                                                                                f"{_popcion}, {_sopcion}")
                        else:
                            return f"{_sopcion} no es una opción válida en {data['Type_Queries'][_popcion]}"

        except Exception as e:
            print("----------------------------------------------")
            print("getQuery - ReaderJSON | Error Detectado:", e)
            print("----------------------------------------------")
