from Models.model_finance import MPagos, Buro, UPGRADE, Precio_Regular, Dias_Gozados
from Resources.database.connection import connection
from Utils.ReaderJSON import ReaderJSON


class FinancialRepository:
    def __init__(self):
        self.db = connection()
        self.reader_json = ReaderJSON()

    def getData_Financial(self, _diccionario: dict) -> dict:
        try:
            if "popcion" in _diccionario:
                _popcion = _diccionario["popcion"]
                self.db.connect()
                if _popcion == "ALL_MPAGOS":
                    if "sopcion" in _diccionario:
                        _sopcion = _diccionario["sopcion"]
                        _Qdiccionario = {
                            "popcion": "Finance",
                            "sopcion": "ALL_MPAGOS"
                        }
                        if _sopcion == 1:
                            _Qdiccionario["name_Query"] = "ALL_MPAGOS"
                            query = self.reader_json.getQuery(_Qdiccionario)
                            results = self.db.execute_query(query)
                            if results is None:
                                return {}
                            data = {
                                'MPAGOS': []
                            }
                            for result in results:
                                mpagos = MPagos(result[0], result[1])
                                data['MPAGOS'].append(mpagos)
                            print("\n**** Modo de Pago - DATOS OBTENIDOS ****\n")
                            self.db.close()
                            return data
                if _popcion == "ALL_BURO":
                    if "sopcion" in _diccionario:
                        _sopcion = _diccionario["sopcion"]
                        _Qdiccionario = {
                            "popcion": "Finance",
                            "sopcion": "ALL_BURO"
                        }
                        if _sopcion == 1:
                            _Qdiccionario["name_Query"] = "ALL_BURO"
                            query = self.reader_json.getQuery(_Qdiccionario)
                            results = self.db.execute_query(query)
                            if results is None:
                                return {}
                            data = {
                                'BURO': []
                            }
                            for result in results:
                                buro = Buro(result[0], result[1])
                                data['BURO'].append(buro)
                            print("\n**** BURO - DATOS OBTENIDOS ****\n")
                            self.db.close()
                            return data
                if _popcion == "UPGRADE" or _popcion == "PRECIO_REGULAR" or _popcion == "DIAS_GOZADOS":
                    _Qdiccionario = {
                        "popcion": "Finance",
                        "sopcion": _popcion
                    }
                    if '_V1' in _diccionario:
                        _Qdiccionario["_V1"] = _diccionario["_V1"]
                        if '_V2' in _diccionario:
                            _Qdiccionario["_V2"] = _diccionario["_V2"]
                    query = self.reader_json.getQuery(_Qdiccionario)
                    results = self.db.execute_query(query)
                    if results is None:
                        return {}
                    data = {
                        _popcion: []
                    }
                    for result in results:
                        if _popcion == "UPGRADE":
                            dt = UPGRADE(result[0], result[1])
                            data[_popcion].append(dt)
                        if _popcion == "PRECIO_REGULAR":
                            dt = Precio_Regular(result[0], result[1])
                            data[_popcion].append(dt)
                        if _popcion == "DIAS_GOZADOS":
                            dt = Dias_Gozados(result[0], result[1])
                            data[_popcion].append(dt)
                    print("\n**** "+_popcion+" - DATOS OBTENIDOS ****\n")
                    self.db.close()
                    return data

        except Exception as e:
            self.db.close()
            print("--------------------------------------------------------------------")
            print("getData_ModoPagos - FinancialRepository | Error: ", e)
            print("--------------------------------------------------------------------")
            return {}
