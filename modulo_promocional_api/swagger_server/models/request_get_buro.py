# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class RequestGetBuro(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, channel: str=None, type: str=None, external_transaction_id: str=None):  # noqa: E501
        """RequestGetBuro - a model defined in Swagger

        :param channel: The channel of this RequestGetBuro.  # noqa: E501
        :type channel: str
        :param type: The type of this RequestGetBuro.  # noqa: E501
        :type type: str
        :param external_transaction_id: The external_transaction_id of this RequestGetBuro.  # noqa: E501
        :type external_transaction_id: str
        """
        self.swagger_types = {
            'channel': str,
            'type': str,
            'external_transaction_id': str
        }

        self.attribute_map = {
            'channel': 'channel',
            'type': 'type',
            'external_transaction_id': 'externalTransactionId'
        }
        self._channel = channel
        self._type = type
        self._external_transaction_id = external_transaction_id

    @classmethod
    def from_dict(cls, dikt) -> 'RequestGetBuro':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The RequestGetBuro of this RequestGetBuro.  # noqa: E501
        :rtype: RequestGetBuro
        """
        return util.deserialize_model(dikt, cls)

    @property
    def channel(self) -> str:
        """Gets the channel of this RequestGetBuro.


        :return: The channel of this RequestGetBuro.
        :rtype: str
        """
        return self._channel

    @channel.setter
    def channel(self, channel: str):
        """Sets the channel of this RequestGetBuro.


        :param channel: The channel of this RequestGetBuro.
        :type channel: str
        """
        if channel is None:
            raise ValueError("Invalid value for `channel`, must not be `None`")  # noqa: E501

        self._channel = channel

    @property
    def type(self) -> str:
        """Gets the type of this RequestGetBuro.


        :return: The type of this RequestGetBuro.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this RequestGetBuro.


        :param type: The type of this RequestGetBuro.
        :type type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def external_transaction_id(self) -> str:
        """Gets the external_transaction_id of this RequestGetBuro.


        :return: The external_transaction_id of this RequestGetBuro.
        :rtype: str
        """
        return self._external_transaction_id

    @external_transaction_id.setter
    def external_transaction_id(self, external_transaction_id: str):
        """Sets the external_transaction_id of this RequestGetBuro.


        :param external_transaction_id: The external_transaction_id of this RequestGetBuro.
        :type external_transaction_id: str
        """
        if external_transaction_id is None:
            raise ValueError("Invalid value for `external_transaction_id`, must not be `None`")  # noqa: E501

        self._external_transaction_id = external_transaction_id