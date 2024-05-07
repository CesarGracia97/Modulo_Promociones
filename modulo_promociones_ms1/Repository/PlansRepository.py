from Models.model_place import Provincia, Ciudad, Sector
from Models.model_plane import Ofertas, Servicios, Tipo_Servicios, TariffPlanes, TariffPlanVariant, \
    TariffPlan_X_TariffPlanVariant, Tecnologias, Productos
from Resources.database.connection import connection
from Utils.ReaderJSON import ReaderJSON


class PlansRepository:
    def __init__(self):
        self.db = connection()
        self.reader_json = ReaderJSON()

    def getData_Planes(self, _diccionario: dict) -> dict:
        try:
            if "popcion" in _diccionario:
                _popcion = _diccionario["popcion"]
                self.db.connect()
                if _popcion == "ALL_DATA":
                    if "sopcion" in _diccionario:
                        _sopcion = _diccionario["sopcion"]
                        if _sopcion == "OFER":
                            _Qdiccionario = {"popcion": "Planes",
                                             "sopcion": "ALL_DATA",
                                             "topcion": "OFER",
                                             "name_Query": "AD_OFERTAS"}
                            query = self.reader_json.getQuery(_Qdiccionario)
                            results = self.db.execute_query(query)
                            if results is None:
                                return {}
                            data = {
                                'OFERTAS': []
                            }
                            for result in results:
                                oferta = Ofertas(result[0], result[1])
                                data['OFERTAS'].append(oferta)
                            print("\n**** OFERTAS - DATOS OBTENIDOS ****\n")
                            self.db.close()
                            return data

                        if _sopcion == "SERV":
                            _Qdiccionario = {"popcion": "Planes",
                                             "sopcion": "ALL_DATA",
                                             "topcion": "SERV",
                                             "name_Query": "AD_SERVICIOS"}
                            query = self.reader_json.getQuery(_Qdiccionario)
                            results = self.db.execute_query(query)
                            if results is None:
                                return {}
                            data = {
                                'SERVICIOS': []
                            }
                            for result in results:
                                servicio = Servicios(result[0])
                                data['SERVICIOS'].append(servicio)
                            print("\n**** SERVICIOS - DATOS OBTENIDOS ****\n")
                            self.db.close()
                            return data
                        if _sopcion == "TECN":
                            _Qdiccionario = {"popcion": "Planes",
                                             "sopcion": "ALL_DATA",
                                             "topcion": "TECN",
                                             "name_Query": "AD_TECNOLOGIAS"}
                            query = self.reader_json.getQuery(_Qdiccionario)
                            results = self.db.execute_query(query)
                            if results is None:
                                return {}
                            data = {
                                'TECNOLOGIAS': []
                            }
                            for result in results:
                                tecnologia = Tecnologias(result[0])
                                data['TECNOLOGIAS'].append(tecnologia)
                            print("\n**** TECNOLOGIAS - DATOS OBTENIDOS ****\n")
                            self.db.close()
                            return data

                        if _sopcion == "TISE":
                            _Qdiccionario = {"popcion": "Planes",
                                             "sopcion": "ALL_DATA",
                                             "topcion": "TISE",
                                             "name_Query": "AD_TIPO_SERVICIO"}
                            query = self.reader_json.getQuery(_Qdiccionario)
                            results = self.db.execute_query(query)
                            if results is None:
                                return {}
                            data = {
                                'TIPO_SERVICIO': []
                            }
                            for result in results:
                                tservicio = Tipo_Servicios(result[0])
                                data['TIPO_SERVICIO'].append(tservicio)
                            print("\n**** TIPO DE SERVICIO - DATOS OBTENIDOS ****\n")
                            self.db.close()
                            return data

                        if _sopcion == "PLAN":
                            _topcion = _diccionario["topcion"]
                            if _topcion == 1:
                                _Qdiccionario = {"popcion": "Planes",
                                                 "sopcion": "ALL_DATA",
                                                 "topcion": "PLAN",
                                                 "name_Query": "AD_TARIFFPLAN"}
                                query = self.reader_json.getQuery(_Qdiccionario)
                                results = self.db.execute_query(query)
                                if results is None:
                                    return {}
                                data = {
                                    'PLANES': []
                                }
                                for result in results:
                                    planes = TariffPlanes(result[0], result[1])
                                    data['PLANES'].append(planes)
                                print("\n**** PLANES - DATOS OBTENIDOS ****\n")
                                self.db.close()
                                return data

                            if _topcion == 2:
                                _V1 = _diccionario["_V1"]
                                _V2 = _diccionario["_V2"]
                                _V3 = _diccionario["_V3"]
                                _Qdiccionario = {"popcion": "Planes",
                                                 "sopcion": "ALL_DATA",
                                                 "topcion": "PLAN",
                                                 "name_Query": "AD_TARIFFPLANVARIANT",
                                                 "_V1": _V1,
                                                 "_V2": _V2,
                                                 "_V3": _V3}
                                query = self.reader_json.getQuery(_Qdiccionario)
                                results = self.db.execute_query(query)
                                if results is None:
                                    return {}
                                data = {
                                    'PLANES': []
                                }
                                for result in results:
                                    planes = TariffPlanVariant(result[0], result[1])
                                    data['PLANES'].append(planes)
                                print("\n**** PLANES - DATOS OBTENIDOS ****\n")
                                self.db.close()
                                return data

                            if _topcion == 3:

                                _Qdiccionario = {"popcion": "Planes",
                                                 "sopcion": "ALL_DATA",
                                                 "topcion": "PLAN",
                                                 "name_Query": "AD_TARIFFPLAN_TARIFFPLANVARIANT"}
                                query = self.reader_json.getQuery(_Qdiccionario)
                                results = self.db.execute_query(query)
                                if results is None:
                                    return {}
                                data = {
                                    'PLANES': []
                                }
                                for result in results:
                                    planes = TariffPlan_X_TariffPlanVariant(result[0], result[1], result[2], result[3])
                                    data['PLANES'].append(planes)
                                print("\n**** PLANES - DATOS OBTENIDOS ****\n")
                                self.db.close()
                                return data

                if _popcion == "COMBO":
                    if "sopcion" in _diccionario:
                        _sopcion = _diccionario["sopcion"]
                        if _sopcion == 1:
                            _V1 = _diccionario["_V1"]
                            _Qdiccionario = {"popcion": "Planes",
                                             "sopcion": "COMBO",
                                             "name_Query": "COMBO_TIPO_SERVICIOS",
                                             "_V1": _V1}
                            query = self.reader_json.getQuery(_Qdiccionario)
                            results = self.db.execute_query(query)
                            if results is None:
                                return {}
                            data = {
                                'C_TIPO_SERVICIOS': []
                            }
                            for result in results:
                                _CTipoSer = Tipo_Servicios(result[0])
                                data['C_TIPO_SERVICIOS'].append(_CTipoSer)
                            print("\n**** C_TIPO DE SERVICIOS - DATOS OBTENIDOS ****\n")
                            self.db.close()
                            return data

                        if _sopcion == 2:
                            _V1 = _diccionario["_V1"]
                            _V2 = _diccionario["_V2"]
                            _Qdiccionario = {"popcion": "Planes",
                                             "sopcion": "COMBO",
                                             "name_Query": "COMBO_PRODUCTO",
                                             "_V1": _V1,
                                             "_V2": _V2}
                            query = self.reader_json.getQuery(_Qdiccionario)
                            results = self.db.execute_query(query)
                            if results is None:
                                return {}
                            data = {
                                'C_PRODUCTOS': []
                            }
                            for result in results:
                                _CProductos = Productos(result[0], result[1])
                                data['C_PRODUCTOS'].append(_CProductos)
                            print("\n**** C_PRODUCTOS- DATOS OBTENIDOS ****\n")
                            self.db.close()
                            return data

                        if _sopcion == 3:
                            _V1 = _diccionario["_V1"]
                            _V2 = _diccionario["_V2"]
                            _V3 = _diccionario["_V3"]
                            _Qdiccionario = {"popcion": "Planes",
                                             "sopcion": "COMBO",
                                             "name_Query": "COMBO_PLANES",
                                             "_V1": _V1,
                                             "_V2": _V2,
                                             "_V3": _V3}
                            query = self.reader_json.getQuery(_Qdiccionario)
                            results = self.db.execute_query(query)
                            if results is None:
                                return {}
                            data = {
                                'C_PLANES': []
                            }
                            for result in results:
                                _CTariffPlanVariant = TariffPlanVariant(result[0], result[1])
                                data['C_PLANES'].append(_CTariffPlanVariant)
                            print("\n**** C_PLANES - DATOS OBTENIDOS ****\n")
                            self.db.close()
                            return data

                        if _sopcion == 4:
                            _V1 = _diccionario["_V1"]
                            _V2 = _diccionario["_V2"]
                            _V3 = _diccionario["_V3"]
                            _V4 = _diccionario["_V4"]
                            _Qdiccionario = {"popcion": "Planes",
                                             "sopcion": "COMBO",
                                             "name_Query": "COMBO_PROVINCIA",
                                             "_V1": _V1,
                                             "_V2": _V2,
                                             "_V3": _V3,
                                             "_V4": _V4}
                            query = self.reader_json.getQuery(_Qdiccionario)
                            results = self.db.execute_query(query)
                            if results is None:
                                return {}
                            data = {
                                'C_PROVINCIA': []
                            }
                            for result in results:
                                _CProvincias = Provincia(result[0], result[1])
                                data['C_PROVINCIA'].append(_CProvincias)
                            print("\n**** C_PROVINCIAS - DATOS OBTENIDOS ****\n")
                            self.db.close()
                            return data

                        if _sopcion == 5:
                            _V1 = _diccionario["_V1"]
                            _V2 = _diccionario["_V2"]
                            _V3 = _diccionario["_V3"]
                            _V4 = _diccionario["_V4"]
                            _V5 = _diccionario["_V5"]
                            _Qdiccionario = {"popcion": "Planes",
                                             "sopcion": "COMBO",
                                             "name_Query": "COMBO_CIUDAD",
                                             "_V1": _V1,
                                             "_V2": _V2,
                                             "_V3": _V3,
                                             "_V4": _V4,
                                             "_V5": _V5}
                            query = self.reader_json.getQuery(_Qdiccionario)
                            results = self.db.execute_query(query)
                            if results is None:
                                return {}
                            data = {
                                'C_CIUDAD': []
                            }
                            for result in results:
                                _CCiudad = Ciudad(result[0], result[1], result[2])
                                data['C_CIUDAD'].append(_CCiudad)
                            print("\n**** C_CIUDAD - DATOS OBTENIDOS ****\n")
                            self.db.close()
                            return data

                        if _sopcion == 6:
                            _V1 = _diccionario["_V1"]
                            _V2 = _diccionario["_V2"]
                            _V3 = _diccionario["_V3"]
                            _V4 = _diccionario["_V4"]
                            _V5 = _diccionario["_V5"]
                            _V6 = _diccionario["_V6"]
                            _Qdiccionario = {"popcion": "Planes",
                                             "sopcion": "COMBO",
                                             "name_Query": "COMBO_SECTOR",
                                             "_V1": _V1,
                                             "_V2": _V2,
                                             "_V3": _V3,
                                             "_V4": _V4,
                                             "_V5": _V5,
                                             "_V6": _V6}
                            query = self.reader_json.getQuery(_Qdiccionario)
                            results = self.db.execute_query(query)
                            if results is None:
                                return {}
                            data = {
                                'C_SECTOR': []
                            }
                            for result in results:
                                _CSector = Sector(result[0], result[1], result[2])
                                data['C_SECTOR'].append(_CSector)
                            print("\n**** C_CIUDAD - DATOS OBTENIDOS ****\n")
                            self.db.close()
                            return data
        except Exception as e:
            self.db.close()
            print("--------------------------------------------------------------------")
            print("getData_Planes - PlansRepository | Error: ", e)
            print("--------------------------------------------------------------------")
            return {}
