# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class ResponseGetTecnologiasTECNOLOGIAS(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, tecnologia: str=None):  # noqa: E501
        """ResponseGetTecnologiasTECNOLOGIAS - a model defined in Swagger

        :param tecnologia: The tecnologia of this ResponseGetTecnologiasTECNOLOGIAS.  # noqa: E501
        :type tecnologia: str
        """
        self.swagger_types = {
            'tecnologia': str
        }

        self.attribute_map = {
            'tecnologia': 'TECNOLOGIA'
        }
        self._tecnologia = tecnologia

    @classmethod
    def from_dict(cls, dikt) -> 'ResponseGetTecnologiasTECNOLOGIAS':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ResponseGetTecnologias_TECNOLOGIAS of this ResponseGetTecnologiasTECNOLOGIAS.  # noqa: E501
        :rtype: ResponseGetTecnologiasTECNOLOGIAS
        """
        return util.deserialize_model(dikt, cls)

    @property
    def tecnologia(self) -> str:
        """Gets the tecnologia of this ResponseGetTecnologiasTECNOLOGIAS.


        :return: The tecnologia of this ResponseGetTecnologiasTECNOLOGIAS.
        :rtype: str
        """
        return self._tecnologia

    @tecnologia.setter
    def tecnologia(self, tecnologia: str):
        """Sets the tecnologia of this ResponseGetTecnologiasTECNOLOGIAS.


        :param tecnologia: The tecnologia of this ResponseGetTecnologiasTECNOLOGIAS.
        :type tecnologia: str
        """

        self._tecnologia = tecnologia