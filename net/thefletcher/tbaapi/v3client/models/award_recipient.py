# coding: utf-8

"""
    The Blue Alliance API v3

    # Overview    Information and statistics about FIRST Robotics Competition teams and events.   # Authentication   All endpoints require an Auth Key to be passed in the header `X-TBA-Auth-Key`. If you do not have an auth key yet, you can obtain one from your [Account Page](/account).    A `User-Agent` header may need to be set to prevent a 403 Unauthorized error.

    OpenAPI spec version: 3.02.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class AwardRecipient(object):
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
        'team_key': 'str',
        'awardee': 'str'
    }

    attribute_map = {
        'team_key': 'team_key',
        'awardee': 'awardee'
    }

    def __init__(self, team_key=None, awardee=None):
        """
        AwardRecipient - a model defined in Swagger
        """

        self._team_key = None
        self._awardee = None

        if team_key is not None:
          self.team_key = team_key
        if awardee is not None:
          self.awardee = awardee

    @property
    def team_key(self):
        """
        Gets the team_key of this AwardRecipient.
        The TBA team key for the team that was given the award. May be null.

        :return: The team_key of this AwardRecipient.
        :rtype: str
        """
        return self._team_key

    @team_key.setter
    def team_key(self, team_key):
        """
        Sets the team_key of this AwardRecipient.
        The TBA team key for the team that was given the award. May be null.

        :param team_key: The team_key of this AwardRecipient.
        :type: str
        """

        self._team_key = team_key

    @property
    def awardee(self):
        """
        Gets the awardee of this AwardRecipient.
        The name of the individual given the award. May be null.

        :return: The awardee of this AwardRecipient.
        :rtype: str
        """
        return self._awardee

    @awardee.setter
    def awardee(self, awardee):
        """
        Sets the awardee of this AwardRecipient.
        The name of the individual given the award. May be null.

        :param awardee: The awardee of this AwardRecipient.
        :type: str
        """

        self._awardee = awardee

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
        if not isinstance(other, AwardRecipient):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
