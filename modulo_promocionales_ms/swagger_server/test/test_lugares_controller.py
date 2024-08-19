# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.inline_response2001 import InlineResponse2001  # noqa: E501
from swagger_server.models.request_get_lugares import RequestGetLugares  # noqa: E501
from swagger_server.models.response_error import ResponseError  # noqa: E501
from swagger_server.test import BaseTestCase


class TestLugaresController(BaseTestCase):
    """LugaresController integration test stubs"""

    def test_get_lugares(self):
        """Test case for get_lugares

        
        """
        body = RequestGetLugares()
        response = self.client.open(
            '/get/Lugares',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
