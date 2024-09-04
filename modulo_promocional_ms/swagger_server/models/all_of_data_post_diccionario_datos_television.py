# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.data_television import DataTELEVISION  # noqa: F401,E501
from swagger_server import util


class AllOfDataPostDiccionarioDatosTelevision(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, plan: int=None, producto_adicional: str=None, cantidad: int=None, precio_referencial: float=None, precio_promocional: float=None, mes_inicio: int=None, mes_fin: str=None):  # noqa: E501
        """AllOfDataPostDiccionarioDatosTelevision - a model defined in Swagger

        :param plan: The plan of this AllOfDataPostDiccionarioDatosTelevision.  # noqa: E501
        :type plan: int
        :param producto_adicional: The producto_adicional of this AllOfDataPostDiccionarioDatosTelevision.  # noqa: E501
        :type producto_adicional: str
        :param cantidad: The cantidad of this AllOfDataPostDiccionarioDatosTelevision.  # noqa: E501
        :type cantidad: int
        :param precio_referencial: The precio_referencial of this AllOfDataPostDiccionarioDatosTelevision.  # noqa: E501
        :type precio_referencial: float
        :param precio_promocional: The precio_promocional of this AllOfDataPostDiccionarioDatosTelevision.  # noqa: E501
        :type precio_promocional: float
        :param mes_inicio: The mes_inicio of this AllOfDataPostDiccionarioDatosTelevision.  # noqa: E501
        :type mes_inicio: int
        :param mes_fin: The mes_fin of this AllOfDataPostDiccionarioDatosTelevision.  # noqa: E501
        :type mes_fin: str
        """
        self.swagger_types = {
            'plan': int,
            'producto_adicional': str,
            'cantidad': int,
            'precio_referencial': float,
            'precio_promocional': float,
            'mes_inicio': int,
            'mes_fin': str
        }

        self.attribute_map = {
            'plan': 'Plan',
            'producto_adicional': 'Producto Adicional',
            'cantidad': 'Cantidad',
            'precio_referencial': 'Precio Referencial',
            'precio_promocional': 'Precio Promocional',
            'mes_inicio': 'Mes Inicio',
            'mes_fin': 'Mes Fin'
        }
        self._plan = plan
        self._producto_adicional = producto_adicional
        self._cantidad = cantidad
        self._precio_referencial = precio_referencial
        self._precio_promocional = precio_promocional
        self._mes_inicio = mes_inicio
        self._mes_fin = mes_fin

    @classmethod
    def from_dict(cls, dikt) -> 'AllOfDataPostDiccionarioDatosTelevision':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AllOfDataPostDiccionarioDatosTelevision of this AllOfDataPostDiccionarioDatosTelevision.  # noqa: E501
        :rtype: AllOfDataPostDiccionarioDatosTelevision
        """
        return util.deserialize_model(dikt, cls)

    @property
    def plan(self) -> int:
        """Gets the plan of this AllOfDataPostDiccionarioDatosTelevision.


        :return: The plan of this AllOfDataPostDiccionarioDatosTelevision.
        :rtype: int
        """
        return self._plan

    @plan.setter
    def plan(self, plan: int):
        """Sets the plan of this AllOfDataPostDiccionarioDatosTelevision.


        :param plan: The plan of this AllOfDataPostDiccionarioDatosTelevision.
        :type plan: int
        """
        if plan is None:
            raise ValueError("Invalid value for `plan`, must not be `None`")  # noqa: E501

        self._plan = plan

    @property
    def producto_adicional(self) -> str:
        """Gets the producto_adicional of this AllOfDataPostDiccionarioDatosTelevision.


        :return: The producto_adicional of this AllOfDataPostDiccionarioDatosTelevision.
        :rtype: str
        """
        return self._producto_adicional

    @producto_adicional.setter
    def producto_adicional(self, producto_adicional: str):
        """Sets the producto_adicional of this AllOfDataPostDiccionarioDatosTelevision.


        :param producto_adicional: The producto_adicional of this AllOfDataPostDiccionarioDatosTelevision.
        :type producto_adicional: str
        """

        self._producto_adicional = producto_adicional

    @property
    def cantidad(self) -> int:
        """Gets the cantidad of this AllOfDataPostDiccionarioDatosTelevision.


        :return: The cantidad of this AllOfDataPostDiccionarioDatosTelevision.
        :rtype: int
        """
        return self._cantidad

    @cantidad.setter
    def cantidad(self, cantidad: int):
        """Sets the cantidad of this AllOfDataPostDiccionarioDatosTelevision.


        :param cantidad: The cantidad of this AllOfDataPostDiccionarioDatosTelevision.
        :type cantidad: int
        """

        self._cantidad = cantidad

    @property
    def precio_referencial(self) -> float:
        """Gets the precio_referencial of this AllOfDataPostDiccionarioDatosTelevision.


        :return: The precio_referencial of this AllOfDataPostDiccionarioDatosTelevision.
        :rtype: float
        """
        return self._precio_referencial

    @precio_referencial.setter
    def precio_referencial(self, precio_referencial: float):
        """Sets the precio_referencial of this AllOfDataPostDiccionarioDatosTelevision.


        :param precio_referencial: The precio_referencial of this AllOfDataPostDiccionarioDatosTelevision.
        :type precio_referencial: float
        """

        self._precio_referencial = precio_referencial

    @property
    def precio_promocional(self) -> float:
        """Gets the precio_promocional of this AllOfDataPostDiccionarioDatosTelevision.


        :return: The precio_promocional of this AllOfDataPostDiccionarioDatosTelevision.
        :rtype: float
        """
        return self._precio_promocional

    @precio_promocional.setter
    def precio_promocional(self, precio_promocional: float):
        """Sets the precio_promocional of this AllOfDataPostDiccionarioDatosTelevision.


        :param precio_promocional: The precio_promocional of this AllOfDataPostDiccionarioDatosTelevision.
        :type precio_promocional: float
        """

        self._precio_promocional = precio_promocional

    @property
    def mes_inicio(self) -> int:
        """Gets the mes_inicio of this AllOfDataPostDiccionarioDatosTelevision.


        :return: The mes_inicio of this AllOfDataPostDiccionarioDatosTelevision.
        :rtype: int
        """
        return self._mes_inicio

    @mes_inicio.setter
    def mes_inicio(self, mes_inicio: int):
        """Sets the mes_inicio of this AllOfDataPostDiccionarioDatosTelevision.


        :param mes_inicio: The mes_inicio of this AllOfDataPostDiccionarioDatosTelevision.
        :type mes_inicio: int
        """

        self._mes_inicio = mes_inicio

    @property
    def mes_fin(self) -> str:
        """Gets the mes_fin of this AllOfDataPostDiccionarioDatosTelevision.


        :return: The mes_fin of this AllOfDataPostDiccionarioDatosTelevision.
        :rtype: str
        """
        return self._mes_fin

    @mes_fin.setter
    def mes_fin(self, mes_fin: str):
        """Sets the mes_fin of this AllOfDataPostDiccionarioDatosTelevision.


        :param mes_fin: The mes_fin of this AllOfDataPostDiccionarioDatosTelevision.
        :type mes_fin: str
        """

        self._mes_fin = mes_fin
