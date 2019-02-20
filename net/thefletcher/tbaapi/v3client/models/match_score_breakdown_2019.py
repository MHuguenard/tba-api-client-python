# coding: utf-8

"""
    The Blue Alliance API v3

    # Overview    Information and statistics about FIRST Robotics Competition teams and events.   # Authentication   All endpoints require an Auth Key to be passed in the header `X-TBA-Auth-Key`. If you do not have an auth key yet, you can obtain one from your [Account Page](/account).    A `User-Agent` header may need to be set to prevent a 403 Unauthorized error.

    OpenAPI spec version: 3.04.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class MatchScoreBreakdown2019(object):
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
        'blue': 'MatchScoreBreakdown2019Alliance',
        'red': 'MatchScoreBreakdown2019Alliance'
    }

    attribute_map = {
        'blue': 'blue',
        'red': 'red'
    }

    def __init__(self, blue=None, red=None):
        """
        MatchScoreBreakdown2019 - a model defined in Swagger
        """

        self._blue = None
        self._red = None

        if blue is not None:
          self.blue = blue
        if red is not None:
          self.red = red

    @property
    def blue(self):
        """
        Gets the blue of this MatchScoreBreakdown2019.

        :return: The blue of this MatchScoreBreakdown2019.
        :rtype: MatchScoreBreakdown2019Alliance
        """
        return self._blue

    @blue.setter
    def blue(self, blue):
        """
        Sets the blue of this MatchScoreBreakdown2019.

        :param blue: The blue of this MatchScoreBreakdown2019.
        :type: MatchScoreBreakdown2019Alliance
        """

        self._blue = blue

    @property
    def red(self):
        """
        Gets the red of this MatchScoreBreakdown2019.

        :return: The red of this MatchScoreBreakdown2019.
        :rtype: MatchScoreBreakdown2019Alliance
        """
        return self._red

    @red.setter
    def red(self, red):
        """
        Sets the red of this MatchScoreBreakdown2019.

        :param red: The red of this MatchScoreBreakdown2019.
        :type: MatchScoreBreakdown2019Alliance
        """

        self._red = red

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
        if not isinstance(other, MatchScoreBreakdown2019):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
