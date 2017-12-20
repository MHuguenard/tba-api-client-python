# coding: utf-8

"""
    The Blue Alliance API v3

    # Overview    Information and statistics about FIRST Robotics Competition teams and events. If you are looking for the old version (v2) of the API, documentation can be found [here](/apidocs/v2).   # Authentication   All endpoints require an Auth Key to be passed in the header `X-TBA-Auth-Key`. If you do not have an auth key yet, you can obtain one from your [Account Page](/account).    A `User-Agent` header may need to be set to prevent a 403 Unauthorized error.

    OpenAPI spec version: 3.0.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class TeamSimple(object):
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
        'key': 'str',
        'team_number': 'int',
        'nickname': 'str',
        'name': 'str',
        'city': 'str',
        'state_prov': 'str',
        'country': 'str'
    }

    attribute_map = {
        'key': 'key',
        'team_number': 'team_number',
        'nickname': 'nickname',
        'name': 'name',
        'city': 'city',
        'state_prov': 'state_prov',
        'country': 'country'
    }

    def __init__(self, key=None, team_number=None, nickname=None, name=None, city=None, state_prov=None, country=None):
        """
        TeamSimple - a model defined in Swagger
        """

        self._key = None
        self._team_number = None
        self._nickname = None
        self._name = None
        self._city = None
        self._state_prov = None
        self._country = None

        self.key = key
        self.team_number = team_number
        if nickname is not None:
          self.nickname = nickname
        self.name = name
        if city is not None:
          self.city = city
        if state_prov is not None:
          self.state_prov = state_prov
        if country is not None:
          self.country = country

    @property
    def key(self):
        """
        Gets the key of this TeamSimple.
        TBA team key with the format `frcXXXX` with `XXXX` representing the team number.

        :return: The key of this TeamSimple.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this TeamSimple.
        TBA team key with the format `frcXXXX` with `XXXX` representing the team number.

        :param key: The key of this TeamSimple.
        :type: str
        """
        if key is None:
            raise ValueError("Invalid value for `key`, must not be `None`")

        self._key = key

    @property
    def team_number(self):
        """
        Gets the team_number of this TeamSimple.
        Official team number issued by FIRST.

        :return: The team_number of this TeamSimple.
        :rtype: int
        """
        return self._team_number

    @team_number.setter
    def team_number(self, team_number):
        """
        Sets the team_number of this TeamSimple.
        Official team number issued by FIRST.

        :param team_number: The team_number of this TeamSimple.
        :type: int
        """
        if team_number is None:
            raise ValueError("Invalid value for `team_number`, must not be `None`")

        self._team_number = team_number

    @property
    def nickname(self):
        """
        Gets the nickname of this TeamSimple.
        Team nickname provided by FIRST.

        :return: The nickname of this TeamSimple.
        :rtype: str
        """
        return self._nickname

    @nickname.setter
    def nickname(self, nickname):
        """
        Sets the nickname of this TeamSimple.
        Team nickname provided by FIRST.

        :param nickname: The nickname of this TeamSimple.
        :type: str
        """

        self._nickname = nickname

    @property
    def name(self):
        """
        Gets the name of this TeamSimple.
        Official long name registered with FIRST.

        :return: The name of this TeamSimple.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this TeamSimple.
        Official long name registered with FIRST.

        :param name: The name of this TeamSimple.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def city(self):
        """
        Gets the city of this TeamSimple.
        City of team derived from parsing the address registered with FIRST.

        :return: The city of this TeamSimple.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """
        Sets the city of this TeamSimple.
        City of team derived from parsing the address registered with FIRST.

        :param city: The city of this TeamSimple.
        :type: str
        """

        self._city = city

    @property
    def state_prov(self):
        """
        Gets the state_prov of this TeamSimple.
        State of team derived from parsing the address registered with FIRST.

        :return: The state_prov of this TeamSimple.
        :rtype: str
        """
        return self._state_prov

    @state_prov.setter
    def state_prov(self, state_prov):
        """
        Sets the state_prov of this TeamSimple.
        State of team derived from parsing the address registered with FIRST.

        :param state_prov: The state_prov of this TeamSimple.
        :type: str
        """

        self._state_prov = state_prov

    @property
    def country(self):
        """
        Gets the country of this TeamSimple.
        Country of team derived from parsing the address registered with FIRST.

        :return: The country of this TeamSimple.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """
        Sets the country of this TeamSimple.
        Country of team derived from parsing the address registered with FIRST.

        :param country: The country of this TeamSimple.
        :type: str
        """

        self._country = country

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
        if not isinstance(other, TeamSimple):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
