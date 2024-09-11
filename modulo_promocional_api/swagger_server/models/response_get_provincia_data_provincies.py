# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class ResponseGetProvinciaDataPROVINCIES(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, provincia_id: int=None, provincia: str=None):  # noqa: E501
        """ResponseGetProvinciaDataPROVINCIES - a model defined in Swagger

        :param provincia_id: The provincia_id of this ResponseGetProvinciaDataPROVINCIES.  # noqa: E501
        :type provincia_id: int
        :param provincia: The provincia of this ResponseGetProvinciaDataPROVINCIES.  # noqa: E501
        :type provincia: str
        """
        self.swagger_types = {
            'provincia_id': int,
            'provincia': str
        }

        self.attribute_map = {
            'provincia_id': 'PROVINCIA_ID',
            'provincia': 'PROVINCIA'
        }
        self._provincia_id = provincia_id
        self._provincia = provincia

    @classmethod
    def from_dict(cls, dikt) -> 'ResponseGetProvinciaDataPROVINCIES':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ResponseGetProvincia_data_PROVINCIES of this ResponseGetProvinciaDataPROVINCIES.  # noqa: E501
        :rtype: ResponseGetProvinciaDataPROVINCIES
        """
        return util.deserialize_model(dikt, cls)

    @property
    def provincia_id(self) -> int:
        """Gets the provincia_id of this ResponseGetProvinciaDataPROVINCIES.


        :return: The provincia_id of this ResponseGetProvinciaDataPROVINCIES.
        :rtype: int
        """
        return self._provincia_id

    @provincia_id.setter
    def provincia_id(self, provincia_id: int):
        """Sets the provincia_id of this ResponseGetProvinciaDataPROVINCIES.


        :param provincia_id: The provincia_id of this ResponseGetProvinciaDataPROVINCIES.
        :type provincia_id: int
        """

        self._provincia_id = provincia_id

    @property
    def provincia(self) -> str:
        """Gets the provincia of this ResponseGetProvinciaDataPROVINCIES.


        :return: The provincia of this ResponseGetProvinciaDataPROVINCIES.
        :rtype: str
        """
        return self._provincia

    @provincia.setter
    def provincia(self, provincia: str):
        """Sets the provincia of this ResponseGetProvinciaDataPROVINCIES.


        :param provincia: The provincia of this ResponseGetProvinciaDataPROVINCIES.
        :type provincia: str
        """

        self._provincia = provincia