# coding: utf-8

"""
    The Blue Alliance API v3

    # Overview    Information and statistics about FIRST Robotics Competition teams and events. If you are looking for the old version (v2) of the API, documentation can be found [here](/apidocs/v2).   # Authentication   All endpoints require an Auth Key to be passed in the header `X-TBA-Auth-Key`. If you do not have an auth key yet, you can obtain one from your [Account Page](/account).    A `User-Agent` header may need to be set to prevent a 403 Unauthorized error.

    OpenAPI spec version: 3.0.5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class EliminationAllianceStatus(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'current_level_record': 'WLTRecord',
        'level': 'str',
        'playoff_average': 'float',
        'record': 'WLTRecord',
        'status': 'str'
    }

    attribute_map = {
        'current_level_record': 'current_level_record',
        'level': 'level',
        'playoff_average': 'playoff_average',
        'record': 'record',
        'status': 'status'
    }

    def __init__(self, current_level_record=None, level=None, playoff_average=None, record=None, status=None):
        """
        EliminationAllianceStatus - a model defined in Swagger
        """

        self._current_level_record = None
        self._level = None
        self._playoff_average = None
        self._record = None
        self._status = None

        if current_level_record is not None:
          self.current_level_record = current_level_record
        if level is not None:
          self.level = level
        if playoff_average is not None:
          self.playoff_average = playoff_average
        if record is not None:
          self.record = record
        if status is not None:
          self.status = status

    @property
    def current_level_record(self):
        """
        Gets the current_level_record of this EliminationAllianceStatus.

        :return: The current_level_record of this EliminationAllianceStatus.
        :rtype: WLTRecord
        """
        return self._current_level_record

    @current_level_record.setter
    def current_level_record(self, current_level_record):
        """
        Sets the current_level_record of this EliminationAllianceStatus.

        :param current_level_record: The current_level_record of this EliminationAllianceStatus.
        :type: WLTRecord
        """

        self._current_level_record = current_level_record

    @property
    def level(self):
        """
        Gets the level of this EliminationAllianceStatus.

        :return: The level of this EliminationAllianceStatus.
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        """
        Sets the level of this EliminationAllianceStatus.

        :param level: The level of this EliminationAllianceStatus.
        :type: str
        """

        self._level = level

    @property
    def playoff_average(self):
        """
        Gets the playoff_average of this EliminationAllianceStatus.

        :return: The playoff_average of this EliminationAllianceStatus.
        :rtype: float
        """
        return self._playoff_average

    @playoff_average.setter
    def playoff_average(self, playoff_average):
        """
        Sets the playoff_average of this EliminationAllianceStatus.

        :param playoff_average: The playoff_average of this EliminationAllianceStatus.
        :type: float
        """

        self._playoff_average = playoff_average

    @property
    def record(self):
        """
        Gets the record of this EliminationAllianceStatus.

        :return: The record of this EliminationAllianceStatus.
        :rtype: WLTRecord
        """
        return self._record

    @record.setter
    def record(self, record):
        """
        Sets the record of this EliminationAllianceStatus.

        :param record: The record of this EliminationAllianceStatus.
        :type: WLTRecord
        """

        self._record = record

    @property
    def status(self):
        """
        Gets the status of this EliminationAllianceStatus.

        :return: The status of this EliminationAllianceStatus.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this EliminationAllianceStatus.

        :param status: The status of this EliminationAllianceStatus.
        :type: str
        """

        self._status = status

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, EliminationAllianceStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
