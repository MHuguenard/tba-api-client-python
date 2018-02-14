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


class EventDistrictPointsTiebreakers(object):
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
        'highest_qual_scores': 'list[int]',
        'qual_wins': 'int'
    }

    attribute_map = {
        'highest_qual_scores': 'highest_qual_scores',
        'qual_wins': 'qual_wins'
    }

    def __init__(self, highest_qual_scores=None, qual_wins=None):
        """
        EventDistrictPointsTiebreakers - a model defined in Swagger
        """

        self._highest_qual_scores = None
        self._qual_wins = None

        if highest_qual_scores is not None:
          self.highest_qual_scores = highest_qual_scores
        if qual_wins is not None:
          self.qual_wins = qual_wins

    @property
    def highest_qual_scores(self):
        """
        Gets the highest_qual_scores of this EventDistrictPointsTiebreakers.

        :return: The highest_qual_scores of this EventDistrictPointsTiebreakers.
        :rtype: list[int]
        """
        return self._highest_qual_scores

    @highest_qual_scores.setter
    def highest_qual_scores(self, highest_qual_scores):
        """
        Sets the highest_qual_scores of this EventDistrictPointsTiebreakers.

        :param highest_qual_scores: The highest_qual_scores of this EventDistrictPointsTiebreakers.
        :type: list[int]
        """

        self._highest_qual_scores = highest_qual_scores

    @property
    def qual_wins(self):
        """
        Gets the qual_wins of this EventDistrictPointsTiebreakers.

        :return: The qual_wins of this EventDistrictPointsTiebreakers.
        :rtype: int
        """
        return self._qual_wins

    @qual_wins.setter
    def qual_wins(self, qual_wins):
        """
        Sets the qual_wins of this EventDistrictPointsTiebreakers.

        :param qual_wins: The qual_wins of this EventDistrictPointsTiebreakers.
        :type: int
        """

        self._qual_wins = qual_wins

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
        if not isinstance(other, EventDistrictPointsTiebreakers):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
