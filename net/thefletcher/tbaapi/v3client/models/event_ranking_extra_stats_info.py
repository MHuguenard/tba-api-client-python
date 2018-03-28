# coding: utf-8

"""
    The Blue Alliance API v3

    # Overview    Information and statistics about FIRST Robotics Competition teams and events.   # Authentication   All endpoints require an Auth Key to be passed in the header `X-TBA-Auth-Key`. If you do not have an auth key yet, you can obtain one from your [Account Page](/account).    A `User-Agent` header may need to be set to prevent a 403 Unauthorized error.

    OpenAPI spec version: 3.03.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class EventRankingExtraStatsInfo(object):
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
        'name': 'str',
        'precision': 'float'
    }

    attribute_map = {
        'name': 'name',
        'precision': 'precision'
    }

    def __init__(self, name=None, precision=None):
        """
        EventRankingExtraStatsInfo - a model defined in Swagger
        """

        self._name = None
        self._precision = None

        self.name = name
        self.precision = precision

    @property
    def name(self):
        """
        Gets the name of this EventRankingExtraStatsInfo.
        Name of the field used in the `extra_stats` array.

        :return: The name of this EventRankingExtraStatsInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this EventRankingExtraStatsInfo.
        Name of the field used in the `extra_stats` array.

        :param name: The name of this EventRankingExtraStatsInfo.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def precision(self):
        """
        Gets the precision of this EventRankingExtraStatsInfo.
        Integer expressing the number of digits of precision in the number provided in `sort_orders`.

        :return: The precision of this EventRankingExtraStatsInfo.
        :rtype: float
        """
        return self._precision

    @precision.setter
    def precision(self, precision):
        """
        Sets the precision of this EventRankingExtraStatsInfo.
        Integer expressing the number of digits of precision in the number provided in `sort_orders`.

        :param precision: The precision of this EventRankingExtraStatsInfo.
        :type: float
        """
        if precision is None:
            raise ValueError("Invalid value for `precision`, must not be `None`")

        self._precision = precision

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
        if not isinstance(other, EventRankingExtraStatsInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
