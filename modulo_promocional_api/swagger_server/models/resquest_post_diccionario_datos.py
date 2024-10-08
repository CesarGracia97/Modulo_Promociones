# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.diccionario_datos import DiccionarioDatos  # noqa: F401,E501
from swagger_server import util


class ResquestPostDiccionarioDatos(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, channel: str=None, diccionario_datos: DiccionarioDatos=None, external_transaction_id: str=None):  # noqa: E501
        """ResquestPostDiccionarioDatos - a model defined in Swagger

        :param channel: The channel of this ResquestPostDiccionarioDatos.  # noqa: E501
        :type channel: str
        :param diccionario_datos: The diccionario_datos of this ResquestPostDiccionarioDatos.  # noqa: E501
        :type diccionario_datos: DiccionarioDatos
        :param external_transaction_id: The external_transaction_id of this ResquestPostDiccionarioDatos.  # noqa: E501
        :type external_transaction_id: str
        """
        self.swagger_types = {
            'channel': str,
            'diccionario_datos': DiccionarioDatos,
            'external_transaction_id': str
        }

        self.attribute_map = {
            'channel': 'channel',
            'diccionario_datos': 'diccionarioDatos',
            'external_transaction_id': 'externalTransactionId'
        }
        self._channel = channel
        self._diccionario_datos = diccionario_datos
        self._external_transaction_id = external_transaction_id

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
    def diccionario_datos(self) -> DiccionarioDatos:
        """Gets the diccionario_datos of this ResquestPostDiccionarioDatos.


        :return: The diccionario_datos of this ResquestPostDiccionarioDatos.
        :rtype: DiccionarioDatos
        """
        return self._diccionario_datos

    @diccionario_datos.setter
    def diccionario_datos(self, diccionario_datos: DiccionarioDatos):
        """Sets the diccionario_datos of this ResquestPostDiccionarioDatos.


        :param diccionario_datos: The diccionario_datos of this ResquestPostDiccionarioDatos.
        :type diccionario_datos: DiccionarioDatos
        """
        if diccionario_datos is None:
            raise ValueError("Invalid value for `diccionario_datos`, must not be `None`")  # noqa: E501

        self._diccionario_datos = diccionario_datos

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
