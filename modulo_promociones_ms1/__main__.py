from flask import Flask

from Controllers.InjectionPostController import receptor_bpost
from Resources.database.connection import connection
from Controllers.PeticionPlacesController import receptor_bplc
from Controllers.PeticionPlanesController import receptor_bpln
from Controllers.PeticionFinanController import receptor_bfinan


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
        app.register_blueprint(receptor_bfinan)
        app.register_blueprint(receptor_bpost)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(port=5011)
