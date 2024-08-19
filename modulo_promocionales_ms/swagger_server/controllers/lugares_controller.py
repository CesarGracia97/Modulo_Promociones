import connexion
import six

from swagger_server.models.inline_response2001 import InlineResponse2001  # noqa: E501
from swagger_server.models.request_get_lugares import RequestGetLugares  # noqa: E501
from swagger_server.models.response_error import ResponseError  # noqa: E501
from swagger_server import util


def get_lugares(body=None):  # noqa: E501
    """get_lugares

    Consulta de Datos de Provincias segun sus parametros. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse2001
    """
    if connexion.request.is_json:
        body = RequestGetLugares.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
