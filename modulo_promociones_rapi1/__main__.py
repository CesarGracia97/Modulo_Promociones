from flask import Flask
from flask_cors import CORS

from controllers.BackEndpointController import backp_bp
from controllers.FrontEndpointController import provp_bp, cityp_bp, sectp_bp, ssecp_bp, infmv_bp


def create_app():
    app = Flask(__name__)
    print("---------------------------------")
    print("Rest Api1 - PLACE")
    print("---------------------------------")
    app.register_blueprint(backp_bp)
    app.register_blueprint(provp_bp)
    app.register_blueprint(cityp_bp)
    app.register_blueprint(sectp_bp)
    app.register_blueprint(ssecp_bp)
    app.register_blueprint(infmv_bp)
    CORS(app)

    return app


if __name__ == '__main__':
    app = create_app()

    # Inicia el servidor de desarrollo
    app.run(port=5012)
