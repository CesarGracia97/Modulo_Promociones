#!/usr/bin/env python3
import connexion
from connexion.resolver import MethodViewResolver
from swagger_server import encoder
from flask_cors import CORS  # <--- Importa CORS


def create_app():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    CORS(app.app)  # <--- Activa CORS en la aplicación Flask
    app.add_api('swagger.yaml', arguments={'title': 'Api for modulo-promocionales-api'}, pythonic_params=True,
                resolver=MethodViewResolver("swagger_server.controllers"))
    return app


if __name__ == '__main__':
    app = create_app()
    # app.run(port=8080) #Desa
    app.run(port=2014, debug=False)  # Pre