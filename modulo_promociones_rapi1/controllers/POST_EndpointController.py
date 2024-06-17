from flask import Blueprint, request, jsonify
from config.config import config
from resources.GeneratorToken import GeneratorToken

postBd_bp = Blueprint('rapi_postBd_POST', __name__)
__URLBD__ = config.get('URL', 'URL_POST_BD')


class POST_EndpointController:

    @postBd_bp.route(__URLBD__, methods=['POST'])
    def postBd_endpoint():
        try:
            print("---------------------------------------------------")
            print("POST - POST INJECCION")
            print("---------------------------------------------------")

        except Exception as e:
            print("--------------------------------------------------------------------")
            print("postBd_endpoint - Error Encontrado")
            print(e)
            print("--------------------------------------------------------------------")
