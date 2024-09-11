# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.response_get_buro_data_buro import ResponseGetBuroDataBURO  # noqa: F401,E501
from swagger_server import util


class ResponseGetBuroData(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, error_code: int=None, internal_transaction_id: str=None, external_transaction_id: str=None, message: str=None, buro: ResponseGetBuroDataBURO=None):  # noqa: E501
        """ResponseGetBuroData - a model defined in Swagger

        :param error_code: The error_code of this ResponseGetBuroData.  # noqa: E501
        :type error_code: int
        :param internal_transaction_id: The internal_transaction_id of this ResponseGetBuroData.  # noqa: E501
        :type internal_transaction_id: str
        :param external_transaction_id: The external_transaction_id of this ResponseGetBuroData.  # noqa: E501
        :type external_transaction_id: str
        :param message: The message of this ResponseGetBuroData.  # noqa: E501
        :type message: str
        :param buro: The buro of this ResponseGetBuroData.  # noqa: E501
        :type buro: ResponseGetBuroDataBURO
        """
        self.swagger_types = {
            'error_code': int,
            'internal_transaction_id': str,
            'external_transaction_id': str,
            'message': str,
            'buro': ResponseGetBuroDataBURO
        }

        self.attribute_map = {
            'error_code': 'errorCode',
            'internal_transaction_id': 'internalTransactionId',
            'external_transaction_id': 'externalTransactionId',
            'message': 'message',
            'buro': 'BURO'
        }
        self._error_code = error_code
        self._internal_transaction_id = internal_transaction_id
        self._external_transaction_id = external_transaction_id
        self._message = message
        self._buro = buro

    @classmethod
    def from_dict(cls, dikt) -> 'ResponseGetBuroData':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ResponseGetBuro_data of this ResponseGetBuroData.  # noqa: E501
        :rtype: ResponseGetBuroData
        """
        return util.deserialize_model(dikt, cls)

    @property
    def error_code(self) -> int:
        """Gets the error_code of this ResponseGetBuroData.


        :return: The error_code of this ResponseGetBuroData.
        :rtype: int
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code: int):
        """Sets the error_code of this ResponseGetBuroData.


        :param error_code: The error_code of this ResponseGetBuroData.
        :type error_code: int
        """

        self._error_code = error_code

    @property
    def internal_transaction_id(self) -> str:
        """Gets the internal_transaction_id of this ResponseGetBuroData.


        :return: The internal_transaction_id of this ResponseGetBuroData.
        :rtype: str
        """
        return self._internal_transaction_id

    @internal_transaction_id.setter
    def internal_transaction_id(self, internal_transaction_id: str):
        """Sets the internal_transaction_id of this ResponseGetBuroData.


        :param internal_transaction_id: The internal_transaction_id of this ResponseGetBuroData.
        :type internal_transaction_id: str
        """

        self._internal_transaction_id = internal_transaction_id

    @property
    def external_transaction_id(self) -> str:
        """Gets the external_transaction_id of this ResponseGetBuroData.


        :return: The external_transaction_id of this ResponseGetBuroData.
        :rtype: str
        """
        return self._external_transaction_id

    @external_transaction_id.setter
    def external_transaction_id(self, external_transaction_id: str):
        """Sets the external_transaction_id of this ResponseGetBuroData.


        :param external_transaction_id: The external_transaction_id of this ResponseGetBuroData.
        :type external_transaction_id: str
        """

        self._external_transaction_id = external_transaction_id

    @property
    def message(self) -> str:
        """Gets the message of this ResponseGetBuroData.


        :return: The message of this ResponseGetBuroData.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message: str):
        """Sets the message of this ResponseGetBuroData.


        :param message: The message of this ResponseGetBuroData.
        :type message: str
        """

        self._message = message

    @property
    def buro(self) -> ResponseGetBuroDataBURO:
        """Gets the buro of this ResponseGetBuroData.


        :return: The buro of this ResponseGetBuroData.
        :rtype: ResponseGetBuroDataBURO
        """
        return self._buro

    @buro.setter
    def buro(self, buro: ResponseGetBuroDataBURO):
        """Sets the buro of this ResponseGetBuroData.


        :param buro: The buro of this ResponseGetBuroData.
        :type buro: ResponseGetBuroDataBURO
        """

        self._buro = buro