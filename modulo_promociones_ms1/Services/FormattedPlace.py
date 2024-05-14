from flask import jsonify


class FormattedPlace:
    @staticmethod
    def formated_placeSIMPLEDATA(data, _type: str):
        try:
            _provincias = {"ALL_PROVS", "PROVINCIAS_ESPECIFICASxTFV"}
            _ciudades = {"ALL_CITIES"}
            _sectores = {"ALL_SECTORS"}
            if _type in _provincias:
                json_data = {
                    'PROVINCIES': []
                }
                for provincia in data['PROVINCIES']:
                    json_data['PROVINCIES'].append({
                        'PROVINCIA_ID': provincia.PROVINCIA_ID,
                        'PROVINCIA': provincia.PROVINCIA
                    })
                return json_data
            if _type in _ciudades:
                json_data = {
                    'CITIES': []
                }
                for ciudad in data['CITIES']:
                    json_data['CITIES'].append({
                        'CIUDAD_ID': ciudad.CIUDAD_ID,
                        'CIUDAD': ciudad.CIUDAD,
                        'PROVINCIA': ciudad.PROVINCIA
                    })
                return json_data
            if _type in _sectores:
                json_data = {
                    'SECTORS': []
                }
                for sector in data['SECTORS']:
                    json_data['SECTORS'].append({
                        'SECTOR_ID': sector.SECTOR_ID,
                        'SECTOR': sector.SECTOR,
                        'CIUDAD': sector.CIUDAD
                    })
                return json_data
        except Exception as e:
            print("--------------------------------------------------------------------")
            print("FormattedPlace - formated_placeALLDATA | Error: "+_type+" - ", e)
            print("--------------------------------------------------------------------")
            return jsonify({'Error': str(e)})

    @staticmethod
    def formated_placeMIXDATA(data, _type: str):
        try:
            _provincias = {"PROVINCIAS_ESPECIFICASxTFV"}
            _ciudades = {"CIUDADES_ESPECIFICASxPROV", "CIUDADES_ESPECIFICASxPROVxTFV", "CIUDADES_ESPECIFICASxTFV"}
            _sectores = {"SECTORES_ESPECIFICOSxCITY", "SECTORES_ESPECIFICOSxCITYxTFV", "SECTORES_ESPECIFICOSxTFV"}
            if _type in _provincias:
                if _type in _provincias:
                    json_data = {
                        'PROVINCIES': []
                    }
                    for provincia in data['PROVINCIES']:
                        json_data['PROVINCIES'].append({
                            'PROVINCIA_ID': provincia.PROVINCIA_ID,
                            'PROVINCIA': provincia.PROVINCIA
                        })
                    return json_data
            if _type in _ciudades:
                json_data = {
                    'CITIESxPROV': []
                }
                for ciudad in data['CITIESxPROV']:
                    json_data['CITIESxPROV'].append({
                        'CIUDAD_ID': ciudad.CIUDAD_ID,
                        'CIUDAD': ciudad.CIUDAD,
                        'PROVINCIA': ciudad.PROVINCIA
                    })
                return json_data
            if _type in _sectores:
                json_data = {
                    'SECTORSxCITY': []
                }
                for sector in data['SECTORSxCITY']:
                    json_data['SECTORSxCITY'].append({
                        'SECTOR_ID': sector.SECTOR_ID,
                        'SECTOR': sector.SECTOR,
                        'CIUDAD': sector.CIUDAD
                    })
                return json_data
        except Exception as e:
            print("--------------------------------------------------------------------")
            print("FormattedPlace - formated_placeMIXDATA | Error: "+_type+" - ", e)
            print("--------------------------------------------------------------------")
            return jsonify({'Error': str(e)})
