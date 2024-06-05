from Models.model_place import Provincia, Ciudad, Sector
from Resources.database.connection import connection
from Utils.ReaderJSON import ReaderJSON


class PlaceRepository:
    def __init__(self):
        self.db = connection()
        self.reader_json = ReaderJSON()

    def getData_Places(self, _diccionario: dict) -> dict:
        _ciudades = {"CIUDADES_ESPECIFICASxPROV", "CIUDADES_ESPECIFICASxTFV", "CIUDADES_ESPECIFICASxPROVxTFV",
                     "CIUDADES_ESPECIFICASxPROVxTFV", "CIUDADES_ESPECIFICASxTFVxPROD"}
        _sectores = {"SECTORES_ESPECIFICOSxCITY", "SECTORES_ESPECIFICOSxTFV", "SECTORES_ESPECIFICOSxCITYxTFV",
                     "SECTORES_ESPECIFICOSxCITYxTFVxPROD"}
        try:
            if "popcion" in _diccionario:
                if _diccionario["popcion"] == "ALL_DATA":
                    _Qdiccionario = {"popcion": "Places", "sopcion": _diccionario["popcion"]}
                    if "name_Query" in _diccionario:
                        self.db.connect()
                        _Qdiccionario["name_Query"] = _diccionario["name_Query"]
                        query = self.reader_json.getQuery(_Qdiccionario)
                        results = self.db.execute_query(query)
                        data = {}
                        if results is None:
                            print("--- EL RESULTADO DE LA CONSULTA FUE NULLO ---")
                            return data

                        if _diccionario["name_Query"] == "ALL_PROVS":
                            data['PROVINCIES'] = []
                            for result in results:
                                provincias = Provincia(result[0], result[1])
                                data['PROVINCIES'].append(provincias)
                            print("\n**** PROVINCIAS - DATOS OBTENIDOS ****\n")
                        elif _diccionario["name_Query"] == "ALL_CITIES":
                            data['CITIES'] = []
                            for result in results:
                                ciudades = Ciudad(result[0], result[1], result[2])
                                data['CITIES'].append(ciudades)
                            print("\n**** CIUDADES - DATOS OBTENIDOS ****\n")
                        elif _diccionario["name_Query"] == "ALL_SECTORS":
                            data['SECTORS'] = []
                            for result in results:
                                sectores = Sector(result[0], result[1], result[2])
                                data['SECTORS'].append(sectores)
                            print("\n**** SECTORES - DATOS OBTENIDOS ****\n")
                        self.db.close()
                        return data

                elif _diccionario["popcion"] == "SPECIFIC_DATA":
                    _Qdiccionario = {"popcion": "Places", "sopcion": _diccionario["popcion"]}
                    if "name_Query" in _diccionario:
                        self.db.connect()
                        _Qdiccionario["name_Query"] = _diccionario["name_Query"]
                        _Qdiccionario["_V1"] = _diccionario["_V1"]
                        if "_V2" in _diccionario:
                            _Qdiccionario["_V2"] = _diccionario["_V2"]
                        query = self.reader_json.getQuery(_Qdiccionario)
                        results = self.db.execute_query(query)
                        data = {}
                        if results is None:
                            print("--- EL RESULTADO DE LA CONSULTA FUE NULLO ---")
                            return data

                        if _diccionario["name_Query"] == "PROVINCIAS_ESPECIFICASxTFV":
                            data['PROVINCIES'] = []
                            for result in results:
                                provincias = Provincia(result[0], result[1])
                                data['PROVINCIES'].append(provincias)
                            print("\n**** PROVINCIAS - DATOS OBTENIDOS ****\n")
                        elif _diccionario["name_Query"] in _ciudades:
                            data['CITIESxPROV'] = []
                            for result in results:
                                ciudades = Ciudad(result[0], result[1], result[2])
                                data['CITIESxPROV'].append(ciudades)
                            print("\n**** CIUDADES ESPECIFICAS POR PROVINCIA - DATOS OBTENIDOS ****\n")
                        elif _diccionario["name_Query"] in _sectores:
                            data['SECTORSxCITY'] = []
                            for result in results:
                                sector = Sector(result[0], result[1], result[2])
                                data['SECTORSxCITY'].append(sector)
                            print("\n**** SECTORES ESPECIFICOS POR CIUDAD - DATOS OBTENIDOS ****\n")
                        self.db.close()
                        return data

                elif _diccionario["popcion"] == "MASIVE_DATA":
                    _Qdiccionario = {"popcion": "Places", "sopcion": _diccionario["popcion"]}
                    if "name_Query" in _diccionario:
                        self.db.connect()
                        _Qdiccionario["name_Query"] = _diccionario["name_Query"]
                        for i, city_id in enumerate(_diccionario["_V1"]):
                            key = f"_V1_{i + 1}"  # Nombre único para cada valor de id_Cities
                            _Qdiccionario[key] = city_id
                        _Qdiccionario["_V2"] = _diccionario["_V2"]
                        if '_V3' in _Qdiccionario:
                            _Qdiccionario["_V3"] = _diccionario["_V3"]
                        query = self.reader_json.getQuery(_Qdiccionario)
                        results = self.db.execute_query(query)
                        data = {}
                        if results is None:
                            print("--- EL RESULTADO DE LA CONSULTA FUE NULLO ---")
                            return data

                        if _diccionario["name_Query"] == "CIUDADES_ESPECIFICASxPROVxTFV":
                            data['CITIESxPROV'] = []
                            for result in results:
                                sector = Ciudad(result[0], result[1], result[2])
                                data['CITIESxPROV'].append(sector)
                            print("\n**** CIUDADES ESPECIFICAS POR PROVINCIA TT - DATOS OBTENIDOS ****\n")
                        elif _diccionario["name_Query"] == "SECTORES_ESPECIFICOSxCITYxTFV":
                            data['SECTORSxCITY'] = []
                            for result in results:
                                sector = Sector(result[0], result[1], result[2])
                                data['SECTORSxCITY'].append(sector)
                            print("\n**** SECTORES ESPECIFICOS POR CIUDAD TT - DATOS OBTENIDOS ****\n")
                        self.db.close()
                        return data

                else:
                    print("La clave 'popcion' no está presente en el diccionario _parametro")
                    print("Eso o el valor de 'popcion' no es valida: ", _diccionario["popcion"])
        except Exception as e:
            self.db.close()
            print("--------------------------------------------------------------------")
            print("getData_Places - PlaceRepository | Error: ", e)
            print("--------------------------------------------------------------------")
            return {}
