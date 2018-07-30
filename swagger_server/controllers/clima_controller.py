import connexion
import six

# Objeto que permite operar con la tabla de la BD
from swagger_server import db
from swagger_server.models.medicion import Medicion  # noqa: E501
# Tabla de SQLAlchemy de las mediciones
from swagger_server.sqlalchemy_models import Medicion as Med
from swagger_server import util
# Registro del log del sistema
import logging
logging.basicConfig(format='%(levelname)s:[%(filename)s:%(lineno)s - %(funcName)20s() ]:%(message)s', level=logging.INFO)


def clima_id_estacion_get(idEstacion, inicio=None, fin=None, sensor=None):  # noqa: E501
    """Devuelve los valores medidos mas reciente, de una estación.

     # noqa: E501

    :param idEstacion: Id del hardware del equipo de medición.
    :type idEstacion: str
    :param inicio: fecha de inicio de la medición.
    :type inicio: str
    :param fin: fecha de fin de la medición.
    :type fin: str
    :param sensor: nombre del sensor sobre el cual queremos obtener información.
    :type sensor: List[str]

    :rtype: List[Medicion]
    """
    inicio = util.deserialize_datetime(inicio)
    fin = util.deserialize_datetime(fin)
    # Variable de salida
    res = list()
    try:
        # Obtenemos el listado de los registros de la estación consultada
        consulta = Med.query.filter_by(hardware=idEstacion).all()

        # Recorremos los resultados de la consulta.
        for fila in consulta:
            # Llenamos el JSON basado en la data de la fila 
            f = fila.__dict__
            f.pop('_sa_instance_state')
            # Agregamos la medición al vector de salida
            res.append(f)        
    except Exception as e:
        return "Error inesperado. Detalles [{0}]".format(e), 500

    return res, 200
