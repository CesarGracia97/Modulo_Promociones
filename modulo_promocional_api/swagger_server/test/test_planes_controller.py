# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.request_get_combos import RequestGetCombos  # noqa: E501
from swagger_server.models.request_get_ofertas import RequestGetOfertas  # noqa: E501
from swagger_server.models.request_get_planes import RequestGetPlanes  # noqa: E501
from swagger_server.models.request_get_servicios import RequestGetServicios  # noqa: E501
from swagger_server.models.response_combos_data import ResponseCombosData  # noqa: E501
from swagger_server.models.response_error import ResponseError  # noqa: E501
from swagger_server.models.response_get_planes_data import ResponseGetPlanesData  # noqa: E501
from swagger_server.models.response_ofertas_data import ResponseOfertasData  # noqa: E501
from swagger_server.models.response_servicios_data import ResponseServiciosData  # noqa: E501
from swagger_server.test import BaseTestCase


class TestPlanesController(BaseTestCase):
    """PlanesController integration test stubs"""

    def test_get_combos(self):
        """Test case for get_combos

        
        """
        body = RequestGetCombos()
        response = self.client.open(
            '/get/planes/combos',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_ofertas(self):
        """Test case for get_ofertas

        
        """
        body = RequestGetOfertas()
        response = self.client.open(
            '/get/planes/ofertas',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_planes(self):
        """Test case for get_planes

        
        """
        body = RequestGetPlanes()
        response = self.client.open(
            '/get/planes/planes',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_servicios(self):
        """Test case for get_servicios

        
        """
        body = RequestGetServicios()
        response = self.client.open(
            '/get/planes/servicios',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
