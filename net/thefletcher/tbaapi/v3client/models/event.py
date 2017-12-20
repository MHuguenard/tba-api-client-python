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


class Event(object):
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
        'year': 'int',
        'short_name': 'str',
        'event_type_string': 'str',
        'week': 'int',
        'address': 'str',
        'postal_code': 'str',
        'gmaps_place_id': 'str',
        'gmaps_url': 'str',
        'lat': 'float',
        'lng': 'float',
        'location_name': 'str',
        'timezone': 'str',
        'website': 'str',
        'first_event_id': 'int',
        'first_event_code': 'str',
        'webcasts': 'list[Webcast]',
        'division_keys': 'list[str]',
        'parent_event_key': 'str',
        'playoff_type': 'int',
        'playoff_type_string': 'str'
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
        'year': 'year',
        'short_name': 'short_name',
        'event_type_string': 'event_type_string',
        'week': 'week',
        'address': 'address',
        'postal_code': 'postal_code',
        'gmaps_place_id': 'gmaps_place_id',
        'gmaps_url': 'gmaps_url',
        'lat': 'lat',
        'lng': 'lng',
        'location_name': 'location_name',
        'timezone': 'timezone',
        'website': 'website',
        'first_event_id': 'first_event_id',
        'first_event_code': 'first_event_code',
        'webcasts': 'webcasts',
        'division_keys': 'division_keys',
        'parent_event_key': 'parent_event_key',
        'playoff_type': 'playoff_type',
        'playoff_type_string': 'playoff_type_string'
    }

    def __init__(self, key=None, name=None, event_code=None, event_type=None, district=None, city=None, state_prov=None, country=None, start_date=None, end_date=None, year=None, short_name=None, event_type_string=None, week=None, address=None, postal_code=None, gmaps_place_id=None, gmaps_url=None, lat=None, lng=None, location_name=None, timezone=None, website=None, first_event_id=None, first_event_code=None, webcasts=None, division_keys=None, parent_event_key=None, playoff_type=None, playoff_type_string=None):
        """
        Event - a model defined in Swagger
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
        self._short_name = None
        self._event_type_string = None
        self._week = None
        self._address = None
        self._postal_code = None
        self._gmaps_place_id = None
        self._gmaps_url = None
        self._lat = None
        self._lng = None
        self._location_name = None
        self._timezone = None
        self._website = None
        self._first_event_id = None
        self._first_event_code = None
        self._webcasts = None
        self._division_keys = None
        self._parent_event_key = None
        self._playoff_type = None
        self._playoff_type_string = None

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
        if short_name is not None:
          self.short_name = short_name
        self.event_type_string = event_type_string
        if week is not None:
          self.week = week
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
        if timezone is not None:
          self.timezone = timezone
        if website is not None:
          self.website = website
        if first_event_id is not None:
          self.first_event_id = first_event_id
        if first_event_code is not None:
          self.first_event_code = first_event_code
        if webcasts is not None:
          self.webcasts = webcasts
        if division_keys is not None:
          self.division_keys = division_keys
        if parent_event_key is not None:
          self.parent_event_key = parent_event_key
        if playoff_type is not None:
          self.playoff_type = playoff_type
        if playoff_type_string is not None:
          self.playoff_type_string = playoff_type_string

    @property
    def key(self):
        """
        Gets the key of this Event.
        TBA event key with the format yyyy[EVENT_CODE], where yyyy is the year, and EVENT_CODE is the event code of the event.

        :return: The key of this Event.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this Event.
        TBA event key with the format yyyy[EVENT_CODE], where yyyy is the year, and EVENT_CODE is the event code of the event.

        :param key: The key of this Event.
        :type: str
        """
        if key is None:
            raise ValueError("Invalid value for `key`, must not be `None`")

        self._key = key

    @property
    def name(self):
        """
        Gets the name of this Event.
        Official name of event on record either provided by FIRST or organizers of offseason event.

        :return: The name of this Event.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Event.
        Official name of event on record either provided by FIRST or organizers of offseason event.

        :param name: The name of this Event.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def event_code(self):
        """
        Gets the event_code of this Event.
        Event short code, as provided by FIRST.

        :return: The event_code of this Event.
        :rtype: str
        """
        return self._event_code

    @event_code.setter
    def event_code(self, event_code):
        """
        Sets the event_code of this Event.
        Event short code, as provided by FIRST.

        :param event_code: The event_code of this Event.
        :type: str
        """
        if event_code is None:
            raise ValueError("Invalid value for `event_code`, must not be `None`")

        self._event_code = event_code

    @property
    def event_type(self):
        """
        Gets the event_type of this Event.
        Event Type, as defined here: https://github.com/the-blue-alliance/the-blue-alliance/blob/master/consts/event_type.py#L2

        :return: The event_type of this Event.
        :rtype: int
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """
        Sets the event_type of this Event.
        Event Type, as defined here: https://github.com/the-blue-alliance/the-blue-alliance/blob/master/consts/event_type.py#L2

        :param event_type: The event_type of this Event.
        :type: int
        """
        if event_type is None:
            raise ValueError("Invalid value for `event_type`, must not be `None`")

        self._event_type = event_type

    @property
    def district(self):
        """
        Gets the district of this Event.
        The district this event is in, may be null.

        :return: The district of this Event.
        :rtype: DistrictList
        """
        return self._district

    @district.setter
    def district(self, district):
        """
        Sets the district of this Event.
        The district this event is in, may be null.

        :param district: The district of this Event.
        :type: DistrictList
        """

        self._district = district

    @property
    def city(self):
        """
        Gets the city of this Event.
        City, town, village, etc. the event is located in.

        :return: The city of this Event.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """
        Sets the city of this Event.
        City, town, village, etc. the event is located in.

        :param city: The city of this Event.
        :type: str
        """

        self._city = city

    @property
    def state_prov(self):
        """
        Gets the state_prov of this Event.
        State or Province the event is located in.

        :return: The state_prov of this Event.
        :rtype: str
        """
        return self._state_prov

    @state_prov.setter
    def state_prov(self, state_prov):
        """
        Sets the state_prov of this Event.
        State or Province the event is located in.

        :param state_prov: The state_prov of this Event.
        :type: str
        """

        self._state_prov = state_prov

    @property
    def country(self):
        """
        Gets the country of this Event.
        Country the event is located in.

        :return: The country of this Event.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """
        Sets the country of this Event.
        Country the event is located in.

        :param country: The country of this Event.
        :type: str
        """

        self._country = country

    @property
    def start_date(self):
        """
        Gets the start_date of this Event.
        Event start date in `yyyy-mm-dd` format.

        :return: The start_date of this Event.
        :rtype: date
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """
        Sets the start_date of this Event.
        Event start date in `yyyy-mm-dd` format.

        :param start_date: The start_date of this Event.
        :type: date
        """
        if start_date is None:
            raise ValueError("Invalid value for `start_date`, must not be `None`")

        self._start_date = start_date

    @property
    def end_date(self):
        """
        Gets the end_date of this Event.
        Event end date in `yyyy-mm-dd` format.

        :return: The end_date of this Event.
        :rtype: date
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """
        Sets the end_date of this Event.
        Event end date in `yyyy-mm-dd` format.

        :param end_date: The end_date of this Event.
        :type: date
        """
        if end_date is None:
            raise ValueError("Invalid value for `end_date`, must not be `None`")

        self._end_date = end_date

    @property
    def year(self):
        """
        Gets the year of this Event.
        Year the event data is for.

        :return: The year of this Event.
        :rtype: int
        """
        return self._year

    @year.setter
    def year(self, year):
        """
        Sets the year of this Event.
        Year the event data is for.

        :param year: The year of this Event.
        :type: int
        """
        if year is None:
            raise ValueError("Invalid value for `year`, must not be `None`")

        self._year = year

    @property
    def short_name(self):
        """
        Gets the short_name of this Event.
        Same as `name` but doesn't include event specifiers, such as 'Regional' or 'District'. May be null.

        :return: The short_name of this Event.
        :rtype: str
        """
        return self._short_name

    @short_name.setter
    def short_name(self, short_name):
        """
        Sets the short_name of this Event.
        Same as `name` but doesn't include event specifiers, such as 'Regional' or 'District'. May be null.

        :param short_name: The short_name of this Event.
        :type: str
        """

        self._short_name = short_name

    @property
    def event_type_string(self):
        """
        Gets the event_type_string of this Event.
        Event Type, eg Regional, District, or Offseason.

        :return: The event_type_string of this Event.
        :rtype: str
        """
        return self._event_type_string

    @event_type_string.setter
    def event_type_string(self, event_type_string):
        """
        Sets the event_type_string of this Event.
        Event Type, eg Regional, District, or Offseason.

        :param event_type_string: The event_type_string of this Event.
        :type: str
        """
        if event_type_string is None:
            raise ValueError("Invalid value for `event_type_string`, must not be `None`")

        self._event_type_string = event_type_string

    @property
    def week(self):
        """
        Gets the week of this Event.
        Week of the competition season this event is in.

        :return: The week of this Event.
        :rtype: int
        """
        return self._week

    @week.setter
    def week(self, week):
        """
        Sets the week of this Event.
        Week of the competition season this event is in.

        :param week: The week of this Event.
        :type: int
        """

        self._week = week

    @property
    def address(self):
        """
        Gets the address of this Event.
        Address of the event's venue, if available.

        :return: The address of this Event.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """
        Sets the address of this Event.
        Address of the event's venue, if available.

        :param address: The address of this Event.
        :type: str
        """

        self._address = address

    @property
    def postal_code(self):
        """
        Gets the postal_code of this Event.
        Postal code from the event address.

        :return: The postal_code of this Event.
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """
        Sets the postal_code of this Event.
        Postal code from the event address.

        :param postal_code: The postal_code of this Event.
        :type: str
        """

        self._postal_code = postal_code

    @property
    def gmaps_place_id(self):
        """
        Gets the gmaps_place_id of this Event.
        Google Maps Place ID for the event address.

        :return: The gmaps_place_id of this Event.
        :rtype: str
        """
        return self._gmaps_place_id

    @gmaps_place_id.setter
    def gmaps_place_id(self, gmaps_place_id):
        """
        Sets the gmaps_place_id of this Event.
        Google Maps Place ID for the event address.

        :param gmaps_place_id: The gmaps_place_id of this Event.
        :type: str
        """

        self._gmaps_place_id = gmaps_place_id

    @property
    def gmaps_url(self):
        """
        Gets the gmaps_url of this Event.
        Link to address location on Google Maps.

        :return: The gmaps_url of this Event.
        :rtype: str
        """
        return self._gmaps_url

    @gmaps_url.setter
    def gmaps_url(self, gmaps_url):
        """
        Sets the gmaps_url of this Event.
        Link to address location on Google Maps.

        :param gmaps_url: The gmaps_url of this Event.
        :type: str
        """

        self._gmaps_url = gmaps_url

    @property
    def lat(self):
        """
        Gets the lat of this Event.
        Latitude for the event address.

        :return: The lat of this Event.
        :rtype: float
        """
        return self._lat

    @lat.setter
    def lat(self, lat):
        """
        Sets the lat of this Event.
        Latitude for the event address.

        :param lat: The lat of this Event.
        :type: float
        """

        self._lat = lat

    @property
    def lng(self):
        """
        Gets the lng of this Event.
        Longitude for the event address.

        :return: The lng of this Event.
        :rtype: float
        """
        return self._lng

    @lng.setter
    def lng(self, lng):
        """
        Sets the lng of this Event.
        Longitude for the event address.

        :param lng: The lng of this Event.
        :type: float
        """

        self._lng = lng

    @property
    def location_name(self):
        """
        Gets the location_name of this Event.
        Name of the location at the address for the event, eg. Blue Alliance High School.

        :return: The location_name of this Event.
        :rtype: str
        """
        return self._location_name

    @location_name.setter
    def location_name(self, location_name):
        """
        Sets the location_name of this Event.
        Name of the location at the address for the event, eg. Blue Alliance High School.

        :param location_name: The location_name of this Event.
        :type: str
        """

        self._location_name = location_name

    @property
    def timezone(self):
        """
        Gets the timezone of this Event.
        Timezone name.

        :return: The timezone of this Event.
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """
        Sets the timezone of this Event.
        Timezone name.

        :param timezone: The timezone of this Event.
        :type: str
        """

        self._timezone = timezone

    @property
    def website(self):
        """
        Gets the website of this Event.
        The event's website, if any.

        :return: The website of this Event.
        :rtype: str
        """
        return self._website

    @website.setter
    def website(self, website):
        """
        Sets the website of this Event.
        The event's website, if any.

        :param website: The website of this Event.
        :type: str
        """

        self._website = website

    @property
    def first_event_id(self):
        """
        Gets the first_event_id of this Event.
        The FIRST internal Event ID, used to link to the event on the FRC webpage.

        :return: The first_event_id of this Event.
        :rtype: int
        """
        return self._first_event_id

    @first_event_id.setter
    def first_event_id(self, first_event_id):
        """
        Sets the first_event_id of this Event.
        The FIRST internal Event ID, used to link to the event on the FRC webpage.

        :param first_event_id: The first_event_id of this Event.
        :type: int
        """

        self._first_event_id = first_event_id

    @property
    def first_event_code(self):
        """
        Gets the first_event_code of this Event.
        Public facing event code used by FIRST (on frc-events.firstinspires.org, for example)

        :return: The first_event_code of this Event.
        :rtype: str
        """
        return self._first_event_code

    @first_event_code.setter
    def first_event_code(self, first_event_code):
        """
        Sets the first_event_code of this Event.
        Public facing event code used by FIRST (on frc-events.firstinspires.org, for example)

        :param first_event_code: The first_event_code of this Event.
        :type: str
        """

        self._first_event_code = first_event_code

    @property
    def webcasts(self):
        """
        Gets the webcasts of this Event.

        :return: The webcasts of this Event.
        :rtype: list[Webcast]
        """
        return self._webcasts

    @webcasts.setter
    def webcasts(self, webcasts):
        """
        Sets the webcasts of this Event.

        :param webcasts: The webcasts of this Event.
        :type: list[Webcast]
        """

        self._webcasts = webcasts

    @property
    def division_keys(self):
        """
        Gets the division_keys of this Event.
        An array of event keys for the divisions at this event.

        :return: The division_keys of this Event.
        :rtype: list[str]
        """
        return self._division_keys

    @division_keys.setter
    def division_keys(self, division_keys):
        """
        Sets the division_keys of this Event.
        An array of event keys for the divisions at this event.

        :param division_keys: The division_keys of this Event.
        :type: list[str]
        """

        self._division_keys = division_keys

    @property
    def parent_event_key(self):
        """
        Gets the parent_event_key of this Event.
        The TBA Event key that represents the event's parent. Used to link back to the event from a division event. It is also the inverse relation of `divison_keys`.

        :return: The parent_event_key of this Event.
        :rtype: str
        """
        return self._parent_event_key

    @parent_event_key.setter
    def parent_event_key(self, parent_event_key):
        """
        Sets the parent_event_key of this Event.
        The TBA Event key that represents the event's parent. Used to link back to the event from a division event. It is also the inverse relation of `divison_keys`.

        :param parent_event_key: The parent_event_key of this Event.
        :type: str
        """

        self._parent_event_key = parent_event_key

    @property
    def playoff_type(self):
        """
        Gets the playoff_type of this Event.
        Playoff Type, as defined here: https://github.com/the-blue-alliance/the-blue-alliance/blob/master/consts/playoff_type.py#L4, or null.

        :return: The playoff_type of this Event.
        :rtype: int
        """
        return self._playoff_type

    @playoff_type.setter
    def playoff_type(self, playoff_type):
        """
        Sets the playoff_type of this Event.
        Playoff Type, as defined here: https://github.com/the-blue-alliance/the-blue-alliance/blob/master/consts/playoff_type.py#L4, or null.

        :param playoff_type: The playoff_type of this Event.
        :type: int
        """

        self._playoff_type = playoff_type

    @property
    def playoff_type_string(self):
        """
        Gets the playoff_type_string of this Event.
        String representation of the `playoff_type`, or null.

        :return: The playoff_type_string of this Event.
        :rtype: str
        """
        return self._playoff_type_string

    @playoff_type_string.setter
    def playoff_type_string(self, playoff_type_string):
        """
        Sets the playoff_type_string of this Event.
        String representation of the `playoff_type`, or null.

        :param playoff_type_string: The playoff_type_string of this Event.
        :type: str
        """

        self._playoff_type_string = playoff_type_string

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
        if not isinstance(other, Event):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other