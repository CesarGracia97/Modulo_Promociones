# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.response_get_ciudad_data_cities import ResponseGetCiudadDataCITIES  # noqa: F401,E501
from swagger_server import util


class ResponseGetCiudadData(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, error_code: int=None, internal_transaction_id: str=None, external_transaction_id: str=None, message: str=None, cities: ResponseGetCiudadDataCITIES=None, citiesx_prov: ResponseGetCiudadDataCITIES=None):  # noqa: E501
        """ResponseGetCiudadData - a model defined in Swagger

        :param error_code: The error_code of this ResponseGetCiudadData.  # noqa: E501
        :type error_code: int
        :param internal_transaction_id: The internal_transaction_id of this ResponseGetCiudadData.  # noqa: E501
        :type internal_transaction_id: str
        :param external_transaction_id: The external_transaction_id of this ResponseGetCiudadData.  # noqa: E501
        :type external_transaction_id: str
        :param message: The message of this ResponseGetCiudadData.  # noqa: E501
        :type message: str
        :param cities: The cities of this ResponseGetCiudadData.  # noqa: E501
        :type cities: ResponseGetCiudadDataCITIES
        :param citiesx_prov: The citiesx_prov of this ResponseGetCiudadData.  # noqa: E501
        :type citiesx_prov: ResponseGetCiudadDataCITIES
        """
        self.swagger_types = {
            'error_code': int,
            'internal_transaction_id': str,
            'external_transaction_id': str,
            'message': str,
            'cities': ResponseGetCiudadDataCITIES,
            'citiesx_prov': ResponseGetCiudadDataCITIES
        }

        self.attribute_map = {
            'error_code': 'errorCode',
            'internal_transaction_id': 'internalTransactionId',
            'external_transaction_id': 'externalTransactionId',
            'message': 'message',
            'cities': 'CITIES',
            'citiesx_prov': 'CITIESxPROV'
        }
        self._error_code = error_code
        self._internal_transaction_id = internal_transaction_id
        self._external_transaction_id = external_transaction_id
        self._message = message
        self._cities = cities
        self._citiesx_prov = citiesx_prov

    @classmethod
    def from_dict(cls, dikt) -> 'ResponseGetCiudadData':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ResponseGetCiudad_data of this ResponseGetCiudadData.  # noqa: E501
        :rtype: ResponseGetCiudadData
        """
        return util.deserialize_model(dikt, cls)

    @property
    def error_code(self) -> int:
        """Gets the error_code of this ResponseGetCiudadData.


        :return: The error_code of this ResponseGetCiudadData.
        :rtype: int
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code: int):
        """Sets the error_code of this ResponseGetCiudadData.


        :param error_code: The error_code of this ResponseGetCiudadData.
        :type error_code: int
        """

        self._error_code = error_code

    @property
    def internal_transaction_id(self) -> str:
        """Gets the internal_transaction_id of this ResponseGetCiudadData.


        :return: The internal_transaction_id of this ResponseGetCiudadData.
        :rtype: str
        """
        return self._internal_transaction_id

    @internal_transaction_id.setter
    def internal_transaction_id(self, internal_transaction_id: str):
        """Sets the internal_transaction_id of this ResponseGetCiudadData.


        :param internal_transaction_id: The internal_transaction_id of this ResponseGetCiudadData.
        :type internal_transaction_id: str
        """

        self._internal_transaction_id = internal_transaction_id

    @property
    def external_transaction_id(self) -> str:
        """Gets the external_transaction_id of this ResponseGetCiudadData.


        :return: The external_transaction_id of this ResponseGetCiudadData.
        :rtype: str
        """
        return self._external_transaction_id

    @external_transaction_id.setter
    def external_transaction_id(self, external_transaction_id: str):
        """Sets the external_transaction_id of this ResponseGetCiudadData.


        :param external_transaction_id: The external_transaction_id of this ResponseGetCiudadData.
        :type external_transaction_id: str
        """

        self._external_transaction_id = external_transaction_id

    @property
    def message(self) -> str:
        """Gets the message of this ResponseGetCiudadData.


        :return: The message of this ResponseGetCiudadData.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message: str):
        """Sets the message of this ResponseGetCiudadData.


        :param message: The message of this ResponseGetCiudadData.
        :type message: str
        """

        self._message = message

    @property
    def cities(self) -> ResponseGetCiudadDataCITIES:
        """Gets the cities of this ResponseGetCiudadData.


        :return: The cities of this ResponseGetCiudadData.
        :rtype: ResponseGetCiudadDataCITIES
        """
        return self._cities

    @cities.setter
    def cities(self, cities: ResponseGetCiudadDataCITIES):
        """Sets the cities of this ResponseGetCiudadData.


        :param cities: The cities of this ResponseGetCiudadData.
        :type cities: ResponseGetCiudadDataCITIES
        """

        self._cities = cities

    @property
    def citiesx_prov(self) -> ResponseGetCiudadDataCITIES:
        """Gets the citiesx_prov of this ResponseGetCiudadData.


        :return: The citiesx_prov of this ResponseGetCiudadData.
        :rtype: ResponseGetCiudadDataCITIES
        """
        return self._citiesx_prov

    @citiesx_prov.setter
    def citiesx_prov(self, citiesx_prov: ResponseGetCiudadDataCITIES):
        """Sets the citiesx_prov of this ResponseGetCiudadData.


        :param citiesx_prov: The citiesx_prov of this ResponseGetCiudadData.
        :type citiesx_prov: ResponseGetCiudadDataCITIES
        """

        self._citiesx_prov = citiesx_prov
