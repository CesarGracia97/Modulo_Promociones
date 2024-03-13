from flask import Flask
from Controller.BackEndpointController import backp_bp
from Controller.FrontEndpointController import combp_bp, oferp_bp, servp_bp, tecnp_bp, tisep_bp, planp_bp


def create_app():
    _app = Flask(__name__)
    _app.register_blueprint(combp_bp)
    _app.register_blueprint(oferp_bp)
    _app.register_blueprint(servp_bp)
    _app.register_blueprint(tecnp_bp)
    _app.register_blueprint(tisep_bp)
    _app.register_blueprint(planp_bp)
    _app.register_blueprint(backp_bp)

    return _app


if __name__ == '__main__':
    app = create_app()

    # Inicia el servidor de desarrollo
    app.run(port=5013)
