# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class ResponseGetComboPlanesCOMBOPLAN(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, tariffplan: str=None, tariffplanid: int=None):  # noqa: E501
        """ResponseGetComboPlanesCOMBOPLAN - a model defined in Swagger

        :param tariffplan: The tariffplan of this ResponseGetComboPlanesCOMBOPLAN.  # noqa: E501
        :type tariffplan: str
        :param tariffplanid: The tariffplanid of this ResponseGetComboPlanesCOMBOPLAN.  # noqa: E501
        :type tariffplanid: int
        """
        self.swagger_types = {
            'tariffplan': str,
            'tariffplanid': int
        }

        self.attribute_map = {
            'tariffplan': 'TARIFFPLAN',
            'tariffplanid': 'TARIFFPLANID'
        }
        self._tariffplan = tariffplan
        self._tariffplanid = tariffplanid

    @classmethod
    def from_dict(cls, dikt) -> 'ResponseGetComboPlanesCOMBOPLAN':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ResponseGetCombo_Planes_COMBO_PLAN of this ResponseGetComboPlanesCOMBOPLAN.  # noqa: E501
        :rtype: ResponseGetComboPlanesCOMBOPLAN
        """
        return util.deserialize_model(dikt, cls)

    @property
    def tariffplan(self) -> str:
        """Gets the tariffplan of this ResponseGetComboPlanesCOMBOPLAN.


        :return: The tariffplan of this ResponseGetComboPlanesCOMBOPLAN.
        :rtype: str
        """
        return self._tariffplan

    @tariffplan.setter
    def tariffplan(self, tariffplan: str):
        """Sets the tariffplan of this ResponseGetComboPlanesCOMBOPLAN.


        :param tariffplan: The tariffplan of this ResponseGetComboPlanesCOMBOPLAN.
        :type tariffplan: str
        """

        self._tariffplan = tariffplan

    @property
    def tariffplanid(self) -> int:
        """Gets the tariffplanid of this ResponseGetComboPlanesCOMBOPLAN.


        :return: The tariffplanid of this ResponseGetComboPlanesCOMBOPLAN.
        :rtype: int
        """
        return self._tariffplanid

    @tariffplanid.setter
    def tariffplanid(self, tariffplanid: int):
        """Sets the tariffplanid of this ResponseGetComboPlanesCOMBOPLAN.


        :param tariffplanid: The tariffplanid of this ResponseGetComboPlanesCOMBOPLAN.
        :type tariffplanid: int
        """

        self._tariffplanid = tariffplanid
