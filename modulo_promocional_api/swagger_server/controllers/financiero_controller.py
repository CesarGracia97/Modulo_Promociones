import connexion
import six

from swagger_server.models.request_get_buro import RequestGetBuro  # noqa: E501
from swagger_server.models.request_get_dias_gozados import RequestGetDiasGozados  # noqa: E501
from swagger_server.models.request_get_formas_pago import RequestGetFormasPago  # noqa: E501
from swagger_server.models.request_get_precio_regular import RequestGetPrecioRegular  # noqa: E501
from swagger_server.models.request_get_upgrade import RequestGetUpgrade  # noqa: E501
from swagger_server.models.response_error import ResponseError  # noqa: E501
from swagger_server.models.response_get_buro_data import ResponseGetBuroData  # noqa: E501
from swagger_server.models.response_get_dias_gozados_data import ResponseGetDiasGozadosData  # noqa: E501
from swagger_server.models.response_get_formas_pago_data import ResponseGetFormasPagoData  # noqa: E501
from swagger_server.models.response_get_precio_regular_data import ResponseGetPrecioRegularData  # noqa: E501
from swagger_server.models.response_get_upgrade_data import ResponseGetUpgradeData  # noqa: E501
from swagger_server import util


params_financiero = {
    'channel': 'api-modulos-promocionales-financiero'
}


def get_buro(body=None):  # noqa: E501
    """get_buro
    Consulta de Buro # noqa: E501
    """
    if connexion.request.is_json:
        body = RequestGetBuro.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_diasgozados(body=None):  # noqa: E501
    """get_diasgozados
    Consulta de Dias Gozados # noqa: E501
    """
    if connexion.request.is_json:
        body = RequestGetDiasGozados.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_modospago(body=None):  # noqa: E501
    """get_modospago
    Consulta de Modos de Pago # noqa: E501
    """
    if connexion.request.is_json:
        body = RequestGetFormasPago.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_precioregular(body=None):  # noqa: E501
    """get_precioregular
    Consulta de Precios de Productos # noqa: E501}
    """
    if connexion.request.is_json:
        body = RequestGetPrecioRegular.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_upgrade(body=None):  # noqa: E501
    """get_upgrade
    Consulta de Datos Upgrade # noqa: E501
    """
    if connexion.request.is_json:
        body = RequestGetUpgrade.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
