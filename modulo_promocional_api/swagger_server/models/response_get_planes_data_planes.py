# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class ResponseGetPlanesDataPLANES(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, tariffplanid: int=None, tariffplan: str=None, tariffplanvariantid: int=None, tariffplanvariant: str=None):  # noqa: E501
        """ResponseGetPlanesDataPLANES - a model defined in Swagger

        :param tariffplanid: The tariffplanid of this ResponseGetPlanesDataPLANES.  # noqa: E501
        :type tariffplanid: int
        :param tariffplan: The tariffplan of this ResponseGetPlanesDataPLANES.  # noqa: E501
        :type tariffplan: str
        :param tariffplanvariantid: The tariffplanvariantid of this ResponseGetPlanesDataPLANES.  # noqa: E501
        :type tariffplanvariantid: int
        :param tariffplanvariant: The tariffplanvariant of this ResponseGetPlanesDataPLANES.  # noqa: E501
        :type tariffplanvariant: str
        """
        self.swagger_types = {
            'tariffplanid': int,
            'tariffplan': str,
            'tariffplanvariantid': int,
            'tariffplanvariant': str
        }

        self.attribute_map = {
            'tariffplanid': 'TARIFFPLANID',
            'tariffplan': 'TARIFFPLAN',
            'tariffplanvariantid': 'TARIFFPLANVARIANTID',
            'tariffplanvariant': 'TARIFFPLANVARIANT'
        }
        self._tariffplanid = tariffplanid
        self._tariffplan = tariffplan
        self._tariffplanvariantid = tariffplanvariantid
        self._tariffplanvariant = tariffplanvariant

    @classmethod
    def from_dict(cls, dikt) -> 'ResponseGetPlanesDataPLANES':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ResponseGetPlanes_data_PLANES of this ResponseGetPlanesDataPLANES.  # noqa: E501
        :rtype: ResponseGetPlanesDataPLANES
        """
        return util.deserialize_model(dikt, cls)

    @property
    def tariffplanid(self) -> int:
        """Gets the tariffplanid of this ResponseGetPlanesDataPLANES.


        :return: The tariffplanid of this ResponseGetPlanesDataPLANES.
        :rtype: int
        """
        return self._tariffplanid

    @tariffplanid.setter
    def tariffplanid(self, tariffplanid: int):
        """Sets the tariffplanid of this ResponseGetPlanesDataPLANES.


        :param tariffplanid: The tariffplanid of this ResponseGetPlanesDataPLANES.
        :type tariffplanid: int
        """

        self._tariffplanid = tariffplanid

    @property
    def tariffplan(self) -> str:
        """Gets the tariffplan of this ResponseGetPlanesDataPLANES.


        :return: The tariffplan of this ResponseGetPlanesDataPLANES.
        :rtype: str
        """
        return self._tariffplan

    @tariffplan.setter
    def tariffplan(self, tariffplan: str):
        """Sets the tariffplan of this ResponseGetPlanesDataPLANES.


        :param tariffplan: The tariffplan of this ResponseGetPlanesDataPLANES.
        :type tariffplan: str
        """

        self._tariffplan = tariffplan

    @property
    def tariffplanvariantid(self) -> int:
        """Gets the tariffplanvariantid of this ResponseGetPlanesDataPLANES.


        :return: The tariffplanvariantid of this ResponseGetPlanesDataPLANES.
        :rtype: int
        """
        return self._tariffplanvariantid

    @tariffplanvariantid.setter
    def tariffplanvariantid(self, tariffplanvariantid: int):
        """Sets the tariffplanvariantid of this ResponseGetPlanesDataPLANES.


        :param tariffplanvariantid: The tariffplanvariantid of this ResponseGetPlanesDataPLANES.
        :type tariffplanvariantid: int
        """

        self._tariffplanvariantid = tariffplanvariantid

    @property
    def tariffplanvariant(self) -> str:
        """Gets the tariffplanvariant of this ResponseGetPlanesDataPLANES.


        :return: The tariffplanvariant of this ResponseGetPlanesDataPLANES.
        :rtype: str
        """
        return self._tariffplanvariant

    @tariffplanvariant.setter
    def tariffplanvariant(self, tariffplanvariant: str):
        """Sets the tariffplanvariant of this ResponseGetPlanesDataPLANES.


        :param tariffplanvariant: The tariffplanvariant of this ResponseGetPlanesDataPLANES.
        :type tariffplanvariant: str
        """

        self._tariffplanvariant = tariffplanvariant
