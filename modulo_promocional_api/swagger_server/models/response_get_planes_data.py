# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.response_get_planes_data_planes import ResponseGetPlanesDataPLANES  # noqa: F401,E501
from swagger_server import util


class ResponseGetPlanesData(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, error_code: int=None, internal_transaction_id: str=None, external_transaction_id: str=None, message: str=None, planes: ResponseGetPlanesDataPLANES=None):  # noqa: E501
        """ResponseGetPlanesData - a model defined in Swagger

        :param error_code: The error_code of this ResponseGetPlanesData.  # noqa: E501
        :type error_code: int
        :param internal_transaction_id: The internal_transaction_id of this ResponseGetPlanesData.  # noqa: E501
        :type internal_transaction_id: str
        :param external_transaction_id: The external_transaction_id of this ResponseGetPlanesData.  # noqa: E501
        :type external_transaction_id: str
        :param message: The message of this ResponseGetPlanesData.  # noqa: E501
        :type message: str
        :param planes: The planes of this ResponseGetPlanesData.  # noqa: E501
        :type planes: ResponseGetPlanesDataPLANES
        """
        self.swagger_types = {
            'error_code': int,
            'internal_transaction_id': str,
            'external_transaction_id': str,
            'message': str,
            'planes': ResponseGetPlanesDataPLANES
        }

        self.attribute_map = {
            'error_code': 'errorCode',
            'internal_transaction_id': 'internalTransactionId',
            'external_transaction_id': 'externalTransactionId',
            'message': 'message',
            'planes': 'PLANES'
        }
        self._error_code = error_code
        self._internal_transaction_id = internal_transaction_id
        self._external_transaction_id = external_transaction_id
        self._message = message
        self._planes = planes

    @classmethod
    def from_dict(cls, dikt) -> 'ResponseGetPlanesData':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ResponseGetPlanes_data of this ResponseGetPlanesData.  # noqa: E501
        :rtype: ResponseGetPlanesData
        """
        return util.deserialize_model(dikt, cls)

    @property
    def error_code(self) -> int:
        """Gets the error_code of this ResponseGetPlanesData.


        :return: The error_code of this ResponseGetPlanesData.
        :rtype: int
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code: int):
        """Sets the error_code of this ResponseGetPlanesData.


        :param error_code: The error_code of this ResponseGetPlanesData.
        :type error_code: int
        """

        self._error_code = error_code

    @property
    def internal_transaction_id(self) -> str:
        """Gets the internal_transaction_id of this ResponseGetPlanesData.


        :return: The internal_transaction_id of this ResponseGetPlanesData.
        :rtype: str
        """
        return self._internal_transaction_id

    @internal_transaction_id.setter
    def internal_transaction_id(self, internal_transaction_id: str):
        """Sets the internal_transaction_id of this ResponseGetPlanesData.


        :param internal_transaction_id: The internal_transaction_id of this ResponseGetPlanesData.
        :type internal_transaction_id: str
        """

        self._internal_transaction_id = internal_transaction_id

    @property
    def external_transaction_id(self) -> str:
        """Gets the external_transaction_id of this ResponseGetPlanesData.


        :return: The external_transaction_id of this ResponseGetPlanesData.
        :rtype: str
        """
        return self._external_transaction_id

    @external_transaction_id.setter
    def external_transaction_id(self, external_transaction_id: str):
        """Sets the external_transaction_id of this ResponseGetPlanesData.


        :param external_transaction_id: The external_transaction_id of this ResponseGetPlanesData.
        :type external_transaction_id: str
        """

        self._external_transaction_id = external_transaction_id

    @property
    def message(self) -> str:
        """Gets the message of this ResponseGetPlanesData.


        :return: The message of this ResponseGetPlanesData.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message: str):
        """Sets the message of this ResponseGetPlanesData.


        :param message: The message of this ResponseGetPlanesData.
        :type message: str
        """

        self._message = message

    @property
    def planes(self) -> ResponseGetPlanesDataPLANES:
        """Gets the planes of this ResponseGetPlanesData.


        :return: The planes of this ResponseGetPlanesData.
        :rtype: ResponseGetPlanesDataPLANES
        """
        return self._planes

    @planes.setter
    def planes(self, planes: ResponseGetPlanesDataPLANES):
        """Sets the planes of this ResponseGetPlanesData.


        :param planes: The planes of this ResponseGetPlanesData.
        :type planes: ResponseGetPlanesDataPLANES
        """

        self._planes = planes
