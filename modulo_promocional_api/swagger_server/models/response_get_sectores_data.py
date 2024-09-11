# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.response_get_sectores_data_sectors import ResponseGetSectoresDataSECTORS  # noqa: F401,E501
from swagger_server import util


class ResponseGetSectoresData(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, error_code: int=None, internal_transaction_id: str=None, external_transaction_id: str=None, message: str=None, sectors: ResponseGetSectoresDataSECTORS=None, sectorsx_city: ResponseGetSectoresDataSECTORS=None):  # noqa: E501
        """ResponseGetSectoresData - a model defined in Swagger

        :param error_code: The error_code of this ResponseGetSectoresData.  # noqa: E501
        :type error_code: int
        :param internal_transaction_id: The internal_transaction_id of this ResponseGetSectoresData.  # noqa: E501
        :type internal_transaction_id: str
        :param external_transaction_id: The external_transaction_id of this ResponseGetSectoresData.  # noqa: E501
        :type external_transaction_id: str
        :param message: The message of this ResponseGetSectoresData.  # noqa: E501
        :type message: str
        :param sectors: The sectors of this ResponseGetSectoresData.  # noqa: E501
        :type sectors: ResponseGetSectoresDataSECTORS
        :param sectorsx_city: The sectorsx_city of this ResponseGetSectoresData.  # noqa: E501
        :type sectorsx_city: ResponseGetSectoresDataSECTORS
        """
        self.swagger_types = {
            'error_code': int,
            'internal_transaction_id': str,
            'external_transaction_id': str,
            'message': str,
            'sectors': ResponseGetSectoresDataSECTORS,
            'sectorsx_city': ResponseGetSectoresDataSECTORS
        }

        self.attribute_map = {
            'error_code': 'errorCode',
            'internal_transaction_id': 'internalTransactionId',
            'external_transaction_id': 'externalTransactionId',
            'message': 'message',
            'sectors': 'SECTORS',
            'sectorsx_city': 'SECTORSxCITY'
        }
        self._error_code = error_code
        self._internal_transaction_id = internal_transaction_id
        self._external_transaction_id = external_transaction_id
        self._message = message
        self._sectors = sectors
        self._sectorsx_city = sectorsx_city

    @classmethod
    def from_dict(cls, dikt) -> 'ResponseGetSectoresData':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ResponseGetSectores_Data of this ResponseGetSectoresData.  # noqa: E501
        :rtype: ResponseGetSectoresData
        """
        return util.deserialize_model(dikt, cls)

    @property
    def error_code(self) -> int:
        """Gets the error_code of this ResponseGetSectoresData.


        :return: The error_code of this ResponseGetSectoresData.
        :rtype: int
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code: int):
        """Sets the error_code of this ResponseGetSectoresData.


        :param error_code: The error_code of this ResponseGetSectoresData.
        :type error_code: int
        """

        self._error_code = error_code

    @property
    def internal_transaction_id(self) -> str:
        """Gets the internal_transaction_id of this ResponseGetSectoresData.


        :return: The internal_transaction_id of this ResponseGetSectoresData.
        :rtype: str
        """
        return self._internal_transaction_id

    @internal_transaction_id.setter
    def internal_transaction_id(self, internal_transaction_id: str):
        """Sets the internal_transaction_id of this ResponseGetSectoresData.


        :param internal_transaction_id: The internal_transaction_id of this ResponseGetSectoresData.
        :type internal_transaction_id: str
        """

        self._internal_transaction_id = internal_transaction_id

    @property
    def external_transaction_id(self) -> str:
        """Gets the external_transaction_id of this ResponseGetSectoresData.


        :return: The external_transaction_id of this ResponseGetSectoresData.
        :rtype: str
        """
        return self._external_transaction_id

    @external_transaction_id.setter
    def external_transaction_id(self, external_transaction_id: str):
        """Sets the external_transaction_id of this ResponseGetSectoresData.


        :param external_transaction_id: The external_transaction_id of this ResponseGetSectoresData.
        :type external_transaction_id: str
        """

        self._external_transaction_id = external_transaction_id

    @property
    def message(self) -> str:
        """Gets the message of this ResponseGetSectoresData.


        :return: The message of this ResponseGetSectoresData.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message: str):
        """Sets the message of this ResponseGetSectoresData.


        :param message: The message of this ResponseGetSectoresData.
        :type message: str
        """

        self._message = message

    @property
    def sectors(self) -> ResponseGetSectoresDataSECTORS:
        """Gets the sectors of this ResponseGetSectoresData.


        :return: The sectors of this ResponseGetSectoresData.
        :rtype: ResponseGetSectoresDataSECTORS
        """
        return self._sectors

    @sectors.setter
    def sectors(self, sectors: ResponseGetSectoresDataSECTORS):
        """Sets the sectors of this ResponseGetSectoresData.


        :param sectors: The sectors of this ResponseGetSectoresData.
        :type sectors: ResponseGetSectoresDataSECTORS
        """

        self._sectors = sectors

    @property
    def sectorsx_city(self) -> ResponseGetSectoresDataSECTORS:
        """Gets the sectorsx_city of this ResponseGetSectoresData.


        :return: The sectorsx_city of this ResponseGetSectoresData.
        :rtype: ResponseGetSectoresDataSECTORS
        """
        return self._sectorsx_city

    @sectorsx_city.setter
    def sectorsx_city(self, sectorsx_city: ResponseGetSectoresDataSECTORS):
        """Sets the sectorsx_city of this ResponseGetSectoresData.


        :param sectorsx_city: The sectorsx_city of this ResponseGetSectoresData.
        :type sectorsx_city: ResponseGetSectoresDataSECTORS
        """

        self._sectorsx_city = sectorsx_city