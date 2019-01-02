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


class TeamEventStatusRank(object):
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
        'num_teams': 'int',
        'ranking': 'TeamEventStatusRankRanking',
        'sort_order_info': 'list[TeamEventStatusRankSortOrderInfo]',
        'status': 'str'
    }

    attribute_map = {
        'num_teams': 'num_teams',
        'ranking': 'ranking',
        'sort_order_info': 'sort_order_info',
        'status': 'status'
    }

    def __init__(self, num_teams=None, ranking=None, sort_order_info=None, status=None):
        """
        TeamEventStatusRank - a model defined in Swagger
        """

        self._num_teams = None
        self._ranking = None
        self._sort_order_info = None
        self._status = None

        if num_teams is not None:
          self.num_teams = num_teams
        if ranking is not None:
          self.ranking = ranking
        if sort_order_info is not None:
          self.sort_order_info = sort_order_info
        if status is not None:
          self.status = status

    @property
    def num_teams(self):
        """
        Gets the num_teams of this TeamEventStatusRank.
        Number of teams ranked.

        :return: The num_teams of this TeamEventStatusRank.
        :rtype: int
        """
        return self._num_teams

    @num_teams.setter
    def num_teams(self, num_teams):
        """
        Sets the num_teams of this TeamEventStatusRank.
        Number of teams ranked.

        :param num_teams: The num_teams of this TeamEventStatusRank.
        :type: int
        """

        self._num_teams = num_teams

    @property
    def ranking(self):
        """
        Gets the ranking of this TeamEventStatusRank.

        :return: The ranking of this TeamEventStatusRank.
        :rtype: TeamEventStatusRankRanking
        """
        return self._ranking

    @ranking.setter
    def ranking(self, ranking):
        """
        Sets the ranking of this TeamEventStatusRank.

        :param ranking: The ranking of this TeamEventStatusRank.
        :type: TeamEventStatusRankRanking
        """

        self._ranking = ranking

    @property
    def sort_order_info(self):
        """
        Gets the sort_order_info of this TeamEventStatusRank.
        Ordered list of names corresponding to the elements of the `sort_orders` array.

        :return: The sort_order_info of this TeamEventStatusRank.
        :rtype: list[TeamEventStatusRankSortOrderInfo]
        """
        return self._sort_order_info

    @sort_order_info.setter
    def sort_order_info(self, sort_order_info):
        """
        Sets the sort_order_info of this TeamEventStatusRank.
        Ordered list of names corresponding to the elements of the `sort_orders` array.

        :param sort_order_info: The sort_order_info of this TeamEventStatusRank.
        :type: list[TeamEventStatusRankSortOrderInfo]
        """

        self._sort_order_info = sort_order_info

    @property
    def status(self):
        """
        Gets the status of this TeamEventStatusRank.

        :return: The status of this TeamEventStatusRank.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this TeamEventStatusRank.

        :param status: The status of this TeamEventStatusRank.
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
        if not isinstance(other, TeamEventStatusRank):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
