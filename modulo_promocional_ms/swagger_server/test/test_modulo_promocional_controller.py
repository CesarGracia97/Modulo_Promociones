# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.resquest_post_diccionario_datos import ResquestPostDiccionarioDatos  # noqa: E501
from swagger_server.test import BaseTestCase


class TestModuloPromocionalController(BaseTestCase):
    """ModuloPromocionalController integration test stubs"""

    def test_get_modulo_promocional(self):
        """Test case for get_modulo_promocional

        
        """
        body = ResquestPostDiccionarioDatos()
        response = self.client.open(
            '/post/modulo-promocional',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
