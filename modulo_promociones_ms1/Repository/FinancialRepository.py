from Models.model_finance import MPagos, Buro
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
        except Exception as e:
            self.db.close()
            print("--------------------------------------------------------------------")
            print("getData_ModoPagos - FinancialRepository | Error: ", e)
            print("--------------------------------------------------------------------")
            return {}
