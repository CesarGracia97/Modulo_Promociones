from flask import Blueprint, request, jsonify, current_app
from config.config import config
from resources.GeneratorToken import GeneratorToken

postTo_bp = Blueprint('rapi_postTo_POST', __name__)
postBd_bp = Blueprint('rapi_postBd_POST', __name__)
__URLToken__ = config.get('URL', 'URL_POST_TOKEN')
__URLBD__ = config.get('URL', 'URL_POST_BD')


class POST_EndpointController:
    def __init__(self):
        self.__KEY = config.get('TOKER', 'TOKEN_IDP')

    @postTo_bp.route(__URLToken__, methods=['POST'])
    def postToken_endpoint():
        controller = POST_EndpointController()
        try:
            authorization_header = request.headers.get('Authorization')
            if authorization_header and authorization_header.startswith('Bearer '):
                token = authorization_header.split('Bearer ')[1]

                request_data = request.get_json()
                if request_data and 'key' in request_data and request_data['key'] == controller.__KEY:
                    print("Get Token")
                    new_token = GeneratorToken.generate_token()

                    # Almacenar el nuevo token en la cache global
                    config.set(new_token, 'TOKER', 'TOKEN_GEN')

                    print("Respuesta Enviada")
                    return jsonify({'token': new_token}), 200
                else:
                    return jsonify({'error': 'Clave incorrecta'}), 400
            else:
                return jsonify({'error': 'Token de autorización no válido'}), 401
        except Exception as e:
            print("--------------------------------------------------------------------")
            print("postToken_endpoint - Error Encontrado")
            print(e)
            print("--------------------------------------------------------------------")

    @postBd_bp.route(__URLBD__, methods=['POST'])
    def postBd_endpoint():
        try:
            print()
        except Exception as e:
            print(e)
