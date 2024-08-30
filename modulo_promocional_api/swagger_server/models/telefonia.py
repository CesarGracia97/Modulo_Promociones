# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.body_producto_adicional import BodyProductoAdicional  # noqa: F401,E501
from swagger_server import util


class TELEFONIA(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, producto_adicional: str=None, cantidad: int=None, precio_referencial: float=None, precio_promocional: float=None, mes_inicio: int=None, mes_fin: str=None, plan: int=None):  # noqa: E501
        """TELEFONIA - a model defined in Swagger

        :param producto_adicional: The producto_adicional of this TELEFONIA.  # noqa: E501
        :type producto_adicional: str
        :param cantidad: The cantidad of this TELEFONIA.  # noqa: E501
        :type cantidad: int
        :param precio_referencial: The precio_referencial of this TELEFONIA.  # noqa: E501
        :type precio_referencial: float
        :param precio_promocional: The precio_promocional of this TELEFONIA.  # noqa: E501
        :type precio_promocional: float
        :param mes_inicio: The mes_inicio of this TELEFONIA.  # noqa: E501
        :type mes_inicio: int
        :param mes_fin: The mes_fin of this TELEFONIA.  # noqa: E501
        :type mes_fin: str
        :param plan: The plan of this TELEFONIA.  # noqa: E501
        :type plan: int
        """
        self.swagger_types = {
            'producto_adicional': str,
            'cantidad': int,
            'precio_referencial': float,
            'precio_promocional': float,
            'mes_inicio': int,
            'mes_fin': str,
            'plan': int
        }

        self.attribute_map = {
            'producto_adicional': 'Producto Adicional',
            'cantidad': 'Cantidad',
            'precio_referencial': 'Precio Referencial',
            'precio_promocional': 'Precio Promocional',
            'mes_inicio': 'Mes Inicio',
            'mes_fin': 'Mes Fin',
            'plan': 'Plan'
        }
        self._producto_adicional = producto_adicional
        self._cantidad = cantidad
        self._precio_referencial = precio_referencial
        self._precio_promocional = precio_promocional
        self._mes_inicio = mes_inicio
        self._mes_fin = mes_fin
        self._plan = plan

    @classmethod
    def from_dict(cls, dikt) -> 'TELEFONIA':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The TELEFONIA of this TELEFONIA.  # noqa: E501
        :rtype: TELEFONIA
        """
        return util.deserialize_model(dikt, cls)

    @property
    def producto_adicional(self) -> str:
        """Gets the producto_adicional of this TELEFONIA.


        :return: The producto_adicional of this TELEFONIA.
        :rtype: str
        """
        return self._producto_adicional

    @producto_adicional.setter
    def producto_adicional(self, producto_adicional: str):
        """Sets the producto_adicional of this TELEFONIA.


        :param producto_adicional: The producto_adicional of this TELEFONIA.
        :type producto_adicional: str
        """
        if producto_adicional is None:
            raise ValueError("Invalid value for `producto_adicional`, must not be `None`")  # noqa: E501

        self._producto_adicional = producto_adicional

    @property
    def cantidad(self) -> int:
        """Gets the cantidad of this TELEFONIA.


        :return: The cantidad of this TELEFONIA.
        :rtype: int
        """
        return self._cantidad

    @cantidad.setter
    def cantidad(self, cantidad: int):
        """Sets the cantidad of this TELEFONIA.


        :param cantidad: The cantidad of this TELEFONIA.
        :type cantidad: int
        """
        if cantidad is None:
            raise ValueError("Invalid value for `cantidad`, must not be `None`")  # noqa: E501

        self._cantidad = cantidad

    @property
    def precio_referencial(self) -> float:
        """Gets the precio_referencial of this TELEFONIA.


        :return: The precio_referencial of this TELEFONIA.
        :rtype: float
        """
        return self._precio_referencial

    @precio_referencial.setter
    def precio_referencial(self, precio_referencial: float):
        """Sets the precio_referencial of this TELEFONIA.


        :param precio_referencial: The precio_referencial of this TELEFONIA.
        :type precio_referencial: float
        """
        if precio_referencial is None:
            raise ValueError("Invalid value for `precio_referencial`, must not be `None`")  # noqa: E501

        self._precio_referencial = precio_referencial

    @property
    def precio_promocional(self) -> float:
        """Gets the precio_promocional of this TELEFONIA.


        :return: The precio_promocional of this TELEFONIA.
        :rtype: float
        """
        return self._precio_promocional

    @precio_promocional.setter
    def precio_promocional(self, precio_promocional: float):
        """Sets the precio_promocional of this TELEFONIA.


        :param precio_promocional: The precio_promocional of this TELEFONIA.
        :type precio_promocional: float
        """
        if precio_promocional is None:
            raise ValueError("Invalid value for `precio_promocional`, must not be `None`")  # noqa: E501

        self._precio_promocional = precio_promocional

    @property
    def mes_inicio(self) -> int:
        """Gets the mes_inicio of this TELEFONIA.


        :return: The mes_inicio of this TELEFONIA.
        :rtype: int
        """
        return self._mes_inicio

    @mes_inicio.setter
    def mes_inicio(self, mes_inicio: int):
        """Sets the mes_inicio of this TELEFONIA.


        :param mes_inicio: The mes_inicio of this TELEFONIA.
        :type mes_inicio: int
        """
        if mes_inicio is None:
            raise ValueError("Invalid value for `mes_inicio`, must not be `None`")  # noqa: E501

        self._mes_inicio = mes_inicio

    @property
    def mes_fin(self) -> str:
        """Gets the mes_fin of this TELEFONIA.


        :return: The mes_fin of this TELEFONIA.
        :rtype: str
        """
        return self._mes_fin

    @mes_fin.setter
    def mes_fin(self, mes_fin: str):
        """Sets the mes_fin of this TELEFONIA.


        :param mes_fin: The mes_fin of this TELEFONIA.
        :type mes_fin: str
        """
        if mes_fin is None:
            raise ValueError("Invalid value for `mes_fin`, must not be `None`")  # noqa: E501

        self._mes_fin = mes_fin

    @property
    def plan(self) -> int:
        """Gets the plan of this TELEFONIA.


        :return: The plan of this TELEFONIA.
        :rtype: int
        """
        return self._plan

    @plan.setter
    def plan(self, plan: int):
        """Sets the plan of this TELEFONIA.


        :param plan: The plan of this TELEFONIA.
        :type plan: int
        """
        if plan is None:
            raise ValueError("Invalid value for `plan`, must not be `None`")  # noqa: E501

        self._plan = plan
