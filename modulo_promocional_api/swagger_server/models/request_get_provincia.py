# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class RequestGetProvincia(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, channel: str=None, type: str=None, tariffplanvariant: int=None):  # noqa: E501
        """RequestGetProvincia - a model defined in Swagger

        :param channel: The channel of this RequestGetProvincia.  # noqa: E501
        :type channel: str
        :param type: The type of this RequestGetProvincia.  # noqa: E501
        :type type: str
        :param tariffplanvariant: The tariffplanvariant of this RequestGetProvincia.  # noqa: E501
        :type tariffplanvariant: int
        """
        self.swagger_types = {
            'channel': str,
            'type': str,
            'tariffplanvariant': int
        }

        self.attribute_map = {
            'channel': 'channel',
            'type': 'type',
            'tariffplanvariant': 'TARIFFPLANVARIANT'
        }
        self._channel = channel
        self._type = type
        self._tariffplanvariant = tariffplanvariant

    @classmethod
    def from_dict(cls, dikt) -> 'RequestGetProvincia':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The RequestGetProvincia of this RequestGetProvincia.  # noqa: E501
        :rtype: RequestGetProvincia
        """
        return util.deserialize_model(dikt, cls)

    @property
    def channel(self) -> str:
        """Gets the channel of this RequestGetProvincia.


        :return: The channel of this RequestGetProvincia.
        :rtype: str
        """
        return self._channel

    @channel.setter
    def channel(self, channel: str):
        """Sets the channel of this RequestGetProvincia.


        :param channel: The channel of this RequestGetProvincia.
        :type channel: str
        """
        if channel is None:
            raise ValueError("Invalid value for `channel`, must not be `None`")  # noqa: E501

        self._channel = channel

    @property
    def type(self) -> str:
        """Gets the type of this RequestGetProvincia.


        :return: The type of this RequestGetProvincia.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this RequestGetProvincia.


        :param type: The type of this RequestGetProvincia.
        :type type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def tariffplanvariant(self) -> int:
        """Gets the tariffplanvariant of this RequestGetProvincia.


        :return: The tariffplanvariant of this RequestGetProvincia.
        :rtype: int
        """
        return self._tariffplanvariant

    @tariffplanvariant.setter
    def tariffplanvariant(self, tariffplanvariant: int):
        """Sets the tariffplanvariant of this RequestGetProvincia.


        :param tariffplanvariant: The tariffplanvariant of this RequestGetProvincia.
        :type tariffplanvariant: int
        """

        self._tariffplanvariant = tariffplanvariant
