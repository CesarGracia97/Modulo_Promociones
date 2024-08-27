# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class ResponseServiciosDataSERVICIOS(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, servicios: str=None):  # noqa: E501
        """ResponseServiciosDataSERVICIOS - a model defined in Swagger

        :param servicios: The servicios of this ResponseServiciosDataSERVICIOS.  # noqa: E501
        :type servicios: str
        """
        self.swagger_types = {
            'servicios': str
        }

        self.attribute_map = {
            'servicios': 'SERVICIOS'
        }
        self._servicios = servicios

    @classmethod
    def from_dict(cls, dikt) -> 'ResponseServiciosDataSERVICIOS':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ResponseServicios_data_SERVICIOS of this ResponseServiciosDataSERVICIOS.  # noqa: E501
        :rtype: ResponseServiciosDataSERVICIOS
        """
        return util.deserialize_model(dikt, cls)

    @property
    def servicios(self) -> str:
        """Gets the servicios of this ResponseServiciosDataSERVICIOS.


        :return: The servicios of this ResponseServiciosDataSERVICIOS.
        :rtype: str
        """
        return self._servicios

    @servicios.setter
    def servicios(self, servicios: str):
        """Sets the servicios of this ResponseServiciosDataSERVICIOS.


        :param servicios: The servicios of this ResponseServiciosDataSERVICIOS.
        :type servicios: str
        """

        self._servicios = servicios
