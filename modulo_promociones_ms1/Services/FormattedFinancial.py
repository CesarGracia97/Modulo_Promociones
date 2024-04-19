from flask import jsonify


class FormattedFinance:
    @staticmethod
    def formatted_buro(data):
        try:
            return json_data
        except Exception as e:
            print("--------------------------------------------------------------------")
            print("FormattedFinance - formatted_buro | Error: ", e)
            print("--------------------------------------------------------------------")
            return jsonify({'Error': str(e)})

    @staticmethod
    def formatted_mpagos(data):
        try:
            return json_data
        except Exception as e:
            print("--------------------------------------------------------------------")
            print("FormattedFinance - formatted_mpagos | Error: ", e)
            print("--------------------------------------------------------------------")
            return jsonify({'Error': str(e)})
