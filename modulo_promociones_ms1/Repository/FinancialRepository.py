from Models.model_finance import MPagos, Buro, UPGRADE, Precio_Regular, Dias_Gozados
from Resources.database.connection import connection
from Utils.ReaderJSON import ReaderJSON


class FinancialRepository:
    def __init__(self):
        self.db = connection()
        self.reader_json = ReaderJSON()

    def getData_Financial(self, _diccionario: dict) -> dict:
        try:
            if "name_Query" in _diccionario:
                _Qdiccionario = {"popcion": "Finance", "name_Query": _diccionario['name_Query']}
                if '_V1' in _diccionario:
                    _Qdiccionario['_V1'] = _diccionario["_V1"]
                    if '_V2' in _diccionario:
                        _Qdiccionario['_V2'] = _diccionario["_V2"]
                self.db.connect()
                query = self.reader_json.getQuery(_Qdiccionario)
                results = self.db.execute_query(query)
                if results is None:
                    print("RESULTS devolvio vacio")
                    return {}
                data = {}
                if _diccionario['name_Query'] == "ALL_MPAGOS":
                    data['MPAGOS'] = []
                    for result in results:
                        mpagos = MPagos(result[0], result[1])
                        data['MPAGOS'].append(mpagos)

                if _diccionario['name_Query'] == "ALL_BURO":
                    data['BURO'] = []
                    for result in results:
                        buro = Buro(result[0], result[1])
                        data['BURO'].append(buro)

                if _diccionario['name_Query'] == "UPGRADE":
                    data["UPGRADE"] = []
                    for result in results:
                        dt = UPGRADE(result[0], result[1])
                        data['UPGRADE'].append(dt)

                if _diccionario['name_Query'] == "PRECIO_REGULAR":
                    data['PRECIO_REGULAR'] = []
                    for result in results:
                        dt = Precio_Regular(result[0])
                        data[_diccionario['name_Query']].append(dt)

                if _diccionario['name_Query'] == "DIAS_GOZADOS":
                    data['DIAS_GOZADOS'] = []
                    for result in results:
                        dt = Dias_Gozados(result[0], result[1])
                        data['DIAS_GOZADOS'].append(dt)

                print("\n**** " + _diccionario['name_Query'] + " - DATOS OBTENIDOS ****\n")
                self.db.close()
                return data

        except Exception as e:
            self.db.close()
            print("--------------------------------------------------------------------")
            print("getData_ModoPagos - FinancialRepository | Error: ", e)
            print("--------------------------------------------------------------------")
            return {}
