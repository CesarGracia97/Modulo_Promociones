# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class RequestGetCiudades(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, channel: str=None, type: str=None, id_prov: int=None, id_provs: List[int]=None, tariffplanvariant: int=None, productoid: int=None, external_transaction_id: str=None):  # noqa: E501
        """RequestGetCiudades - a model defined in Swagger

        :param channel: The channel of this RequestGetCiudades.  # noqa: E501
        :type channel: str
        :param type: The type of this RequestGetCiudades.  # noqa: E501
        :type type: str
        :param id_prov: The id_prov of this RequestGetCiudades.  # noqa: E501
        :type id_prov: int
        :param id_provs: The id_provs of this RequestGetCiudades.  # noqa: E501
        :type id_provs: List[int]
        :param tariffplanvariant: The tariffplanvariant of this RequestGetCiudades.  # noqa: E501
        :type tariffplanvariant: int
        :param productoid: The productoid of this RequestGetCiudades.  # noqa: E501
        :type productoid: int
        :param external_transaction_id: The external_transaction_id of this RequestGetCiudades.  # noqa: E501
        :type external_transaction_id: str
        """
        self.swagger_types = {
            'channel': str,
            'type': str,
            'id_prov': int,
            'id_provs': List[int],
            'tariffplanvariant': int,
            'productoid': int,
            'external_transaction_id': str
        }

        self.attribute_map = {
            'channel': 'channel',
            'type': 'type',
            'id_prov': 'id_Prov',
            'id_provs': 'id_Provs',
            'tariffplanvariant': 'TARIFFPLANVARIANT',
            'productoid': 'PRODUCTOID',
            'external_transaction_id': 'externalTransactionId'
        }
        self._channel = channel
        self._type = type
        self._id_prov = id_prov
        self._id_provs = id_provs
        self._tariffplanvariant = tariffplanvariant
        self._productoid = productoid
        self._external_transaction_id = external_transaction_id

    @classmethod
    def from_dict(cls, dikt) -> 'RequestGetCiudades':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The RequestGetCiudades of this RequestGetCiudades.  # noqa: E501
        :rtype: RequestGetCiudades
        """
        return util.deserialize_model(dikt, cls)

    @property
    def channel(self) -> str:
        """Gets the channel of this RequestGetCiudades.


        :return: The channel of this RequestGetCiudades.
        :rtype: str
        """
        return self._channel

    @channel.setter
    def channel(self, channel: str):
        """Sets the channel of this RequestGetCiudades.


        :param channel: The channel of this RequestGetCiudades.
        :type channel: str
        """
        if channel is None:
            raise ValueError("Invalid value for `channel`, must not be `None`")  # noqa: E501

        self._channel = channel

    @property
    def type(self) -> str:
        """Gets the type of this RequestGetCiudades.


        :return: The type of this RequestGetCiudades.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this RequestGetCiudades.


        :param type: The type of this RequestGetCiudades.
        :type type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def id_prov(self) -> int:
        """Gets the id_prov of this RequestGetCiudades.


        :return: The id_prov of this RequestGetCiudades.
        :rtype: int
        """
        return self._id_prov

    @id_prov.setter
    def id_prov(self, id_prov: int):
        """Sets the id_prov of this RequestGetCiudades.


        :param id_prov: The id_prov of this RequestGetCiudades.
        :type id_prov: int
        """

        self._id_prov = id_prov

    @property
    def id_provs(self) -> List[int]:
        """Gets the id_provs of this RequestGetCiudades.


        :return: The id_provs of this RequestGetCiudades.
        :rtype: List[int]
        """
        return self._id_provs

    @id_provs.setter
    def id_provs(self, id_provs: List[int]):
        """Sets the id_provs of this RequestGetCiudades.


        :param id_provs: The id_provs of this RequestGetCiudades.
        :type id_provs: List[int]
        """

        self._id_provs = id_provs

    @property
    def tariffplanvariant(self) -> int:
        """Gets the tariffplanvariant of this RequestGetCiudades.


        :return: The tariffplanvariant of this RequestGetCiudades.
        :rtype: int
        """
        return self._tariffplanvariant

    @tariffplanvariant.setter
    def tariffplanvariant(self, tariffplanvariant: int):
        """Sets the tariffplanvariant of this RequestGetCiudades.


        :param tariffplanvariant: The tariffplanvariant of this RequestGetCiudades.
        :type tariffplanvariant: int
        """

        self._tariffplanvariant = tariffplanvariant

    @property
    def productoid(self) -> int:
        """Gets the productoid of this RequestGetCiudades.


        :return: The productoid of this RequestGetCiudades.
        :rtype: int
        """
        return self._productoid

    @productoid.setter
    def productoid(self, productoid: int):
        """Sets the productoid of this RequestGetCiudades.


        :param productoid: The productoid of this RequestGetCiudades.
        :type productoid: int
        """

        self._productoid = productoid

    @property
    def external_transaction_id(self) -> str:
        """Gets the external_transaction_id of this RequestGetCiudades.


        :return: The external_transaction_id of this RequestGetCiudades.
        :rtype: str
        """
        return self._external_transaction_id

    @external_transaction_id.setter
    def external_transaction_id(self, external_transaction_id: str):
        """Sets the external_transaction_id of this RequestGetCiudades.


        :param external_transaction_id: The external_transaction_id of this RequestGetCiudades.
        :type external_transaction_id: str
        """
        if external_transaction_id is None:
            raise ValueError("Invalid value for `external_transaction_id`, must not be `None`")  # noqa: E501

        self._external_transaction_id = external_transaction_id
