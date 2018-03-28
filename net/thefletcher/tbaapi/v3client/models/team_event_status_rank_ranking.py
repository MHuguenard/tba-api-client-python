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


class TeamEventStatusRankRanking(object):
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
        'dq': 'int',
        'matches_played': 'int',
        'qual_average': 'float',
        'rank': 'int',
        'record': 'WLTRecord',
        'sort_orders': 'list[float]',
        'team_key': 'str'
    }

    attribute_map = {
        'dq': 'dq',
        'matches_played': 'matches_played',
        'qual_average': 'qual_average',
        'rank': 'rank',
        'record': 'record',
        'sort_orders': 'sort_orders',
        'team_key': 'team_key'
    }

    def __init__(self, dq=None, matches_played=None, qual_average=None, rank=None, record=None, sort_orders=None, team_key=None):
        """
        TeamEventStatusRankRanking - a model defined in Swagger
        """

        self._dq = None
        self._matches_played = None
        self._qual_average = None
        self._rank = None
        self._record = None
        self._sort_orders = None
        self._team_key = None

        if dq is not None:
          self.dq = dq
        if matches_played is not None:
          self.matches_played = matches_played
        if qual_average is not None:
          self.qual_average = qual_average
        if rank is not None:
          self.rank = rank
        if record is not None:
          self.record = record
        if sort_orders is not None:
          self.sort_orders = sort_orders
        if team_key is not None:
          self.team_key = team_key

    @property
    def dq(self):
        """
        Gets the dq of this TeamEventStatusRankRanking.
        Number of matches the team was disqualified for.

        :return: The dq of this TeamEventStatusRankRanking.
        :rtype: int
        """
        return self._dq

    @dq.setter
    def dq(self, dq):
        """
        Sets the dq of this TeamEventStatusRankRanking.
        Number of matches the team was disqualified for.

        :param dq: The dq of this TeamEventStatusRankRanking.
        :type: int
        """

        self._dq = dq

    @property
    def matches_played(self):
        """
        Gets the matches_played of this TeamEventStatusRankRanking.
        Number of matches played.

        :return: The matches_played of this TeamEventStatusRankRanking.
        :rtype: int
        """
        return self._matches_played

    @matches_played.setter
    def matches_played(self, matches_played):
        """
        Sets the matches_played of this TeamEventStatusRankRanking.
        Number of matches played.

        :param matches_played: The matches_played of this TeamEventStatusRankRanking.
        :type: int
        """

        self._matches_played = matches_played

    @property
    def qual_average(self):
        """
        Gets the qual_average of this TeamEventStatusRankRanking.
        For some years, average qualification score. Can be null.

        :return: The qual_average of this TeamEventStatusRankRanking.
        :rtype: float
        """
        return self._qual_average

    @qual_average.setter
    def qual_average(self, qual_average):
        """
        Sets the qual_average of this TeamEventStatusRankRanking.
        For some years, average qualification score. Can be null.

        :param qual_average: The qual_average of this TeamEventStatusRankRanking.
        :type: float
        """

        self._qual_average = qual_average

    @property
    def rank(self):
        """
        Gets the rank of this TeamEventStatusRankRanking.
        Relative rank of this team.

        :return: The rank of this TeamEventStatusRankRanking.
        :rtype: int
        """
        return self._rank

    @rank.setter
    def rank(self, rank):
        """
        Sets the rank of this TeamEventStatusRankRanking.
        Relative rank of this team.

        :param rank: The rank of this TeamEventStatusRankRanking.
        :type: int
        """

        self._rank = rank

    @property
    def record(self):
        """
        Gets the record of this TeamEventStatusRankRanking.

        :return: The record of this TeamEventStatusRankRanking.
        :rtype: WLTRecord
        """
        return self._record

    @record.setter
    def record(self, record):
        """
        Sets the record of this TeamEventStatusRankRanking.

        :param record: The record of this TeamEventStatusRankRanking.
        :type: WLTRecord
        """

        self._record = record

    @property
    def sort_orders(self):
        """
        Gets the sort_orders of this TeamEventStatusRankRanking.
        Ordered list of values used to determine the rank. See the `sort_order_info` property for the name of each value.

        :return: The sort_orders of this TeamEventStatusRankRanking.
        :rtype: list[float]
        """
        return self._sort_orders

    @sort_orders.setter
    def sort_orders(self, sort_orders):
        """
        Sets the sort_orders of this TeamEventStatusRankRanking.
        Ordered list of values used to determine the rank. See the `sort_order_info` property for the name of each value.

        :param sort_orders: The sort_orders of this TeamEventStatusRankRanking.
        :type: list[float]
        """

        self._sort_orders = sort_orders

    @property
    def team_key(self):
        """
        Gets the team_key of this TeamEventStatusRankRanking.
        TBA team key for this rank.

        :return: The team_key of this TeamEventStatusRankRanking.
        :rtype: str
        """
        return self._team_key

    @team_key.setter
    def team_key(self, team_key):
        """
        Sets the team_key of this TeamEventStatusRankRanking.
        TBA team key for this rank.

        :param team_key: The team_key of this TeamEventStatusRankRanking.
        :type: str
        """

        self._team_key = team_key

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
        if not isinstance(other, TeamEventStatusRankRanking):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
