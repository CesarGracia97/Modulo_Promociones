import connexion
import six

from swagger_server.models.inline_response2002 import InlineResponse2002  # noqa: E501
from swagger_server.models.request_get_financiero import RequestGetFinanciero  # noqa: E501
from swagger_server.models.response_error import ResponseError  # noqa: E501
from swagger_server import util


def get_financiero(body=None):  # noqa: E501
    """get_financiero

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse2002
    """
    if connexion.request.is_json:
        body = RequestGetFinanciero.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
