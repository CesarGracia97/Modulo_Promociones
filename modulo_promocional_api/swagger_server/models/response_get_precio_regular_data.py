# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.response_get_precio_regular_data_precioregular import ResponseGetPrecioRegularDataPRECIOREGULAR  # noqa: F401,E501
from swagger_server import util


class ResponseGetPrecioRegularData(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, error_code: int=None, internal_transaction_id: str=None, external_transaction_id: str=None, message: str=None, precio_regular: ResponseGetPrecioRegularDataPRECIOREGULAR=None):  # noqa: E501
        """ResponseGetPrecioRegularData - a model defined in Swagger

        :param error_code: The error_code of this ResponseGetPrecioRegularData.  # noqa: E501
        :type error_code: int
        :param internal_transaction_id: The internal_transaction_id of this ResponseGetPrecioRegularData.  # noqa: E501
        :type internal_transaction_id: str
        :param external_transaction_id: The external_transaction_id of this ResponseGetPrecioRegularData.  # noqa: E501
        :type external_transaction_id: str
        :param message: The message of this ResponseGetPrecioRegularData.  # noqa: E501
        :type message: str
        :param precio_regular: The precio_regular of this ResponseGetPrecioRegularData.  # noqa: E501
        :type precio_regular: ResponseGetPrecioRegularDataPRECIOREGULAR
        """
        self.swagger_types = {
            'error_code': int,
            'internal_transaction_id': str,
            'external_transaction_id': str,
            'message': str,
            'precio_regular': ResponseGetPrecioRegularDataPRECIOREGULAR
        }

        self.attribute_map = {
            'error_code': 'errorCode',
            'internal_transaction_id': 'internalTransactionId',
            'external_transaction_id': 'externalTransactionId',
            'message': 'message',
            'precio_regular': 'PRECIO_REGULAR'
        }
        self._error_code = error_code
        self._internal_transaction_id = internal_transaction_id
        self._external_transaction_id = external_transaction_id
        self._message = message
        self._precio_regular = precio_regular

    @classmethod
    def from_dict(cls, dikt) -> 'ResponseGetPrecioRegularData':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ResponseGetPrecioRegular_data of this ResponseGetPrecioRegularData.  # noqa: E501
        :rtype: ResponseGetPrecioRegularData
        """
        return util.deserialize_model(dikt, cls)

    @property
    def error_code(self) -> int:
        """Gets the error_code of this ResponseGetPrecioRegularData.


        :return: The error_code of this ResponseGetPrecioRegularData.
        :rtype: int
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code: int):
        """Sets the error_code of this ResponseGetPrecioRegularData.


        :param error_code: The error_code of this ResponseGetPrecioRegularData.
        :type error_code: int
        """

        self._error_code = error_code

    @property
    def internal_transaction_id(self) -> str:
        """Gets the internal_transaction_id of this ResponseGetPrecioRegularData.


        :return: The internal_transaction_id of this ResponseGetPrecioRegularData.
        :rtype: str
        """
        return self._internal_transaction_id

    @internal_transaction_id.setter
    def internal_transaction_id(self, internal_transaction_id: str):
        """Sets the internal_transaction_id of this ResponseGetPrecioRegularData.


        :param internal_transaction_id: The internal_transaction_id of this ResponseGetPrecioRegularData.
        :type internal_transaction_id: str
        """

        self._internal_transaction_id = internal_transaction_id

    @property
    def external_transaction_id(self) -> str:
        """Gets the external_transaction_id of this ResponseGetPrecioRegularData.


        :return: The external_transaction_id of this ResponseGetPrecioRegularData.
        :rtype: str
        """
        return self._external_transaction_id

    @external_transaction_id.setter
    def external_transaction_id(self, external_transaction_id: str):
        """Sets the external_transaction_id of this ResponseGetPrecioRegularData.


        :param external_transaction_id: The external_transaction_id of this ResponseGetPrecioRegularData.
        :type external_transaction_id: str
        """

        self._external_transaction_id = external_transaction_id

    @property
    def message(self) -> str:
        """Gets the message of this ResponseGetPrecioRegularData.


        :return: The message of this ResponseGetPrecioRegularData.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message: str):
        """Sets the message of this ResponseGetPrecioRegularData.


        :param message: The message of this ResponseGetPrecioRegularData.
        :type message: str
        """

        self._message = message

    @property
    def precio_regular(self) -> ResponseGetPrecioRegularDataPRECIOREGULAR:
        """Gets the precio_regular of this ResponseGetPrecioRegularData.


        :return: The precio_regular of this ResponseGetPrecioRegularData.
        :rtype: ResponseGetPrecioRegularDataPRECIOREGULAR
        """
        return self._precio_regular

    @precio_regular.setter
    def precio_regular(self, precio_regular: ResponseGetPrecioRegularDataPRECIOREGULAR):
        """Sets the precio_regular of this ResponseGetPrecioRegularData.


        :param precio_regular: The precio_regular of this ResponseGetPrecioRegularData.
        :type precio_regular: ResponseGetPrecioRegularDataPRECIOREGULAR
        """

        self._precio_regular = precio_regular
