from flask import Blueprint

postp_bp = Blueprint('rapi_postp_POST', __name__)
__URL__ = 'rest/postdata-modulos-promocionales-api/v1.0/injection'


class PostEndpointController:
    @postp_bp.route(__URL__, methods=['POST'])
    def postendpoint():
        try:
            print()
        except Exception as e:
            print(e)
