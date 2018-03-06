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


class Team(object):
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
        'country': 'str',
        'address': 'str',
        'postal_code': 'str',
        'gmaps_place_id': 'str',
        'gmaps_url': 'str',
        'lat': 'float',
        'lng': 'float',
        'location_name': 'str',
        'website': 'str',
        'rookie_year': 'int',
        'motto': 'str',
        'home_championship': 'object'
    }

    attribute_map = {
        'key': 'key',
        'team_number': 'team_number',
        'nickname': 'nickname',
        'name': 'name',
        'city': 'city',
        'state_prov': 'state_prov',
        'country': 'country',
        'address': 'address',
        'postal_code': 'postal_code',
        'gmaps_place_id': 'gmaps_place_id',
        'gmaps_url': 'gmaps_url',
        'lat': 'lat',
        'lng': 'lng',
        'location_name': 'location_name',
        'website': 'website',
        'rookie_year': 'rookie_year',
        'motto': 'motto',
        'home_championship': 'home_championship'
    }

    def __init__(self, key=None, team_number=None, nickname=None, name=None, city=None, state_prov=None, country=None, address=None, postal_code=None, gmaps_place_id=None, gmaps_url=None, lat=None, lng=None, location_name=None, website=None, rookie_year=None, motto=None, home_championship=None):
        """
        Team - a model defined in Swagger
        """

        self._key = None
        self._team_number = None
        self._nickname = None
        self._name = None
        self._city = None
        self._state_prov = None
        self._country = None
        self._address = None
        self._postal_code = None
        self._gmaps_place_id = None
        self._gmaps_url = None
        self._lat = None
        self._lng = None
        self._location_name = None
        self._website = None
        self._rookie_year = None
        self._motto = None
        self._home_championship = None

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
        if address is not None:
          self.address = address
        if postal_code is not None:
          self.postal_code = postal_code
        if gmaps_place_id is not None:
          self.gmaps_place_id = gmaps_place_id
        if gmaps_url is not None:
          self.gmaps_url = gmaps_url
        if lat is not None:
          self.lat = lat
        if lng is not None:
          self.lng = lng
        if location_name is not None:
          self.location_name = location_name
        if website is not None:
          self.website = website
        self.rookie_year = rookie_year
        if motto is not None:
          self.motto = motto
        if home_championship is not None:
          self.home_championship = home_championship

    @property
    def key(self):
        """
        Gets the key of this Team.
        TBA team key with the format `frcXXXX` with `XXXX` representing the team number.

        :return: The key of this Team.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this Team.
        TBA team key with the format `frcXXXX` with `XXXX` representing the team number.

        :param key: The key of this Team.
        :type: str
        """
        if key is None:
            raise ValueError("Invalid value for `key`, must not be `None`")

        self._key = key

    @property
    def team_number(self):
        """
        Gets the team_number of this Team.
        Official team number issued by FIRST.

        :return: The team_number of this Team.
        :rtype: int
        """
        return self._team_number

    @team_number.setter
    def team_number(self, team_number):
        """
        Sets the team_number of this Team.
        Official team number issued by FIRST.

        :param team_number: The team_number of this Team.
        :type: int
        """
        if team_number is None:
            raise ValueError("Invalid value for `team_number`, must not be `None`")

        self._team_number = team_number

    @property
    def nickname(self):
        """
        Gets the nickname of this Team.
        Team nickname provided by FIRST.

        :return: The nickname of this Team.
        :rtype: str
        """
        return self._nickname

    @nickname.setter
    def nickname(self, nickname):
        """
        Sets the nickname of this Team.
        Team nickname provided by FIRST.

        :param nickname: The nickname of this Team.
        :type: str
        """

        self._nickname = nickname

    @property
    def name(self):
        """
        Gets the name of this Team.
        Official long name registered with FIRST.

        :return: The name of this Team.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Team.
        Official long name registered with FIRST.

        :param name: The name of this Team.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def city(self):
        """
        Gets the city of this Team.
        City of team derived from parsing the address registered with FIRST.

        :return: The city of this Team.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """
        Sets the city of this Team.
        City of team derived from parsing the address registered with FIRST.

        :param city: The city of this Team.
        :type: str
        """

        self._city = city

    @property
    def state_prov(self):
        """
        Gets the state_prov of this Team.
        State of team derived from parsing the address registered with FIRST.

        :return: The state_prov of this Team.
        :rtype: str
        """
        return self._state_prov

    @state_prov.setter
    def state_prov(self, state_prov):
        """
        Sets the state_prov of this Team.
        State of team derived from parsing the address registered with FIRST.

        :param state_prov: The state_prov of this Team.
        :type: str
        """

        self._state_prov = state_prov

    @property
    def country(self):
        """
        Gets the country of this Team.
        Country of team derived from parsing the address registered with FIRST.

        :return: The country of this Team.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """
        Sets the country of this Team.
        Country of team derived from parsing the address registered with FIRST.

        :param country: The country of this Team.
        :type: str
        """

        self._country = country

    @property
    def address(self):
        """
        Gets the address of this Team.
        Will be NULL, for future development.

        :return: The address of this Team.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """
        Sets the address of this Team.
        Will be NULL, for future development.

        :param address: The address of this Team.
        :type: str
        """

        self._address = address

    @property
    def postal_code(self):
        """
        Gets the postal_code of this Team.
        Postal code from the team address.

        :return: The postal_code of this Team.
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """
        Sets the postal_code of this Team.
        Postal code from the team address.

        :param postal_code: The postal_code of this Team.
        :type: str
        """

        self._postal_code = postal_code

    @property
    def gmaps_place_id(self):
        """
        Gets the gmaps_place_id of this Team.
        Will be NULL, for future development.

        :return: The gmaps_place_id of this Team.
        :rtype: str
        """
        return self._gmaps_place_id

    @gmaps_place_id.setter
    def gmaps_place_id(self, gmaps_place_id):
        """
        Sets the gmaps_place_id of this Team.
        Will be NULL, for future development.

        :param gmaps_place_id: The gmaps_place_id of this Team.
        :type: str
        """

        self._gmaps_place_id = gmaps_place_id

    @property
    def gmaps_url(self):
        """
        Gets the gmaps_url of this Team.
        Will be NULL, for future development.

        :return: The gmaps_url of this Team.
        :rtype: str
        """
        return self._gmaps_url

    @gmaps_url.setter
    def gmaps_url(self, gmaps_url):
        """
        Sets the gmaps_url of this Team.
        Will be NULL, for future development.

        :param gmaps_url: The gmaps_url of this Team.
        :type: str
        """

        self._gmaps_url = gmaps_url

    @property
    def lat(self):
        """
        Gets the lat of this Team.
        Will be NULL, for future development.

        :return: The lat of this Team.
        :rtype: float
        """
        return self._lat

    @lat.setter
    def lat(self, lat):
        """
        Sets the lat of this Team.
        Will be NULL, for future development.

        :param lat: The lat of this Team.
        :type: float
        """

        self._lat = lat

    @property
    def lng(self):
        """
        Gets the lng of this Team.
        Will be NULL, for future development.

        :return: The lng of this Team.
        :rtype: float
        """
        return self._lng

    @lng.setter
    def lng(self, lng):
        """
        Sets the lng of this Team.
        Will be NULL, for future development.

        :param lng: The lng of this Team.
        :type: float
        """

        self._lng = lng

    @property
    def location_name(self):
        """
        Gets the location_name of this Team.
        Will be NULL, for future development.

        :return: The location_name of this Team.
        :rtype: str
        """
        return self._location_name

    @location_name.setter
    def location_name(self, location_name):
        """
        Sets the location_name of this Team.
        Will be NULL, for future development.

        :param location_name: The location_name of this Team.
        :type: str
        """

        self._location_name = location_name

    @property
    def website(self):
        """
        Gets the website of this Team.
        Official website associated with the team.

        :return: The website of this Team.
        :rtype: str
        """
        return self._website

    @website.setter
    def website(self, website):
        """
        Sets the website of this Team.
        Official website associated with the team.

        :param website: The website of this Team.
        :type: str
        """

        self._website = website

    @property
    def rookie_year(self):
        """
        Gets the rookie_year of this Team.
        First year the team officially competed.

        :return: The rookie_year of this Team.
        :rtype: int
        """
        return self._rookie_year

    @rookie_year.setter
    def rookie_year(self, rookie_year):
        """
        Sets the rookie_year of this Team.
        First year the team officially competed.

        :param rookie_year: The rookie_year of this Team.
        :type: int
        """
        if rookie_year is None:
            raise ValueError("Invalid value for `rookie_year`, must not be `None`")

        self._rookie_year = rookie_year

    @property
    def motto(self):
        """
        Gets the motto of this Team.
        Team's motto as provided by FIRST.

        :return: The motto of this Team.
        :rtype: str
        """
        return self._motto

    @motto.setter
    def motto(self, motto):
        """
        Sets the motto of this Team.
        Team's motto as provided by FIRST.

        :param motto: The motto of this Team.
        :type: str
        """

        self._motto = motto

    @property
    def home_championship(self):
        """
        Gets the home_championship of this Team.
        Location of the team's home championship each year as a key-value pair. The year (as a string) is the key, and the city is the value.

        :return: The home_championship of this Team.
        :rtype: object
        """
        return self._home_championship

    @home_championship.setter
    def home_championship(self, home_championship):
        """
        Sets the home_championship of this Team.
        Location of the team's home championship each year as a key-value pair. The year (as a string) is the key, and the city is the value.

        :param home_championship: The home_championship of this Team.
        :type: object
        """

        self._home_championship = home_championship

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
        if not isinstance(other, Team):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
