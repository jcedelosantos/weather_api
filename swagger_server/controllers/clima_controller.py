import connexion
import six

from swagger_server.models.medicion import Medicion  # noqa: E501
from swagger_server import util


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
    return 'do some magic!'
