from flask import Flask
from Resources.database.connection import connection
from Controllers.PeticionPlacesController import receptor_bplc
from Controllers.PeticionPlanesController import receptor_bpln


def create_app():
    # Crea la aplicación Flask
    app = Flask(__name__)

    # Configuración
    # app.config.from_pyfile('config.py')  # Considera tener un archivo de configuración separado

    # Conexión a la base de datos
    oracle_db = connection()
    if oracle_db.connect():
        # Registro de blueprints
        app.register_blueprint(receptor_bplc)
        app.register_blueprint(receptor_bpln)

    return app

if __name__ == '__main__':
    # Crea la aplicación
    app = create_app()

    # Inicia el servidor de desarrollo
    app.run(host='127.0.0.1', port=5011)
