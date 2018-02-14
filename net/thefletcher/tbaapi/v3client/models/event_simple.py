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


class EventSimple(object):
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
        'name': 'str',
        'event_code': 'str',
        'event_type': 'int',
        'district': 'DistrictList',
        'city': 'str',
        'state_prov': 'str',
        'country': 'str',
        'start_date': 'date',
        'end_date': 'date',
        'year': 'int'
    }

    attribute_map = {
        'key': 'key',
        'name': 'name',
        'event_code': 'event_code',
        'event_type': 'event_type',
        'district': 'district',
        'city': 'city',
        'state_prov': 'state_prov',
        'country': 'country',
        'start_date': 'start_date',
        'end_date': 'end_date',
        'year': 'year'
    }

    def __init__(self, key=None, name=None, event_code=None, event_type=None, district=None, city=None, state_prov=None, country=None, start_date=None, end_date=None, year=None):
        """
        EventSimple - a model defined in Swagger
        """

        self._key = None
        self._name = None
        self._event_code = None
        self._event_type = None
        self._district = None
        self._city = None
        self._state_prov = None
        self._country = None
        self._start_date = None
        self._end_date = None
        self._year = None

        self.key = key
        self.name = name
        self.event_code = event_code
        self.event_type = event_type
        if district is not None:
          self.district = district
        if city is not None:
          self.city = city
        if state_prov is not None:
          self.state_prov = state_prov
        if country is not None:
          self.country = country
        self.start_date = start_date
        self.end_date = end_date
        self.year = year

    @property
    def key(self):
        """
        Gets the key of this EventSimple.
        TBA event key with the format yyyy[EVENT_CODE], where yyyy is the year, and EVENT_CODE is the event code of the event.

        :return: The key of this EventSimple.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this EventSimple.
        TBA event key with the format yyyy[EVENT_CODE], where yyyy is the year, and EVENT_CODE is the event code of the event.

        :param key: The key of this EventSimple.
        :type: str
        """
        if key is None:
            raise ValueError("Invalid value for `key`, must not be `None`")

        self._key = key

    @property
    def name(self):
        """
        Gets the name of this EventSimple.
        Official name of event on record either provided by FIRST or organizers of offseason event.

        :return: The name of this EventSimple.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this EventSimple.
        Official name of event on record either provided by FIRST or organizers of offseason event.

        :param name: The name of this EventSimple.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def event_code(self):
        """
        Gets the event_code of this EventSimple.
        Event short code, as provided by FIRST.

        :return: The event_code of this EventSimple.
        :rtype: str
        """
        return self._event_code

    @event_code.setter
    def event_code(self, event_code):
        """
        Sets the event_code of this EventSimple.
        Event short code, as provided by FIRST.

        :param event_code: The event_code of this EventSimple.
        :type: str
        """
        if event_code is None:
            raise ValueError("Invalid value for `event_code`, must not be `None`")

        self._event_code = event_code

    @property
    def event_type(self):
        """
        Gets the event_type of this EventSimple.
        Event Type, as defined here: https://github.com/the-blue-alliance/the-blue-alliance/blob/master/consts/event_type.py#L2

        :return: The event_type of this EventSimple.
        :rtype: int
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """
        Sets the event_type of this EventSimple.
        Event Type, as defined here: https://github.com/the-blue-alliance/the-blue-alliance/blob/master/consts/event_type.py#L2

        :param event_type: The event_type of this EventSimple.
        :type: int
        """
        if event_type is None:
            raise ValueError("Invalid value for `event_type`, must not be `None`")

        self._event_type = event_type

    @property
    def district(self):
        """
        Gets the district of this EventSimple.
        The district this event is in, may be null.

        :return: The district of this EventSimple.
        :rtype: DistrictList
        """
        return self._district

    @district.setter
    def district(self, district):
        """
        Sets the district of this EventSimple.
        The district this event is in, may be null.

        :param district: The district of this EventSimple.
        :type: DistrictList
        """

        self._district = district

    @property
    def city(self):
        """
        Gets the city of this EventSimple.
        City, town, village, etc. the event is located in.

        :return: The city of this EventSimple.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """
        Sets the city of this EventSimple.
        City, town, village, etc. the event is located in.

        :param city: The city of this EventSimple.
        :type: str
        """

        self._city = city

    @property
    def state_prov(self):
        """
        Gets the state_prov of this EventSimple.
        State or Province the event is located in.

        :return: The state_prov of this EventSimple.
        :rtype: str
        """
        return self._state_prov

    @state_prov.setter
    def state_prov(self, state_prov):
        """
        Sets the state_prov of this EventSimple.
        State or Province the event is located in.

        :param state_prov: The state_prov of this EventSimple.
        :type: str
        """

        self._state_prov = state_prov

    @property
    def country(self):
        """
        Gets the country of this EventSimple.
        Country the event is located in.

        :return: The country of this EventSimple.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """
        Sets the country of this EventSimple.
        Country the event is located in.

        :param country: The country of this EventSimple.
        :type: str
        """

        self._country = country

    @property
    def start_date(self):
        """
        Gets the start_date of this EventSimple.
        Event start date in `yyyy-mm-dd` format.

        :return: The start_date of this EventSimple.
        :rtype: date
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """
        Sets the start_date of this EventSimple.
        Event start date in `yyyy-mm-dd` format.

        :param start_date: The start_date of this EventSimple.
        :type: date
        """
        if start_date is None:
            raise ValueError("Invalid value for `start_date`, must not be `None`")

        self._start_date = start_date

    @property
    def end_date(self):
        """
        Gets the end_date of this EventSimple.
        Event end date in `yyyy-mm-dd` format.

        :return: The end_date of this EventSimple.
        :rtype: date
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """
        Sets the end_date of this EventSimple.
        Event end date in `yyyy-mm-dd` format.

        :param end_date: The end_date of this EventSimple.
        :type: date
        """
        if end_date is None:
            raise ValueError("Invalid value for `end_date`, must not be `None`")

        self._end_date = end_date

    @property
    def year(self):
        """
        Gets the year of this EventSimple.
        Year the event data is for.

        :return: The year of this EventSimple.
        :rtype: int
        """
        return self._year

    @year.setter
    def year(self, year):
        """
        Sets the year of this EventSimple.
        Year the event data is for.

        :param year: The year of this EventSimple.
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
        if not isinstance(other, EventSimple):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
