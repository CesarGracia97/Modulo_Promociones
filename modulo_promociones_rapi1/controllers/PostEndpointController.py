from flask import Blueprint

postp_bp = Blueprint('rapi_postp_POST', __name__)


class PostEndpointController:
    @postp_bp.route('/api/ra/postp_endpoint', methods=['POST'])
    def postendpoint():
        try:
            print()
        except Exception as e:
            print(e)
