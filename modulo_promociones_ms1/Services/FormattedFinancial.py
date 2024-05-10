from flask import jsonify


class FormattedFinance:
    @staticmethod
    def formatted_buro(data):
        try:
            json_data = {
                'BURO': []
            }
            for buro in data['BURO']:
                json_data['BURO'].append({
                    'ID': buro.ID,
                    'NAME': buro.NAME
                })
            return json_data
        except Exception as e:
            print("--------------------------------------------------------------------")
            print("FormattedFinance - formatted_buro | Error: ", e)
            print("--------------------------------------------------------------------")
            return jsonify({'Error': str(e)})

    @staticmethod
    def formatted_mpagos(data):
        try:
            json_data = {
                'MPAGOS': []
            }
            for mpagos in data['MPAGOS']:
                json_data['MPAGOS'].append({
                    'ID': mpagos.ID,
                    'NAME': mpagos.NAME
                })
            return json_data
        except Exception as e:
            print("--------------------------------------------------------------------")
            print("FormattedFinance - formatted_mpagos | Error: ", e)
            print("--------------------------------------------------------------------")
            return jsonify({'Error': str(e)})

    @staticmethod
    def formatted_dgozados(data):
        try:
            json_data = {
                'DIAS_GOZADOS': []
            }
            for dt in data['DIAS_GOZADOS']:
                json_data['DIAS_GOZADOS'].append({
                    'ID': dt.ID,
                    'NAME': dt.NAME
                })
            return json_data
        except Exception as e:
            print("--------------------------------------------------------------------")
            print("FormattedFinance - formatted_dgozados | Error: ", e)
            print("--------------------------------------------------------------------")
            return jsonify({'Error': str(e)})

    @staticmethod
    def formatted_pregular(data):
        try:
            json_data = {
                'PRECIO_REGULAR': []
            }
            for dt in data['PRECIO_REGULAR']:
                json_data['PRECIO_REGULAR'].append({
                    'ID': dt.ID,
                    'PRECIO': dt.PRECIO
                })
            return json_data
        except Exception as e:
            print("--------------------------------------------------------------------")
            print("FormattedFinance - formatted_pregular | Error: ", e)
            print("--------------------------------------------------------------------")
            return jsonify({'Error': str(e)})

    @staticmethod
    def formatted_upgrade(data):
        try:
            json_data = {
                'UPGRADE': []
            }
            for dt in data['UPGRADE']:
                json_data['UPGRADE'].append({
                    'ID': dt.ID,
                    'NAME': dt.NAME
                })
            return json_data
        except Exception as e:
            print("--------------------------------------------------------------------")
            print("FormattedFinance - formatted_upgrade | Error: ", e)
            print("--------------------------------------------------------------------")
            return jsonify({'Error': str(e)})
