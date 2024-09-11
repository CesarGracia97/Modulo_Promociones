# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class RequestGetPrecioRegular(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, channel: str=None, type: str=None, tariffplanvariant: int=None, id_prod: int=None, external_transaction_id: str=None):  # noqa: E501
        """RequestGetPrecioRegular - a model defined in Swagger

        :param channel: The channel of this RequestGetPrecioRegular.  # noqa: E501
        :type channel: str
        :param type: The type of this RequestGetPrecioRegular.  # noqa: E501
        :type type: str
        :param tariffplanvariant: The tariffplanvariant of this RequestGetPrecioRegular.  # noqa: E501
        :type tariffplanvariant: int
        :param id_prod: The id_prod of this RequestGetPrecioRegular.  # noqa: E501
        :type id_prod: int
        :param external_transaction_id: The external_transaction_id of this RequestGetPrecioRegular.  # noqa: E501
        :type external_transaction_id: str
        """
        self.swagger_types = {
            'channel': str,
            'type': str,
            'tariffplanvariant': int,
            'id_prod': int,
            'external_transaction_id': str
        }

        self.attribute_map = {
            'channel': 'channel',
            'type': 'type',
            'tariffplanvariant': 'TARIFFPLANVARIANT',
            'id_prod': 'id_Prod',
            'external_transaction_id': 'externalTransactionId'
        }
        self._channel = channel
        self._type = type
        self._tariffplanvariant = tariffplanvariant
        self._id_prod = id_prod
        self._external_transaction_id = external_transaction_id

    @classmethod
    def from_dict(cls, dikt) -> 'RequestGetPrecioRegular':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The RequestGetPrecioRegular of this RequestGetPrecioRegular.  # noqa: E501
        :rtype: RequestGetPrecioRegular
        """
        return util.deserialize_model(dikt, cls)

    @property
    def channel(self) -> str:
        """Gets the channel of this RequestGetPrecioRegular.


        :return: The channel of this RequestGetPrecioRegular.
        :rtype: str
        """
        return self._channel

    @channel.setter
    def channel(self, channel: str):
        """Sets the channel of this RequestGetPrecioRegular.


        :param channel: The channel of this RequestGetPrecioRegular.
        :type channel: str
        """
        if channel is None:
            raise ValueError("Invalid value for `channel`, must not be `None`")  # noqa: E501

        self._channel = channel

    @property
    def type(self) -> str:
        """Gets the type of this RequestGetPrecioRegular.


        :return: The type of this RequestGetPrecioRegular.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this RequestGetPrecioRegular.


        :param type: The type of this RequestGetPrecioRegular.
        :type type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def tariffplanvariant(self) -> int:
        """Gets the tariffplanvariant of this RequestGetPrecioRegular.


        :return: The tariffplanvariant of this RequestGetPrecioRegular.
        :rtype: int
        """
        return self._tariffplanvariant

    @tariffplanvariant.setter
    def tariffplanvariant(self, tariffplanvariant: int):
        """Sets the tariffplanvariant of this RequestGetPrecioRegular.


        :param tariffplanvariant: The tariffplanvariant of this RequestGetPrecioRegular.
        :type tariffplanvariant: int
        """
        if tariffplanvariant is None:
            raise ValueError("Invalid value for `tariffplanvariant`, must not be `None`")  # noqa: E501

        self._tariffplanvariant = tariffplanvariant

    @property
    def id_prod(self) -> int:
        """Gets the id_prod of this RequestGetPrecioRegular.


        :return: The id_prod of this RequestGetPrecioRegular.
        :rtype: int
        """
        return self._id_prod

    @id_prod.setter
    def id_prod(self, id_prod: int):
        """Sets the id_prod of this RequestGetPrecioRegular.


        :param id_prod: The id_prod of this RequestGetPrecioRegular.
        :type id_prod: int
        """
        if id_prod is None:
            raise ValueError("Invalid value for `id_prod`, must not be `None`")  # noqa: E501

        self._id_prod = id_prod

    @property
    def external_transaction_id(self) -> str:
        """Gets the external_transaction_id of this RequestGetPrecioRegular.


        :return: The external_transaction_id of this RequestGetPrecioRegular.
        :rtype: str
        """
        return self._external_transaction_id

    @external_transaction_id.setter
    def external_transaction_id(self, external_transaction_id: str):
        """Sets the external_transaction_id of this RequestGetPrecioRegular.


        :param external_transaction_id: The external_transaction_id of this RequestGetPrecioRegular.
        :type external_transaction_id: str
        """
        if external_transaction_id is None:
            raise ValueError("Invalid value for `external_transaction_id`, must not be `None`")  # noqa: E501

        self._external_transaction_id = external_transaction_id