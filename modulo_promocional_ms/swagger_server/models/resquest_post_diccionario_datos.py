# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.data_post_diccionario_datos import DataPostDiccionarioDatos  # noqa: F401,E501
from swagger_server import util


class ResquestPostDiccionarioDatos(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, external_transaction_id: str=None, channel: str=None, data: DataPostDiccionarioDatos=None):  # noqa: E501
        """ResquestPostDiccionarioDatos - a model defined in Swagger

        :param external_transaction_id: The external_transaction_id of this ResquestPostDiccionarioDatos.  # noqa: E501
        :type external_transaction_id: str
        :param channel: The channel of this ResquestPostDiccionarioDatos.  # noqa: E501
        :type channel: str
        :param data: The data of this ResquestPostDiccionarioDatos.  # noqa: E501
        :type data: DataPostDiccionarioDatos
        """
        self.swagger_types = {
            'external_transaction_id': str,
            'channel': str,
            'data': DataPostDiccionarioDatos
        }

        self.attribute_map = {
            'external_transaction_id': 'externalTransactionId',
            'channel': 'channel',
            'data': 'data'
        }
        self._external_transaction_id = external_transaction_id
        self._channel = channel
        self._data = data

    @classmethod
    def from_dict(cls, dikt) -> 'ResquestPostDiccionarioDatos':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ResquestPostDiccionarioDatos of this ResquestPostDiccionarioDatos.  # noqa: E501
        :rtype: ResquestPostDiccionarioDatos
        """
        return util.deserialize_model(dikt, cls)

    @property
    def external_transaction_id(self) -> str:
        """Gets the external_transaction_id of this ResquestPostDiccionarioDatos.


        :return: The external_transaction_id of this ResquestPostDiccionarioDatos.
        :rtype: str
        """
        return self._external_transaction_id

    @external_transaction_id.setter
    def external_transaction_id(self, external_transaction_id: str):
        """Sets the external_transaction_id of this ResquestPostDiccionarioDatos.


        :param external_transaction_id: The external_transaction_id of this ResquestPostDiccionarioDatos.
        :type external_transaction_id: str
        """
        if external_transaction_id is None:
            raise ValueError("Invalid value for `external_transaction_id`, must not be `None`")  # noqa: E501

        self._external_transaction_id = external_transaction_id

    @property
    def channel(self) -> str:
        """Gets the channel of this ResquestPostDiccionarioDatos.


        :return: The channel of this ResquestPostDiccionarioDatos.
        :rtype: str
        """
        return self._channel

    @channel.setter
    def channel(self, channel: str):
        """Sets the channel of this ResquestPostDiccionarioDatos.


        :param channel: The channel of this ResquestPostDiccionarioDatos.
        :type channel: str
        """
        if channel is None:
            raise ValueError("Invalid value for `channel`, must not be `None`")  # noqa: E501

        self._channel = channel

    @property
    def data(self) -> DataPostDiccionarioDatos:
        """Gets the data of this ResquestPostDiccionarioDatos.


        :return: The data of this ResquestPostDiccionarioDatos.
        :rtype: DataPostDiccionarioDatos
        """
        return self._data

    @data.setter
    def data(self, data: DataPostDiccionarioDatos):
        """Sets the data of this ResquestPostDiccionarioDatos.


        :param data: The data of this ResquestPostDiccionarioDatos.
        :type data: DataPostDiccionarioDatos
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")  # noqa: E501

        self._data = data
