# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class ResponseGetModosPagoMPAGOS(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, name: str=None, id: int=None):  # noqa: E501
        """ResponseGetModosPagoMPAGOS - a model defined in Swagger

        :param name: The name of this ResponseGetModosPagoMPAGOS.  # noqa: E501
        :type name: str
        :param id: The id of this ResponseGetModosPagoMPAGOS.  # noqa: E501
        :type id: int
        """
        self.swagger_types = {
            'name': str,
            'id': int
        }

        self.attribute_map = {
            'name': 'NAME',
            'id': 'ID'
        }
        self._name = name
        self._id = id

    @classmethod
    def from_dict(cls, dikt) -> 'ResponseGetModosPagoMPAGOS':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ResponseGetModos_Pago_MPAGOS of this ResponseGetModosPagoMPAGOS.  # noqa: E501
        :rtype: ResponseGetModosPagoMPAGOS
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self) -> str:
        """Gets the name of this ResponseGetModosPagoMPAGOS.


        :return: The name of this ResponseGetModosPagoMPAGOS.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this ResponseGetModosPagoMPAGOS.


        :param name: The name of this ResponseGetModosPagoMPAGOS.
        :type name: str
        """

        self._name = name

    @property
    def id(self) -> int:
        """Gets the id of this ResponseGetModosPagoMPAGOS.


        :return: The id of this ResponseGetModosPagoMPAGOS.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this ResponseGetModosPagoMPAGOS.


        :param id: The id of this ResponseGetModosPagoMPAGOS.
        :type id: int
        """

        self._id = id
