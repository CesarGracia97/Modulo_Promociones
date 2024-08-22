#!/usr/bin/env python3

import connexion
from connexion.resolver import MethodViewResolver
from swagger_server import encoder


def create_app():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Microservices for modulo-promocionales-ms'}, pythonic_params=True,
                resolver=MethodViewResolver("swagger_server.controllers"))
    return app


if __name__ == '__main__':
    app = create_app()
    # app.run(port=8080) #Desa
    app.run(port=2013, debug=False)  # Pre
