from flask import Blueprint, request, jsonify, current_app

from resources.GeneratorToken import GeneratorToken

postTo_bp = Blueprint('rapi_postTo_POST', __name__)
postBd_bp = Blueprint('rapi_postBd_POST', __name__)
__URLToken__ = '/rest/token-api/v1.0/generate'
__URLBD__ = '/rest/postdata-modulos-promocionales-api/v1.0/injection'
EXPECTED_KEY = 'eGLXpAqYGYucR7sBfDR1E4h4fe6mpq0RSaoUpQ4jkppvwzFBQf0YqRrfuDvaCkIrvRiZ4gBa2HO9l9lfLR4qcBprRRqhJHZ'


class POST_EndpointController:
    @postTo_bp.route(__URLToken__, methods=['POST'])
    def postToken_endpoint():
        try:
            authorization_header = request.headers.get('Authorization')
            if authorization_header and authorization_header.startswith('Bearer '):
                token = authorization_header.split('Bearer ')[1]

                request_data = request.get_json()
                if request_data and 'key' in request_data and request_data['key'] == EXPECTED_KEY:
                    print("Get Token")
                    new_token = GeneratorToken.generate_token()

                    # Almacenar el nuevo token en la cache global
                    # current_app.cache.set('new_token', new_token)
                    cache = current_app.extensions['cache']
                    cache.set('new_token', new_token)

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
