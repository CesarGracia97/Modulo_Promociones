from flask import Flask
from flask_cors import CORS

from controllers.BackEndpointController import backp_bp
from controllers.FinanceEndpointController import burop_bp, mpagp_bp, dtpro_bp
from controllers.FrontEndpointController import provp_bp, cityp_bp, sectp_bp, infmv_bp
from controllers.PlanesEndpointController import combp_bp, servp_bp, oferp_bp, planp_bp
from controllers.PostEndpointController import postp_bp


def create_app():
    app = Flask(__name__)
    print("---------------------------------")
    print("MODULOS PROMOCIONALES REST API")
    print("---------------------------------")

    # ---------------------------------- # FrontEndpoint / Lugares (Places)
    app.register_blueprint(provp_bp)
    app.register_blueprint(cityp_bp)
    app.register_blueprint(sectp_bp)
    app.register_blueprint(infmv_bp)
    app.register_blueprint(postp_bp)
    # ---------------------------------- # FrontEndpoint / Planes
    app.register_blueprint(oferp_bp)
    app.register_blueprint(servp_bp)
    app.register_blueprint(combp_bp)
    app.register_blueprint(planp_bp)
    # ---------------------------------- # FrontEndpoint / Finanzas
    app.register_blueprint(burop_bp)
    app.register_blueprint(mpagp_bp)
    app.register_blueprint(dtpro_bp)
    # ---------------------------------- # BackEnpoint
    app.register_blueprint(backp_bp)

    CORS(app)

    return app


if __name__ == '__main__':
    app = create_app()

    # Inicia el servidor de desarrollo
    app.run(port=5012)
