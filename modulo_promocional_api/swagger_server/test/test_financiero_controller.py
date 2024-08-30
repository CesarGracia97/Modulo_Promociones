# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

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
from swagger_server.test import BaseTestCase


class TestFinancieroController(BaseTestCase):
    """FinancieroController integration test stubs"""

    def test_get_buro(self):
        """Test case for get_buro

        
        """
        body = RequestGetBuro()
        response = self.client.open(
            '/get/finance/buro',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_diasgozados(self):
        """Test case for get_diasgozados

        
        """
        body = RequestGetDiasGozados()
        response = self.client.open(
            '/get/finance/dias-gozados',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_modospago(self):
        """Test case for get_modospago

        
        """
        body = RequestGetFormasPago()
        response = self.client.open(
            '/get/finance/modos-pago',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_precioregular(self):
        """Test case for get_precioregular

        
        """
        body = RequestGetPrecioRegular()
        response = self.client.open(
            '/get/finance/precio-regular',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_upgrade(self):
        """Test case for get_upgrade

        
        """
        body = RequestGetUpgrade()
        response = self.client.open(
            '/get/finance/upgrade',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
