import connexion
import six

from swagger_server.models.response_error import ResponseError  # noqa: E501
from swagger_server.models.response_post_diccionario_datos_data import ResponsePostDiccionarioDatosData  # noqa: E501
from swagger_server.models.resquest_post_diccionario_datos import ResquestPostDiccionarioDatos  # noqa: E501
from swagger_server import util


def post_modulopromocional(body=None):  # noqa: E501
    """post_modulopromocional
    Envio de Datos a Base de Datos # noqa: E501
    """
    if connexion.request.is_json:
        body = ResquestPostDiccionarioDatos.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
