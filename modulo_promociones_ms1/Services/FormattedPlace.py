from flask import jsonify


class FormattedPlace:
    @staticmethod
    def formated_provinces(data):
        try:
            json_data = {
                'PROVINCIES': []
            }
            for provincia in data['PROVINCIES']:
                json_data['PROVINCIES'].append({
                    'PROVINCIA_ID': provincia.PROVINCIA_ID,
                    'PROVINCIA': provincia.PROVINCIA
                })
            return json_data
        except Exception as e:
            print("--------------------------------------------------------------------")
            print("FormattedPlace - formated_provinces | Error: ", e)
            print("--------------------------------------------------------------------")
            return jsonify({'Error': str(e)})

    @staticmethod
    def formated_cities(data):
        try:
            json_data = {
                'CITIES': []
            }
            for ciudad in data['CITIES']:
                json_data['CITIES'].append({
                    'CIUDAD_ID': ciudad.CIUDAD_ID,
                    'PROVINCIA_ID': ciudad.PROVINCIA_ID,
                    'CIUDAD': ciudad.CIUDAD
                })
            return json_data
        except Exception as e:
            print("--------------------------------------------------------------------")
            print("FormattedPlace - formated_cities | Error: ", e)
            print("--------------------------------------------------------------------")
            return jsonify({'Error': str(e)})

    @staticmethod
    def formated_sectors(data):
        try:
            json_data = {
                'SECTORS': []
            }
            for sector in data['SECTORS']:
                json_data['SECTORS'].append({
                    'SECTOR_ID': sector.SECTOR_ID,
                    'CIUDAD_ID': sector.CIUDAD_ID,
                    'SECTOR': sector.SECTOR
                })
            return json_data
        except Exception as e:
            print("--------------------------------------------------------------------")
            print("FormattedPlace - formated_sectors | Error: ", e)
            print("--------------------------------------------------------------------")
            return jsonify({'Error': str(e)})

    @staticmethod
    def formated_sub_sectors(data):
        try:
            json_data = {
                'SUB_SECTORS': []
            }
            for subsector in data['SUB_SECTORS']:
                json_data['SUB_SECTORS'].append({
                    'SUBSECTOR_ID': subsector.SUBSECTOR_ID,
                    'SECTOR_ID': subsector.SECTOR_ID,
                    'SUBSECTOR': subsector.SUBSECTOR
                })
            return json_data
        except Exception as e:
            print("--------------------------------------------------------------------")
            print("FormattedPlace - formated_sub_sectors | Error: ", e)
            print("--------------------------------------------------------------------")
            return jsonify({'Error': str(e)})

    @staticmethod
    def formated_specific_city(data):
        try:
            json_data = {
                'CITIESxPROV': []
            }
            for ciudad in data['CITIESxPROV']:
                json_data['CITIESxPROV'].append({
                    'CIUDAD_ID': ciudad.CIUDAD_ID,
                    'CIUDAD': ciudad.CIUDAD
                })
            return json_data
        except Exception as e:
            print("--------------------------------------------------------------------")
            print("FormattedPlace - formated_specific_city | Error: ", e)
            print("--------------------------------------------------------------------")
            return jsonify({'Error': str(e)})

    @staticmethod
    def formated_specific_sector(data):
        try:
            json_data = {
                'SECTORSxCITY': []
            }
            for sector in data['SECTORSxCITY']:
                json_data['SECTORSxCITY'].append({
                    'SECTOR_ID': sector.SECTOR_ID,
                    'SECTOR': sector.SECTOR
                })
            return json_data
        except Exception as e:
            print("--------------------------------------------------------------------")
            print("FormattedPlace - formated_specific_sector | Error: ", e)
            print("--------------------------------------------------------------------")
            return jsonify({'Error': str(e)})

    @staticmethod
    def formated_specific_sectortt(data):
        try:
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
            print("FormattedPlace - formated_specific_sector | Error: ", e)
            print("--------------------------------------------------------------------")
            return jsonify({'Error': str(e)})

    @staticmethod
    def formated_specific_sub_sector(data):
        try:
            json_data = {
                'SUB_SECTORSxSECTOR': []
            }
            for subsector in data['SUB_SECTORSxSECTOR']:
                json_data['SUB_SECTORSxSECTOR'].append({
                    'SUBSECTOR_ID': subsector.SUBSECTOR_ID,
                    'SUBSECTOR': subsector.SUBSECTOR
                })
            return json_data
        except Exception as e:
            print("--------------------------------------------------------------------")
            print("FormattedPlace - formated_specific_sector | Error: ", e)
            print("--------------------------------------------------------------------")
            return jsonify({'Error': str(e)})
