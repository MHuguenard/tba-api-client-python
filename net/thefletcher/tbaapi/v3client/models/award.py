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


class Award(object):
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
        'award_type': 'int',
        'event_key': 'str',
        'recipient_list': 'list[AwardRecipient]',
        'year': 'int'
    }

    attribute_map = {
        'name': 'name',
        'award_type': 'award_type',
        'event_key': 'event_key',
        'recipient_list': 'recipient_list',
        'year': 'year'
    }

    def __init__(self, name=None, award_type=None, event_key=None, recipient_list=None, year=None):
        """
        Award - a model defined in Swagger
        """

        self._name = None
        self._award_type = None
        self._event_key = None
        self._recipient_list = None
        self._year = None

        self.name = name
        self.award_type = award_type
        self.event_key = event_key
        self.recipient_list = recipient_list
        self.year = year

    @property
    def name(self):
        """
        Gets the name of this Award.
        The name of the award as provided by FIRST. May vary for the same award type.

        :return: The name of this Award.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Award.
        The name of the award as provided by FIRST. May vary for the same award type.

        :param name: The name of this Award.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def award_type(self):
        """
        Gets the award_type of this Award.
        Type of award given. See https://github.com/the-blue-alliance/the-blue-alliance/blob/master/consts/award_type.py#L6

        :return: The award_type of this Award.
        :rtype: int
        """
        return self._award_type

    @award_type.setter
    def award_type(self, award_type):
        """
        Sets the award_type of this Award.
        Type of award given. See https://github.com/the-blue-alliance/the-blue-alliance/blob/master/consts/award_type.py#L6

        :param award_type: The award_type of this Award.
        :type: int
        """
        if award_type is None:
            raise ValueError("Invalid value for `award_type`, must not be `None`")

        self._award_type = award_type

    @property
    def event_key(self):
        """
        Gets the event_key of this Award.
        The event_key of the event the award was won at.

        :return: The event_key of this Award.
        :rtype: str
        """
        return self._event_key

    @event_key.setter
    def event_key(self, event_key):
        """
        Sets the event_key of this Award.
        The event_key of the event the award was won at.

        :param event_key: The event_key of this Award.
        :type: str
        """
        if event_key is None:
            raise ValueError("Invalid value for `event_key`, must not be `None`")

        self._event_key = event_key

    @property
    def recipient_list(self):
        """
        Gets the recipient_list of this Award.
        A list of recipients of the award at the event. Either team_key and/or awardee for individual awards.

        :return: The recipient_list of this Award.
        :rtype: list[AwardRecipient]
        """
        return self._recipient_list

    @recipient_list.setter
    def recipient_list(self, recipient_list):
        """
        Sets the recipient_list of this Award.
        A list of recipients of the award at the event. Either team_key and/or awardee for individual awards.

        :param recipient_list: The recipient_list of this Award.
        :type: list[AwardRecipient]
        """
        if recipient_list is None:
            raise ValueError("Invalid value for `recipient_list`, must not be `None`")

        self._recipient_list = recipient_list

    @property
    def year(self):
        """
        Gets the year of this Award.
        The year this award was won.

        :return: The year of this Award.
        :rtype: int
        """
        return self._year

    @year.setter
    def year(self, year):
        """
        Sets the year of this Award.
        The year this award was won.

        :param year: The year of this Award.
        :type: int
        """
        if year is None:
            raise ValueError("Invalid value for `year`, must not be `None`")

        self._year = year

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
        if not isinstance(other, Award):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
