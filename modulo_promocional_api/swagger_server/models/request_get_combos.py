# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class RequestGetCombos(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, channel: str=None, type: str=None, stype: str=None, v1: str=None, external_transaction_id: str=None):  # noqa: E501
        """RequestGetCombos - a model defined in Swagger

        :param channel: The channel of this RequestGetCombos.  # noqa: E501
        :type channel: str
        :param type: The type of this RequestGetCombos.  # noqa: E501
        :type type: str
        :param stype: The stype of this RequestGetCombos.  # noqa: E501
        :type stype: str
        :param v1: The v1 of this RequestGetCombos.  # noqa: E501
        :type v1: str
        :param external_transaction_id: The external_transaction_id of this RequestGetCombos.  # noqa: E501
        :type external_transaction_id: str
        """
        self.swagger_types = {
            'channel': str,
            'type': str,
            'stype': str,
            'v1': str,
            'external_transaction_id': str
        }

        self.attribute_map = {
            'channel': 'channel',
            'type': 'type',
            'stype': 'stype',
            'v1': '_V1',
            'external_transaction_id': 'externalTransactionId'
        }
        self._channel = channel
        self._type = type
        self._stype = stype
        self._v1 = v1
        self._external_transaction_id = external_transaction_id

    @classmethod
    def from_dict(cls, dikt) -> 'RequestGetCombos':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The RequestGetCombos of this RequestGetCombos.  # noqa: E501
        :rtype: RequestGetCombos
        """
        return util.deserialize_model(dikt, cls)

    @property
    def channel(self) -> str:
        """Gets the channel of this RequestGetCombos.


        :return: The channel of this RequestGetCombos.
        :rtype: str
        """
        return self._channel

    @channel.setter
    def channel(self, channel: str):
        """Sets the channel of this RequestGetCombos.


        :param channel: The channel of this RequestGetCombos.
        :type channel: str
        """
        if channel is None:
            raise ValueError("Invalid value for `channel`, must not be `None`")  # noqa: E501

        self._channel = channel

    @property
    def type(self) -> str:
        """Gets the type of this RequestGetCombos.


        :return: The type of this RequestGetCombos.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this RequestGetCombos.


        :param type: The type of this RequestGetCombos.
        :type type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def stype(self) -> str:
        """Gets the stype of this RequestGetCombos.


        :return: The stype of this RequestGetCombos.
        :rtype: str
        """
        return self._stype

    @stype.setter
    def stype(self, stype: str):
        """Sets the stype of this RequestGetCombos.


        :param stype: The stype of this RequestGetCombos.
        :type stype: str
        """
        if stype is None:
            raise ValueError("Invalid value for `stype`, must not be `None`")  # noqa: E501

        self._stype = stype

    @property
    def v1(self) -> str:
        """Gets the v1 of this RequestGetCombos.


        :return: The v1 of this RequestGetCombos.
        :rtype: str
        """
        return self._v1

    @v1.setter
    def v1(self, v1: str):
        """Sets the v1 of this RequestGetCombos.


        :param v1: The v1 of this RequestGetCombos.
        :type v1: str
        """

        self._v1 = v1

    @property
    def external_transaction_id(self) -> str:
        """Gets the external_transaction_id of this RequestGetCombos.


        :return: The external_transaction_id of this RequestGetCombos.
        :rtype: str
        """
        return self._external_transaction_id

    @external_transaction_id.setter
    def external_transaction_id(self, external_transaction_id: str):
        """Sets the external_transaction_id of this RequestGetCombos.


        :param external_transaction_id: The external_transaction_id of this RequestGetCombos.
        :type external_transaction_id: str
        """
        if external_transaction_id is None:
            raise ValueError("Invalid value for `external_transaction_id`, must not be `None`")  # noqa: E501

        self._external_transaction_id = external_transaction_id
