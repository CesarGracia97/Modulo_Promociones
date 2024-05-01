from Models.model_place import Provincia, Ciudad, Sector, Subsector, CiudadxProvincia, SectorxCiudad, SubsectorxSector
from Resources.database.connection import connection
from Utils.ReaderJSON import ReaderJSON


class PlaceRepository:
    def __init__(self):
        self.db = connection()
        self.reader_json = ReaderJSON()

    def getData_Places(self, _diccionario: dict) -> dict:
        try:
            if "popcion" in _diccionario:
                _popcion = _diccionario["popcion"]
                self.db.connect()
                if _popcion == "ALL_DATA":
                    if "sopcion" in _diccionario:
                        _sopcion = _diccionario["sopcion"]
                        _Qdiccionario = {
                            "popcion": "Places",
                            "sopcion": "ALL_DATA"
                        }
                        if _sopcion == 1:
                            _Qdiccionario["name_Query"] = "ONLY_PROV"
                            query = self.reader_json.getQuery(_Qdiccionario)
                            results = self.db.execute_query(query)
                            if results is None:
                                return {}
                            data = {
                                'PROVINCIES': []
                            }
                            for result in results:
                                provincia = Provincia(result[0], result[1])
                                data['PROVINCIES'].append(provincia)
                            print("\n**** PROVINCIAS - DATOS OBTENIDOS ****\n")
                            self.db.close()
                            return data
                        if _sopcion == 2:
                            _Qdiccionario["name_Query"] = "ONLY_CITIES"
                            query = self.reader_json.getQuery(_Qdiccionario)
                            results = self.db.execute_query(query)
                            if results is None:
                                return {}
                            data = {
                                'CITIES': []
                            }
                            for result in results:
                                ciudades = Ciudad(result[0], result[1], result[2])
                                data['CITIES'].append(ciudades)
                            print("\n**** CIUDADES - DATOS OBTENIDOS ****\n")
                            self.db.close()
                            return data
                        if _sopcion == 3:
                            _Qdiccionario["name_Query"] = "ONLY_SECTORS"
                            query = self.reader_json.getQuery(_Qdiccionario)
                            results = self.db.execute_query(query)
                            if results is None:
                                return {}
                            data = {
                                'SECTORS': []
                            }
                            for result in results:
                                sectores = Sector(result[0], result[1], result[2])
                                data['SECTORS'].append(sectores)
                            print("\n**** SECTORES - DATOS OBTENIDOS ****\n")
                            self.db.close()
                            return data
                        if _sopcion == 4:
                            _Qdiccionario["name_Query"] = "ONLY_SUB_SECTORS"
                            query = self.reader_json.getQuery(_Qdiccionario)
                            results = self.db.execute_query(query)
                            if results is None:
                                return {}
                            data = {
                                'SUB_SECTORS': []
                            }
                            for result in results:
                                subsectores = Subsector(result[0], result[1], result[2])
                                data['SUB_SECTORS'].append(subsectores)

                            print("\n**** SUBSECTORES - DATOS OBTENIDOS ****\n")

                            self.db.close()
                            return data
                elif _popcion == "PARAMETRE_DATA":
                    if "sopcion" in _diccionario:
                        _sopcion = _diccionario["sopcion"]
                        _Qdiccionario = {
                            "popcion": "Places",
                            "sopcion": "PARAMETRE_DATA"
                        }
                        if _sopcion == 1:
                            _Qdiccionario["name_Query"] = "SPECIFIC_CITY"
                            _Qdiccionario["id"] = _diccionario["id_Prov"]
                            query = self.reader_json.getQuery(_Qdiccionario)
                            results = self.db.execute_query(query)
                            if results is None:
                                return {}
                            data = {
                                'CITIESxPROV': []
                            }
                            for result in results:
                                ciudades = CiudadxProvincia(result[0], result[1])
                                data['CITIESxPROV'].append(ciudades)
                            print("\n**** CIUDADES ESPECIFICAS POR PROVINCIA - DATOS OBTENIDOS ****\n")
                            self.db.close()
                            return data
                        elif _sopcion == 2:
                            _Qdiccionario["name_Query"] = "SPECIFIC_SECTOR"
                            _Qdiccionario["id"] = _diccionario["id_City"]
                            query = self.reader_json.getQuery(_Qdiccionario)
                            results = self.db.execute_query(query)
                            if results is None:
                                return {}
                            data = {
                                'SECTORSxCITY': []
                            }
                            for result in results:
                                sector = SectorxCiudad(result[0], result[1])
                                data['SECTORSxCITY'].append(sector)
                            print("\n**** SECTORES ESPECIFICOS POR CIUDAD - DATOS OBTENIDOS ****\n")
                            self.db.close()
                            return data
                        elif _sopcion == 3:
                            _Qdiccionario["name_Query"] = "SPECIFIC_SUBSECTOR"
                            _Qdiccionario["id"] = _diccionario["id_Sector"]
                            query = self.reader_json.getQuery(_Qdiccionario)
                            results = self.db.execute_query(query)
                            if results is None:
                                return {}
                            data = {
                                'SUB_SECTORSxSECTOR': []
                            }
                            for result in results:
                                sector = SubsectorxSector(result[0], result[1])
                                data['SUB_SECTORSxSECTOR'].append(sector)
                            print("\n**** SUB SECTORES ESPECIFICOS POR SECTOR - DATOS OBTENIDOS ****\n")
                            self.db.close()
                            return data
                        elif _sopcion == 4:
                            _Qdiccionario["name_Query"] = "SPECIFIC_PROVXTT"
                            _Qdiccionario["_V1"] = _diccionario["_V1"]
                            _Qdiccionario["_V2"] = _diccionario["_V2"]
                            query = self.reader_json.getQuery(_Qdiccionario)
                            results = self.db.execute_query(query)
                            if results is None:
                                return {}
                            data = {
                                'PROVINCIES': []
                            }
                            for result in results:
                                provincia = Provincia(result[0], result[1])
                                data['PROVINCIES'].append(provincia)
                            print("\n**** PROVINCIA ESPECIFICAS TT - DATOS OBTENIDOS ****\n")
                            self.db.close()
                            return data
                        elif _sopcion == 5:
                            _Qdiccionario["name_Query"] = "SPECIFIC_CITYXTT"
                            _Qdiccionario["_V1"] = _diccionario["id_Prov"]
                            _Qdiccionario["_V2"] = _diccionario["_V1"]
                            _Qdiccionario["_V3"] = _diccionario["_V2"]
                            query = self.reader_json.getQuery(_Qdiccionario)
                            results = self.db.execute_query(query)
                            if results is None:
                                return {}
                            data = {
                                'CITIESxPROV': []
                            }
                            for result in results:
                                ciudad = CiudadxProvincia(result[0], result[1])
                                data['CITIESxPROV'].append(ciudad)
                            print("\n**** CIUDADES ESPECIFICAS TT - DATOS OBTENIDOS ****\n")
                            self.db.close()
                            return data
                        elif _sopcion == 6:
                            _Qdiccionario["name_Query"] = "SPECIFIC_SECTXTT"
                            _Qdiccionario["_V1"] = _diccionario["id_City"]
                            _Qdiccionario["_V2"] = _diccionario["_V1"]
                            _Qdiccionario["_V3"] = _diccionario["_V2"]
                            query = self.reader_json.getQuery(_Qdiccionario)
                            results = self.db.execute_query(query)
                            if results is None:
                                return {}
                            data = {
                                'SECTORSxCITY': []
                            }
                            for result in results:
                                sector = SectorxCiudad(result[0], result[1])
                                data['SECTORSxCITY'].append(sector)
                            print("\n**** SECTORES ESPECIFICOS TT - DATOS OBTENIDOS ****\n")
                            self.db.close()
                            return data
                        elif _sopcion == 7:
                            _Qdiccionario["name_Query"] = "SECTMXTT"
                            for i, city_id in enumerate(_diccionario["id_Cities"]):
                                key = f"_V1_{i + 1}"  # Nombre único para cada valor de id_Cities
                                _Qdiccionario[key] = city_id
                            _Qdiccionario["_V2"] = _diccionario["_V1"]
                            _Qdiccionario["_V3"] = _diccionario["_V2"]
                            query = self.reader_json.getQuery(_Qdiccionario)
                            results = self.db.execute_query(query)
                            if results is None:
                                return {}
                            data = {
                                'SECTORSxCITY': []
                            }
                            for result in results:
                                sector = SectorxCiudad(result[0], result[1])
                                data['SECTORSxCITY'].append(sector)
                            print("\n**** SECTORES ESPECIFICOS TT - DATOS OBTENIDOS ****\n")
                            self.db.close()
                            return data
                        else:
                            self.db.close()
                            print("Segunda Opción no válida: ", _sopcion)
                else:
                    print("La clave 'popcion' no está presente en el diccionario _parametro")
                    print("Eso o el valor de 'popcion' no es valida: ", _popcion)
        except Exception as e:
            self.db.close()
            print("--------------------------------------------------------------------")
            print("getData_Places - PlaceRepository | Error: ", e)
            print("--------------------------------------------------------------------")
            return {}
