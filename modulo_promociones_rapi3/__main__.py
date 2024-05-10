from flask import Flask
from flask_cors import CORS

from Controller.FrontEnpointController import burop_bp, mpagp_bp, dtpro_bp
from Controller.BackEndpointController import backp_bp


def create_app():
    app = Flask(__name__)
    print("---------------------------------")
    print("Rest Api3 - Finance")
    print("---------------------------------")
    app.register_blueprint(burop_bp)
    app.register_blueprint(mpagp_bp)
    app.register_blueprint(backp_bp)
    app.register_blueprint(dtpro_bp)

    CORS(app)

    return app


if __name__ == '__main__':
    app = create_app()

    # Inicia el servidor de desarrollo
    app.run(port=5014)
