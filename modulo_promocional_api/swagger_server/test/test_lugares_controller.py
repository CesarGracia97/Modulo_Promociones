# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.request_get_ciudades import RequestGetCiudades  # noqa: E501
from swagger_server.models.request_get_provincia import RequestGetProvincia  # noqa: E501
from swagger_server.models.request_get_sectores import RequestGetSectores  # noqa: E501
from swagger_server.models.response_error import ResponseError  # noqa: E501
from swagger_server.models.response_get_ciudad_data import ResponseGetCiudadData  # noqa: E501
from swagger_server.models.response_get_provincia_data import ResponseGetProvinciaData  # noqa: E501
from swagger_server.models.response_get_sectores_data import ResponseGetSectoresData  # noqa: E501
from swagger_server.test import BaseTestCase


class TestLugaresController(BaseTestCase):
    """LugaresController integration test stubs"""

    def test_get_ciudades(self):
        """Test case for get_ciudades

        
        """
        body = RequestGetCiudades()
        response = self.client.open(
            '/get/lugares/ciudades',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_provincias(self):
        """Test case for get_provincias

        
        """
        body = RequestGetProvincia()
        response = self.client.open(
            '/get/lugares/provincias',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_sectores(self):
        """Test case for get_sectores

        
        """
        body = RequestGetSectores()
        response = self.client.open(
            '/get/lugares/sectores',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
