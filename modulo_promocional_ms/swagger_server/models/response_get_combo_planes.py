# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.response_get_combo_planes_comboplan import ResponseGetComboPlanesCOMBOPLAN  # noqa: F401,E501
from swagger_server import util


class ResponseGetComboPlanes(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, error_code: int=None, combo_plan: List[ResponseGetComboPlanesCOMBOPLAN]=None, internal_transaction_id: int=None, external_transaction_id: int=None, message: str=None):  # noqa: E501
        """ResponseGetComboPlanes - a model defined in Swagger

        :param error_code: The error_code of this ResponseGetComboPlanes.  # noqa: E501
        :type error_code: int
        :param combo_plan: The combo_plan of this ResponseGetComboPlanes.  # noqa: E501
        :type combo_plan: List[ResponseGetComboPlanesCOMBOPLAN]
        :param internal_transaction_id: The internal_transaction_id of this ResponseGetComboPlanes.  # noqa: E501
        :type internal_transaction_id: int
        :param external_transaction_id: The external_transaction_id of this ResponseGetComboPlanes.  # noqa: E501
        :type external_transaction_id: int
        :param message: The message of this ResponseGetComboPlanes.  # noqa: E501
        :type message: str
        """
        self.swagger_types = {
            'error_code': int,
            'combo_plan': List[ResponseGetComboPlanesCOMBOPLAN],
            'internal_transaction_id': int,
            'external_transaction_id': int,
            'message': str
        }

        self.attribute_map = {
            'error_code': 'errorCode',
            'combo_plan': 'COMBO_PLAN',
            'internal_transaction_id': 'internalTransactionId',
            'external_transaction_id': 'externalTransactionId',
            'message': 'message'
        }
        self._error_code = error_code
        self._combo_plan = combo_plan
        self._internal_transaction_id = internal_transaction_id
        self._external_transaction_id = external_transaction_id
        self._message = message

    @classmethod
    def from_dict(cls, dikt) -> 'ResponseGetComboPlanes':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ResponseGetCombo_Planes of this ResponseGetComboPlanes.  # noqa: E501
        :rtype: ResponseGetComboPlanes
        """
        return util.deserialize_model(dikt, cls)

    @property
    def error_code(self) -> int:
        """Gets the error_code of this ResponseGetComboPlanes.


        :return: The error_code of this ResponseGetComboPlanes.
        :rtype: int
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code: int):
        """Sets the error_code of this ResponseGetComboPlanes.


        :param error_code: The error_code of this ResponseGetComboPlanes.
        :type error_code: int
        """

        self._error_code = error_code

    @property
    def combo_plan(self) -> List[ResponseGetComboPlanesCOMBOPLAN]:
        """Gets the combo_plan of this ResponseGetComboPlanes.


        :return: The combo_plan of this ResponseGetComboPlanes.
        :rtype: List[ResponseGetComboPlanesCOMBOPLAN]
        """
        return self._combo_plan

    @combo_plan.setter
    def combo_plan(self, combo_plan: List[ResponseGetComboPlanesCOMBOPLAN]):
        """Sets the combo_plan of this ResponseGetComboPlanes.


        :param combo_plan: The combo_plan of this ResponseGetComboPlanes.
        :type combo_plan: List[ResponseGetComboPlanesCOMBOPLAN]
        """

        self._combo_plan = combo_plan

    @property
    def internal_transaction_id(self) -> int:
        """Gets the internal_transaction_id of this ResponseGetComboPlanes.


        :return: The internal_transaction_id of this ResponseGetComboPlanes.
        :rtype: int
        """
        return self._internal_transaction_id

    @internal_transaction_id.setter
    def internal_transaction_id(self, internal_transaction_id: int):
        """Sets the internal_transaction_id of this ResponseGetComboPlanes.


        :param internal_transaction_id: The internal_transaction_id of this ResponseGetComboPlanes.
        :type internal_transaction_id: int
        """

        self._internal_transaction_id = internal_transaction_id

    @property
    def external_transaction_id(self) -> int:
        """Gets the external_transaction_id of this ResponseGetComboPlanes.


        :return: The external_transaction_id of this ResponseGetComboPlanes.
        :rtype: int
        """
        return self._external_transaction_id

    @external_transaction_id.setter
    def external_transaction_id(self, external_transaction_id: int):
        """Sets the external_transaction_id of this ResponseGetComboPlanes.


        :param external_transaction_id: The external_transaction_id of this ResponseGetComboPlanes.
        :type external_transaction_id: int
        """

        self._external_transaction_id = external_transaction_id

    @property
    def message(self) -> str:
        """Gets the message of this ResponseGetComboPlanes.


        :return: The message of this ResponseGetComboPlanes.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message: str):
        """Sets the message of this ResponseGetComboPlanes.


        :param message: The message of this ResponseGetComboPlanes.
        :type message: str
        """

        self._message = message