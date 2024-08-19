# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.request_get_planes import RequestGetPlanes  # noqa: E501
from swagger_server.models.response_error import ResponseError  # noqa: E501
from swagger_server.test import BaseTestCase


class TestPlanesController(BaseTestCase):
    """PlanesController integration test stubs"""

    def test_get_planes(self):
        """Test case for get_planes

        
        """
        body = RequestGetPlanes()
        response = self.client.open(
            '/get/Planes',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
