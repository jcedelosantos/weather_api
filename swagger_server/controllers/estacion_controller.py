import connexion
import six

# Objeto que permite transformar las primitivas de python en JSON
from swagger_server.models.medicion import Medicion  # noqa: E501
from swagger_server import util
# Objeto que permite operar con la tabla de la BD
from swagger_server.sqlalchemy_models import Medicion as Med
from swagger_server import db
# Registro del log del sistema
import logging
logging.basicConfig(format='%(levelname)s:[%(filename)s:%(lineno)s - %(funcName)20s() ]:%(message)s', level=logging.INFO)

def estacion_post(body):  # noqa: E501
    """Registra los valores de telemetría de una estación de medición del tiempo.

     # noqa: E501

    :param body: mediciones del equipo en formato JSON
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Medicion.from_dict(connexion.request.get_json())  # noqa: E501
    # Transformamos el objeto Medicion, hacia un diccionario de python.
    data_dict = body.to_dict()
    data_dict['idHardware'] = data_dict['id_hardware']
    data_dict['presionBar'] = data_dict['presion_bar']
    data_dict.pop('id_hardware')
    data_dict.pop('presion_bar')
    # logging.info(data_dict)
    # return "DEBUG", 200
    
    # 
    data_sensor = Med(**data_dict)
    db.session.add(data_sensor)
    db.session.commit()


    return "DEBUG", 200
