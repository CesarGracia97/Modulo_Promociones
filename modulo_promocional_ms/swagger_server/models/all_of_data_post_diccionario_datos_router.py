# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.data_router import DataROUTER  # noqa: F401,E501
from swagger_server import util


class AllOfDataPostDiccionarioDatosRouter(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, modelo: int=None, producto_adicional: str=None, cantidad: int=None, precio_referencial: float=None, precio_promocional: float=None, mes_inicio: int=None, mes_fin: str=None):  # noqa: E501
        """AllOfDataPostDiccionarioDatosRouter - a model defined in Swagger

        :param modelo: The modelo of this AllOfDataPostDiccionarioDatosRouter.  # noqa: E501
        :type modelo: int
        :param producto_adicional: The producto_adicional of this AllOfDataPostDiccionarioDatosRouter.  # noqa: E501
        :type producto_adicional: str
        :param cantidad: The cantidad of this AllOfDataPostDiccionarioDatosRouter.  # noqa: E501
        :type cantidad: int
        :param precio_referencial: The precio_referencial of this AllOfDataPostDiccionarioDatosRouter.  # noqa: E501
        :type precio_referencial: float
        :param precio_promocional: The precio_promocional of this AllOfDataPostDiccionarioDatosRouter.  # noqa: E501
        :type precio_promocional: float
        :param mes_inicio: The mes_inicio of this AllOfDataPostDiccionarioDatosRouter.  # noqa: E501
        :type mes_inicio: int
        :param mes_fin: The mes_fin of this AllOfDataPostDiccionarioDatosRouter.  # noqa: E501
        :type mes_fin: str
        """
        self.swagger_types = {
            'modelo': int,
            'producto_adicional': str,
            'cantidad': int,
            'precio_referencial': float,
            'precio_promocional': float,
            'mes_inicio': int,
            'mes_fin': str
        }

        self.attribute_map = {
            'modelo': 'Modelo',
            'producto_adicional': 'Producto Adicional',
            'cantidad': 'Cantidad',
            'precio_referencial': 'Precio Referencial',
            'precio_promocional': 'Precio Promocional',
            'mes_inicio': 'Mes Inicio',
            'mes_fin': 'Mes Fin'
        }
        self._modelo = modelo
        self._producto_adicional = producto_adicional
        self._cantidad = cantidad
        self._precio_referencial = precio_referencial
        self._precio_promocional = precio_promocional
        self._mes_inicio = mes_inicio
        self._mes_fin = mes_fin

    @classmethod
    def from_dict(cls, dikt) -> 'AllOfDataPostDiccionarioDatosRouter':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AllOfDataPostDiccionarioDatosRouter of this AllOfDataPostDiccionarioDatosRouter.  # noqa: E501
        :rtype: AllOfDataPostDiccionarioDatosRouter
        """
        return util.deserialize_model(dikt, cls)

    @property
    def modelo(self) -> int:
        """Gets the modelo of this AllOfDataPostDiccionarioDatosRouter.


        :return: The modelo of this AllOfDataPostDiccionarioDatosRouter.
        :rtype: int
        """
        return self._modelo

    @modelo.setter
    def modelo(self, modelo: int):
        """Sets the modelo of this AllOfDataPostDiccionarioDatosRouter.


        :param modelo: The modelo of this AllOfDataPostDiccionarioDatosRouter.
        :type modelo: int
        """
        if modelo is None:
            raise ValueError("Invalid value for `modelo`, must not be `None`")  # noqa: E501

        self._modelo = modelo

    @property
    def producto_adicional(self) -> str:
        """Gets the producto_adicional of this AllOfDataPostDiccionarioDatosRouter.


        :return: The producto_adicional of this AllOfDataPostDiccionarioDatosRouter.
        :rtype: str
        """
        return self._producto_adicional

    @producto_adicional.setter
    def producto_adicional(self, producto_adicional: str):
        """Sets the producto_adicional of this AllOfDataPostDiccionarioDatosRouter.


        :param producto_adicional: The producto_adicional of this AllOfDataPostDiccionarioDatosRouter.
        :type producto_adicional: str
        """

        self._producto_adicional = producto_adicional

    @property
    def cantidad(self) -> int:
        """Gets the cantidad of this AllOfDataPostDiccionarioDatosRouter.


        :return: The cantidad of this AllOfDataPostDiccionarioDatosRouter.
        :rtype: int
        """
        return self._cantidad

    @cantidad.setter
    def cantidad(self, cantidad: int):
        """Sets the cantidad of this AllOfDataPostDiccionarioDatosRouter.


        :param cantidad: The cantidad of this AllOfDataPostDiccionarioDatosRouter.
        :type cantidad: int
        """

        self._cantidad = cantidad

    @property
    def precio_referencial(self) -> float:
        """Gets the precio_referencial of this AllOfDataPostDiccionarioDatosRouter.


        :return: The precio_referencial of this AllOfDataPostDiccionarioDatosRouter.
        :rtype: float
        """
        return self._precio_referencial

    @precio_referencial.setter
    def precio_referencial(self, precio_referencial: float):
        """Sets the precio_referencial of this AllOfDataPostDiccionarioDatosRouter.


        :param precio_referencial: The precio_referencial of this AllOfDataPostDiccionarioDatosRouter.
        :type precio_referencial: float
        """

        self._precio_referencial = precio_referencial

    @property
    def precio_promocional(self) -> float:
        """Gets the precio_promocional of this AllOfDataPostDiccionarioDatosRouter.


        :return: The precio_promocional of this AllOfDataPostDiccionarioDatosRouter.
        :rtype: float
        """
        return self._precio_promocional

    @precio_promocional.setter
    def precio_promocional(self, precio_promocional: float):
        """Sets the precio_promocional of this AllOfDataPostDiccionarioDatosRouter.


        :param precio_promocional: The precio_promocional of this AllOfDataPostDiccionarioDatosRouter.
        :type precio_promocional: float
        """

        self._precio_promocional = precio_promocional

    @property
    def mes_inicio(self) -> int:
        """Gets the mes_inicio of this AllOfDataPostDiccionarioDatosRouter.


        :return: The mes_inicio of this AllOfDataPostDiccionarioDatosRouter.
        :rtype: int
        """
        return self._mes_inicio

    @mes_inicio.setter
    def mes_inicio(self, mes_inicio: int):
        """Sets the mes_inicio of this AllOfDataPostDiccionarioDatosRouter.


        :param mes_inicio: The mes_inicio of this AllOfDataPostDiccionarioDatosRouter.
        :type mes_inicio: int
        """

        self._mes_inicio = mes_inicio

    @property
    def mes_fin(self) -> str:
        """Gets the mes_fin of this AllOfDataPostDiccionarioDatosRouter.


        :return: The mes_fin of this AllOfDataPostDiccionarioDatosRouter.
        :rtype: str
        """
        return self._mes_fin

    @mes_fin.setter
    def mes_fin(self, mes_fin: str):
        """Sets the mes_fin of this AllOfDataPostDiccionarioDatosRouter.


        :param mes_fin: The mes_fin of this AllOfDataPostDiccionarioDatosRouter.
        :type mes_fin: str
        """

        self._mes_fin = mes_fin