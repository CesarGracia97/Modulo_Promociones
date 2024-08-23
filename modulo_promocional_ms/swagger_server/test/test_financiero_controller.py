# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.inline_response2002 import InlineResponse2002  # noqa: E501
from swagger_server.models.request_get_financiero import RequestGetFinanciero  # noqa: E501
from swagger_server.models.response_error import ResponseError  # noqa: E501
from swagger_server.test import BaseTestCase


class TestFinancieroController(BaseTestCase):
    """FinancieroController integration test stubs"""

    def test_get_financiero(self):
        """Test case for get_financiero

        
        """
        body = RequestGetFinanciero()
        response = self.client.open(
            '/get/Financiero',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
