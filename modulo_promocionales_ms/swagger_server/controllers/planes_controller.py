import connexion
import six

from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.request_get_planes import RequestGetPlanes  # noqa: E501
from swagger_server.models.response_error import ResponseError  # noqa: E501
from swagger_server import util


def get_planes(body=None):  # noqa: E501
    """get_planes

    Consulta de Datos de Provincias segun sus parametros. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse200
    """
    if connexion.request.is_json:
        body = RequestGetPlanes.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
