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


class EventDistrictPoints(object):
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
        'points': 'dict(str, EventDistrictPointsPoints)',
        'tiebreakers': 'dict(str, EventDistrictPointsTiebreakers)'
    }

    attribute_map = {
        'points': 'points',
        'tiebreakers': 'tiebreakers'
    }

    def __init__(self, points=None, tiebreakers=None):
        """
        EventDistrictPoints - a model defined in Swagger
        """

        self._points = None
        self._tiebreakers = None

        self.points = points
        if tiebreakers is not None:
          self.tiebreakers = tiebreakers

    @property
    def points(self):
        """
        Gets the points of this EventDistrictPoints.
        Points gained for each team at the event. Stored as a key-value pair with the team key as the key, and an object describing the points as its value.

        :return: The points of this EventDistrictPoints.
        :rtype: dict(str, EventDistrictPointsPoints)
        """
        return self._points

    @points.setter
    def points(self, points):
        """
        Sets the points of this EventDistrictPoints.
        Points gained for each team at the event. Stored as a key-value pair with the team key as the key, and an object describing the points as its value.

        :param points: The points of this EventDistrictPoints.
        :type: dict(str, EventDistrictPointsPoints)
        """
        if points is None:
            raise ValueError("Invalid value for `points`, must not be `None`")

        self._points = points

    @property
    def tiebreakers(self):
        """
        Gets the tiebreakers of this EventDistrictPoints.
        Tiebreaker values for each team at the event. Stored as a key-value pair with the team key as the key, and an object describing the tiebreaker elements as its value.

        :return: The tiebreakers of this EventDistrictPoints.
        :rtype: dict(str, EventDistrictPointsTiebreakers)
        """
        return self._tiebreakers

    @tiebreakers.setter
    def tiebreakers(self, tiebreakers):
        """
        Sets the tiebreakers of this EventDistrictPoints.
        Tiebreaker values for each team at the event. Stored as a key-value pair with the team key as the key, and an object describing the tiebreaker elements as its value.

        :param tiebreakers: The tiebreakers of this EventDistrictPoints.
        :type: dict(str, EventDistrictPointsTiebreakers)
        """

        self._tiebreakers = tiebreakers

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
        if not isinstance(other, EventDistrictPoints):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
