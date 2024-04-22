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
