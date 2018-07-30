import os
import connexion
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy 
from swagger_server import encoder

# Vinculamos la aplicación de Flask con la especificación de Swagger
app = connexion.App(__name__, specification_dir='./swagger/')
# Variable de SQL Server
db = SQLAlchemy()

def create_app():
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'API Weather Station Project'})
    # Driver de conexión a la BD
    app.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clima.db'
    # Habilitamos el soporte CORS
    CORS(app.app)
    # Habilitamos el soporte de la BD
    db.init_app(app.app)
    # Puerto de ejecución de la aplicación
    app.run(port=8080)