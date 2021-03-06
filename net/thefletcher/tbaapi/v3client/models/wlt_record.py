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


class WLTRecord(object):
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
        'losses': 'int',
        'wins': 'int',
        'ties': 'int'
    }

    attribute_map = {
        'losses': 'losses',
        'wins': 'wins',
        'ties': 'ties'
    }

    def __init__(self, losses=None, wins=None, ties=None):
        """
        WLTRecord - a model defined in Swagger
        """

        self._losses = None
        self._wins = None
        self._ties = None

        self.losses = losses
        self.wins = wins
        self.ties = ties

    @property
    def losses(self):
        """
        Gets the losses of this WLTRecord.
        Number of losses.

        :return: The losses of this WLTRecord.
        :rtype: int
        """
        return self._losses

    @losses.setter
    def losses(self, losses):
        """
        Sets the losses of this WLTRecord.
        Number of losses.

        :param losses: The losses of this WLTRecord.
        :type: int
        """
        if losses is None:
            raise ValueError("Invalid value for `losses`, must not be `None`")

        self._losses = losses

    @property
    def wins(self):
        """
        Gets the wins of this WLTRecord.
        Number of wins.

        :return: The wins of this WLTRecord.
        :rtype: int
        """
        return self._wins

    @wins.setter
    def wins(self, wins):
        """
        Sets the wins of this WLTRecord.
        Number of wins.

        :param wins: The wins of this WLTRecord.
        :type: int
        """
        if wins is None:
            raise ValueError("Invalid value for `wins`, must not be `None`")

        self._wins = wins

    @property
    def ties(self):
        """
        Gets the ties of this WLTRecord.
        Number of ties.

        :return: The ties of this WLTRecord.
        :rtype: int
        """
        return self._ties

    @ties.setter
    def ties(self, ties):
        """
        Sets the ties of this WLTRecord.
        Number of ties.

        :param ties: The ties of this WLTRecord.
        :type: int
        """
        if ties is None:
            raise ValueError("Invalid value for `ties`, must not be `None`")

        self._ties = ties

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
        if not isinstance(other, WLTRecord):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
