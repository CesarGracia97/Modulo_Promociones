# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class ResponseGetCiudadDataCITIES(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, ciudad_id: int=None, ciudad: str=None, provincia: str=None):  # noqa: E501
        """ResponseGetCiudadDataCITIES - a model defined in Swagger

        :param ciudad_id: The ciudad_id of this ResponseGetCiudadDataCITIES.  # noqa: E501
        :type ciudad_id: int
        :param ciudad: The ciudad of this ResponseGetCiudadDataCITIES.  # noqa: E501
        :type ciudad: str
        :param provincia: The provincia of this ResponseGetCiudadDataCITIES.  # noqa: E501
        :type provincia: str
        """
        self.swagger_types = {
            'ciudad_id': int,
            'ciudad': str,
            'provincia': str
        }

        self.attribute_map = {
            'ciudad_id': 'CIUDAD_ID',
            'ciudad': 'CIUDAD',
            'provincia': 'PROVINCIA'
        }
        self._ciudad_id = ciudad_id
        self._ciudad = ciudad
        self._provincia = provincia

    @classmethod
    def from_dict(cls, dikt) -> 'ResponseGetCiudadDataCITIES':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ResponseGetCiudad_data_CITIES of this ResponseGetCiudadDataCITIES.  # noqa: E501
        :rtype: ResponseGetCiudadDataCITIES
        """
        return util.deserialize_model(dikt, cls)

    @property
    def ciudad_id(self) -> int:
        """Gets the ciudad_id of this ResponseGetCiudadDataCITIES.


        :return: The ciudad_id of this ResponseGetCiudadDataCITIES.
        :rtype: int
        """
        return self._ciudad_id

    @ciudad_id.setter
    def ciudad_id(self, ciudad_id: int):
        """Sets the ciudad_id of this ResponseGetCiudadDataCITIES.


        :param ciudad_id: The ciudad_id of this ResponseGetCiudadDataCITIES.
        :type ciudad_id: int
        """

        self._ciudad_id = ciudad_id

    @property
    def ciudad(self) -> str:
        """Gets the ciudad of this ResponseGetCiudadDataCITIES.


        :return: The ciudad of this ResponseGetCiudadDataCITIES.
        :rtype: str
        """
        return self._ciudad

    @ciudad.setter
    def ciudad(self, ciudad: str):
        """Sets the ciudad of this ResponseGetCiudadDataCITIES.


        :param ciudad: The ciudad of this ResponseGetCiudadDataCITIES.
        :type ciudad: str
        """

        self._ciudad = ciudad

    @property
    def provincia(self) -> str:
        """Gets the provincia of this ResponseGetCiudadDataCITIES.


        :return: The provincia of this ResponseGetCiudadDataCITIES.
        :rtype: str
        """
        return self._provincia

    @provincia.setter
    def provincia(self, provincia: str):
        """Sets the provincia of this ResponseGetCiudadDataCITIES.


        :param provincia: The provincia of this ResponseGetCiudadDataCITIES.
        :type provincia: str
        """

        self._provincia = provincia
