from Models.model_place import Provincia, Ciudad, Sector
from Models.model_plane import Ofertas, Servicios, Tipo_Servicios, TariffPlanes, TariffPlanVariant, \
    TariffPlan_X_TariffPlanVariant, Tecnologias, Producto
from Resources.database.connection import connection
from Utils.ReaderJSON import ReaderJSON


class PlansRepository:
    def __init__(self):
        self.db = connection()
        self.reader_json = ReaderJSON()

    def getData_Planes(self, _diccionario: dict) -> dict:
        try:
            if "popcion" in _diccionario:
                self.db.connect()
                if _diccionario["popcion"] == "ALL_DATA":
                    if "sopcion" in _diccionario:
                        valid_sopcion = {'AD_TARIFFPLAN', 'AD_TARIFFPLANVARIANT', 'AD_TARIFFPLAN_TARIFFPLANVARIANT',
                                         'AD_TARIFFPLANVARIANT_PRODUCTO_ADICIONAL'}
                        _Qdiccionario = {"popcion": "Planes", "sopcion": _diccionario["popcion"]}
                        if _diccionario["sopcion"] == "OFER":
                            _Qdiccionario['topcion'] = _diccionario["sopcion"]
                            _Qdiccionario['name_Query'] = "AD_OFERTAS"
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

                        if _diccionario["sopcion"] == "SERV":
                            _Qdiccionario['topcion'] = _diccionario["sopcion"]
                            _Qdiccionario['name_Query'] = "AD_SERVICIOS"
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

                        if _diccionario["sopcion"] == "TECN":
                            _Qdiccionario['topcion'] = _diccionario["sopcion"]
                            _Qdiccionario['name_Query'] = "AD_TECNOLOGIAS"
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

                        if _diccionario["sopcion"] == "TISE":
                            _Qdiccionario['topcion'] = _diccionario["sopcion"]
                            _Qdiccionario['name_Query'] = "AD_TIPO_SERVICIO"
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

                        if _diccionario["sopcion"] in valid_sopcion:
                            data = {}
                            _Qdiccionario['topcion'] = _diccionario["sopcion"]
                            if '_V1' in _diccionario:
                                _Qdiccionario['_V1'] = _diccionario['_V1']
                                if '_V2' in _diccionario:
                                    _Qdiccionario['_V2'] = _diccionario['_V2']

                            query = self.reader_json.getQuery(_Qdiccionario)
                            results = self.db.execute_query(query)
                            if results is None:
                                print("--- EL RESULTADO DE LA CONSULTA FUE NULLO ---")
                                return data
                            self.db.close()
                            data = {'PLANES': []}

                            if _diccionario['sopcion'] == "AD_TARIFFPLAN":
                                for result in results:
                                    planes = TariffPlanes(result[0], result[1])
                                    data['PLANES'].append(planes)

                            if (_diccionario['sopcion'] == "AD_TARIFFPLANVARIANT" or
                                    _diccionario['sopcion'] == "AD_TARIFFPLANVARIANT_PRODUCTO_ADICIONAL"):
                                for result in results:
                                    planes = TariffPlanVariant(result[0], result[1])
                                    data['PLANES'].append(planes)

                            if _diccionario['sopcion'] == "AD_TARIFFPLAN_TARIFFPLANVARIANT":
                                for result in results:
                                    planes = TariffPlanes(result[0], result[1])
                                    data['PLANES'].append(planes)
                            print("\n**** PLANES - DATOS OBTENIDOS ****\n")
                            return data

                if _diccionario["popcion"] == "COMBO":
                    if "sopcion" in _diccionario:
                        _sopcion = _diccionario["sopcion"]
                        if _sopcion == 1:
                            _V1 = _diccionario["_V1"]
                            _Qdiccionario = {"popcion": "Planes",
                                             "sopcion": "COMBO",
                                             "name_Query": "COMBO_PLAN",
                                             "_V1": _V1}
                            query = self.reader_json.getQuery(_Qdiccionario)
                            results = self.db.execute_query(query)
                            if results is None:
                                return {}
                            data = {
                                'COMBO_PLAN': []
                            }
                            for result in results:
                                _COMBO_PLAN = TariffPlanes(result[0], result[1])
                                data['COMBO_PLAN'].append(_COMBO_PLAN)
                            print("\n**** COMBO_PLAN - DATOS OBTENIDOS ****\n")
                            self.db.close()
                            return data

                        if _sopcion == 2:
                            _V1 = _diccionario["_V1"]
                            _Qdiccionario = {"popcion": "Planes",
                                             "sopcion": "COMBO",
                                             "name_Query": "COMBO_PLANVARIANT",
                                             "_V1": _V1}
                            query = self.reader_json.getQuery(_Qdiccionario)
                            results = self.db.execute_query(query)
                            if results is None:
                                return {}
                            data = {
                                'COMBO_PLANVARIANT': []
                            }
                            for result in results:
                                _COMBO_PLANVARIANT = TariffPlanVariant(result[0], result[1])
                                data['COMBO_PLANVARIANT'].append(_COMBO_PLANVARIANT)
                            print("\n**** COMBO_PLANVARIANT - DATOS OBTENIDOS ****\n")
                            self.db.close()
                            return data

                        if _sopcion == 3:
                            _V1 = _diccionario["_V1"]
                            _Qdiccionario = {"popcion": "Planes",
                                             "sopcion": "COMBO",
                                             "name_Query": "COMBO_PRODUCTO",
                                             "_V1": _V1}
                            query = self.reader_json.getQuery(_Qdiccionario)
                            results = self.db.execute_query(query)
                            if results is None:
                                return {}
                            data = {
                                'COMBO_PRODUCTO': []
                            }
                            for result in results:
                                _COMBO_PRODUCTO = Producto(result[0], result[1])
                                data['COMBO_PRODUCTO'].append(_COMBO_PRODUCTO)
                            print("\n**** COMBO_PRODUCTO - DATOS OBTENIDOS ****\n")
                            self.db.close()
                            return data

                        if _sopcion == 4:
                            _V1 = _diccionario["_V1"]
                            _Qdiccionario = {"popcion": "Planes",
                                             "sopcion": "COMBO",
                                             "name_Query": "COMBO_TIPO_SERVICIO",
                                             "_V1": _V1}
                            query = self.reader_json.getQuery(_Qdiccionario)
                            results = self.db.execute_query(query)
                            if results is None:
                                return {}
                            data = {
                                'COMBO_TIPO_SERVICIO': []
                            }
                            for result in results:
                                _COMBO_TIPO_SERVICIO = Tipo_Servicios(result[0])
                                data['COMBO_TIPO_SERVICIO'].append(_COMBO_TIPO_SERVICIO)
                            print("\n**** COMBO_TIPO_SERVICIO - DATOS OBTENIDOS ****\n")
                            self.db.close()
                            return data

                        if _sopcion == 5:
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

                        if _sopcion == 6:
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

                        if _sopcion == 7:
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

                        if _sopcion == 8:
                            _Qdiccionario = {"popcion": "Planes",
                                             "sopcion": "COMBO",
                                             "name_Query": "COMBO_PRODUCTO_ROUTER"}
                            query = self.reader_json.getQuery(_Qdiccionario)
                            results = self.db.execute_query(query)
                            if results is None:
                                return {}
                            data = {
                                'COMBO_PRODUCTO': []
                            }
                            for result in results:
                                _COMBO_PRODUCTO = Producto(result[0], result[1])
                                data['COMBO_PRODUCTO'].append(_COMBO_PRODUCTO)
                            print("\n**** COMBO_PRODUCTO - DATOS OBTENIDOS ****\n")
                            self.db.close()
                            return data
        except Exception as e:
            self.db.close()
            print("--------------------------------------------------------------------")
            print("getData_Planes - PlansRepository | Error: ", e)
            print("--------------------------------------------------------------------")
            return {}
