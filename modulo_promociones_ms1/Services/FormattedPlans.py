from flask import jsonify


class FormattedPlans:
    @staticmethod
    def formated_ADOferta(data):
        try:
            json_data = {
                'OFERTAS': []
            }
            for oferta in data['OFERTAS']:
                json_data['OFERTAS'].append({
                    'OFERTA_ID': oferta.OFERTA_ID,
                    'OFERTA': oferta.OFERTA
                })
            return json_data
        except Exception as e:
            print("--------------------------------------------------------------------")
            print("FormattedPlans - formated_ADOferta | Error: ", e)
            print("--------------------------------------------------------------------")
            return jsonify({'Error': str(e)})

    @staticmethod
    def formated_ADServicio(data):
        try:
            json_data = {
                'SERVICIOS': []
            }
            for servicio in data['SERVICIOS']:
                json_data['SERVICIOS'].append({
                    'SERVICIO': servicio.SERVICIO
                })
            return json_data
        except Exception as e:
            print("--------------------------------------------------------------------")
            print("FormattedPlans - formated_ADServicio | Error: ", e)
            print("--------------------------------------------------------------------")
            return jsonify({'Error': str(e)})

    @staticmethod
    def formated_ADTecnologia(data):
        try:
            json_data = {
                'TECNOLOGIAS': []
            }
            for tecnologia in data['TECNOLOGIAS']:
                json_data['TECNOLOGIAS'].append({
                    'TECNOLOGIA': tecnologia.TECNOLOGIA
                })
            return json_data
        except Exception as e:
            print("--------------------------------------------------------------------")
            print("FormattedPlans - formated_ADTecnologia | Error: ", e)
            print("--------------------------------------------------------------------")
            return jsonify({'Error': str(e)})

    @staticmethod
    def formated_ADTipoServicio(data):
        try:
            json_data = {
                'TIPO_SERVICIO': []
            }
            for tipotecnologia in data['TIPO_SERVICIO']:
                json_data['TIPO_SERVICIO'].append({
                    'TIPO_SERVICIO': tipotecnologia.TIPO_SERVICIO
                })
            return json_data
        except Exception as e:
            print("--------------------------------------------------------------------")
            print("FormattedPlans - formated_ADTipoServicio | Error: ", e)
            print("--------------------------------------------------------------------")
            return jsonify({'Error': str(e)})

    @staticmethod
    def formated_ADPlan(data, opcion):
        try:
            json_data = {
                'PLANES': []
            }
            if opcion == 1:
                for plan in data['PLANES']:
                    json_data['PLANES'].append({
                        'TARIFFPLANID': plan.TARIFFPLANID,
                        'TARIFFPLAN': plan.TARIFFPLAN
                    })
                return json_data
            elif opcion == 2:
                for plan in data['PLANES']:
                    json_data['PLANES'].append({
                        'TARIFFPLANVARIANTID': plan.TARIFFPLANVARIANTID,
                        'TARIFFPLANVARIANT': plan.TARIFFPLANVARIANT
                    })
                return json_data
            elif opcion == 3:
                for plan in data['PLANES']:
                    json_data['PLANES'].append({
                        'TARIFFPLANID': plan.TARIFFPLANID,
                        'TARIFFPLAN': plan.TARIFFPLAN,
                        'TARIFFPLANVARIANTID': plan.TARIFFPLANVARIANTID,
                        'TARIFFPLANVARIANT': plan.TARIFFPLANVARIANT
                    })
                return json_data
        except Exception as e:
            print("--------------------------------------------------------------------")
            print("FormattedPlans - formated_ADPlan | Error: ", e)
            print("--------------------------------------------------------------------")
            return jsonify({'Error': str(e)})

    @staticmethod
    def formated_COPlan(data):
        try:
            json_data = {
                'COMBO_PLAN': []
            }
            for plan in data['COMBO_PLAN']:
                json_data['COMBO_PLAN'].append({
                    'TARIFFPLANID': plan.TARIFFPLANID,
                    'TARIFFPLAN': plan.TARIFFPLAN
                })
            return json_data
        except Exception as e:
            print("--------------------------------------------------------------------")
            print("FormattedPlanes - formated_COPlan | Error: ", e)
            print("--------------------------------------------------------------------")
            return jsonify({'Error': str(e)})

    @staticmethod
    def formated_COPlanVariant(data):
        try:
            json_data = {
                'COMBO_PLANVARIANT': []
            }
            for plan in data['COMBO_PLANVARIANT']:
                json_data['COMBO_PLANVARIANT'].append({
                    'TARIFFPLANVARIANTID': plan.TARIFFPLANVARIANTID,
                    'TARIFFPLANVARIANT': plan.TARIFFPLANVARIANT
                })
            return json_data
        except Exception as e:
            print("--------------------------------------------------------------------")
            print("FormattedPlanes - formated_COPlanVariant | Error: ", e)
            print("--------------------------------------------------------------------")
            return jsonify({'Error': str(e)})

    @staticmethod
    def formated_COProducto(data):
        try:
            json_data = {
                'COMBO_PRODUCTO': []
            }
            for producto in data['COMBO_PRODUCTO']:
                json_data['COMBO_PRODUCTO'].append({
                    'PRODUCTID': producto.PRODUCTID,
                    'PRODUCTO': producto.PRODUCTO
                })
            return json_data
        except Exception as e:
            print("--------------------------------------------------------------------")
            print("FormattedPlanes - formated_COProducto | Error: ", e)
            print("--------------------------------------------------------------------")
            return jsonify({'Error': str(e)})

    @staticmethod
    def formated_COTipoServicio(data):
        try:
            json_data = {
                'COMBO_TIPO_SERVICIO': []
            }
            for tiposervicio in data['COMBO_TIPO_SERVICIO']:
                json_data['COMBO_TIPO_SERVICIO'].append({
                    'TIPO_SERVICIO': tiposervicio.TIPO_SERVICIO
                })
            return json_data
        except Exception as e:
            print("--------------------------------------------------------------------")
            print("FormattedPlans - formated_COTipoServicio | Error: ", e)
            print("--------------------------------------------------------------------")
            return jsonify({'Error': str(e)})

    @staticmethod
    def formated_COProvincia(data):
        try:
            json_data = {
                'C_PROVINCIA': []
            }
            for provincia in data['C_PROVINCIA']:
                json_data['C_PROVINCIA'].append({
                    'PROVINCIA_ID': provincia.PROVINCIA_ID,
                    'PROVINCIA': provincia.PROVINCIA
                })
            return json_data
        except Exception as e:
            print("--------------------------------------------------------------------")
            print("FormattedPlanes - formated_COProvincia | Error: ", e)
            print("--------------------------------------------------------------------")
            return jsonify({'Error': str(e)})

    @staticmethod
    def formated_COCiudad(data):
        try:
            json_data = {
                'C_CIUDAD': []
            }
            for ciudad in data['C_CIUDAD']:
                json_data['C_CIUDAD'].append({
                    'CIUDAD_ID': ciudad.CIUDAD_ID,
                    'PROVINCIA': ciudad.PROVINCIA,
                    'CIUDAD': ciudad.CIUDAD
                })
            return json_data
        except Exception as e:
            print("--------------------------------------------------------------------")
            print("FormattedPlanes - formated_COCiudad | Error: ", e)
            print("--------------------------------------------------------------------")
            return jsonify({'Error': str(e)})

    @staticmethod
    def formated_COSector(data):
        try:
            json_data = {
                'C_SECTOR': []
            }
            for sector in data['C_SECTOR']:
                json_data['C_SECTOR'].append({
                    'SECTOR_ID': sector.SECTOR_ID,
                    'CIUDAD': sector.CIUDAD,
                    'SECTOR': sector.SECTOR
                })
            return json_data
        except Exception as e:
            print("--------------------------------------------------------------------")
            print("FormattedPlanes - formated_COSector | Error: ", e)
            print("--------------------------------------------------------------------")
            return jsonify({'Error': str(e)})
