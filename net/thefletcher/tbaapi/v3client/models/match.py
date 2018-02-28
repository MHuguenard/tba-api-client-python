# coding: utf-8

"""
    The Blue Alliance API v3

    # Overview    Information and statistics about FIRST Robotics Competition teams and events.   # Authentication   All endpoints require an Auth Key to be passed in the header `X-TBA-Auth-Key`. If you do not have an auth key yet, you can obtain one from your [Account Page](/account).    A `User-Agent` header may need to be set to prevent a 403 Unauthorized error.

    OpenAPI spec version: 3.02.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Match(object):
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
        'comp_level': 'str',
        'set_number': 'int',
        'match_number': 'int',
        'alliances': 'MatchSimpleAlliances',
        'winning_alliance': 'str',
        'event_key': 'str',
        'time': 'int',
        'actual_time': 'int',
        'predicted_time': 'int',
        'post_result_time': 'int',
        'score_breakdown': 'object',
        'videos': 'list[MatchVideos]'
    }

    attribute_map = {
        'key': 'key',
        'comp_level': 'comp_level',
        'set_number': 'set_number',
        'match_number': 'match_number',
        'alliances': 'alliances',
        'winning_alliance': 'winning_alliance',
        'event_key': 'event_key',
        'time': 'time',
        'actual_time': 'actual_time',
        'predicted_time': 'predicted_time',
        'post_result_time': 'post_result_time',
        'score_breakdown': 'score_breakdown',
        'videos': 'videos'
    }

    def __init__(self, key=None, comp_level=None, set_number=None, match_number=None, alliances=None, winning_alliance=None, event_key=None, time=None, actual_time=None, predicted_time=None, post_result_time=None, score_breakdown=None, videos=None):
        """
        Match - a model defined in Swagger
        """

        self._key = None
        self._comp_level = None
        self._set_number = None
        self._match_number = None
        self._alliances = None
        self._winning_alliance = None
        self._event_key = None
        self._time = None
        self._actual_time = None
        self._predicted_time = None
        self._post_result_time = None
        self._score_breakdown = None
        self._videos = None

        self.key = key
        self.comp_level = comp_level
        self.set_number = set_number
        self.match_number = match_number
        if alliances is not None:
          self.alliances = alliances
        if winning_alliance is not None:
          self.winning_alliance = winning_alliance
        self.event_key = event_key
        if time is not None:
          self.time = time
        if actual_time is not None:
          self.actual_time = actual_time
        if predicted_time is not None:
          self.predicted_time = predicted_time
        if post_result_time is not None:
          self.post_result_time = post_result_time
        if score_breakdown is not None:
          self.score_breakdown = score_breakdown
        if videos is not None:
          self.videos = videos

    @property
    def key(self):
        """
        Gets the key of this Match.
        TBA match key with the format `yyyy[EVENT_CODE]_[COMP_LEVEL]m[MATCH_NUMBER]`, where `yyyy` is the year, and `EVENT_CODE` is the event code of the event, `COMP_LEVEL` is (qm, ef, qf, sf, f), and `MATCH_NUMBER` is the match number in the competition level. A set number may be appended to the competition level if more than one match in required per set.

        :return: The key of this Match.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this Match.
        TBA match key with the format `yyyy[EVENT_CODE]_[COMP_LEVEL]m[MATCH_NUMBER]`, where `yyyy` is the year, and `EVENT_CODE` is the event code of the event, `COMP_LEVEL` is (qm, ef, qf, sf, f), and `MATCH_NUMBER` is the match number in the competition level. A set number may be appended to the competition level if more than one match in required per set.

        :param key: The key of this Match.
        :type: str
        """
        if key is None:
            raise ValueError("Invalid value for `key`, must not be `None`")

        self._key = key

    @property
    def comp_level(self):
        """
        Gets the comp_level of this Match.
        The competition level the match was played at.

        :return: The comp_level of this Match.
        :rtype: str
        """
        return self._comp_level

    @comp_level.setter
    def comp_level(self, comp_level):
        """
        Sets the comp_level of this Match.
        The competition level the match was played at.

        :param comp_level: The comp_level of this Match.
        :type: str
        """
        if comp_level is None:
            raise ValueError("Invalid value for `comp_level`, must not be `None`")
        allowed_values = ["qm", "ef", "qf", "sf", "f"]
        if comp_level not in allowed_values:
            raise ValueError(
                "Invalid value for `comp_level` ({0}), must be one of {1}"
                .format(comp_level, allowed_values)
            )

        self._comp_level = comp_level

    @property
    def set_number(self):
        """
        Gets the set_number of this Match.
        The set number in a series of matches where more than one match is required in the match series.

        :return: The set_number of this Match.
        :rtype: int
        """
        return self._set_number

    @set_number.setter
    def set_number(self, set_number):
        """
        Sets the set_number of this Match.
        The set number in a series of matches where more than one match is required in the match series.

        :param set_number: The set_number of this Match.
        :type: int
        """
        if set_number is None:
            raise ValueError("Invalid value for `set_number`, must not be `None`")

        self._set_number = set_number

    @property
    def match_number(self):
        """
        Gets the match_number of this Match.
        The match number of the match in the competition level.

        :return: The match_number of this Match.
        :rtype: int
        """
        return self._match_number

    @match_number.setter
    def match_number(self, match_number):
        """
        Sets the match_number of this Match.
        The match number of the match in the competition level.

        :param match_number: The match_number of this Match.
        :type: int
        """
        if match_number is None:
            raise ValueError("Invalid value for `match_number`, must not be `None`")

        self._match_number = match_number

    @property
    def alliances(self):
        """
        Gets the alliances of this Match.

        :return: The alliances of this Match.
        :rtype: MatchSimpleAlliances
        """
        return self._alliances

    @alliances.setter
    def alliances(self, alliances):
        """
        Sets the alliances of this Match.

        :param alliances: The alliances of this Match.
        :type: MatchSimpleAlliances
        """

        self._alliances = alliances

    @property
    def winning_alliance(self):
        """
        Gets the winning_alliance of this Match.
        The color (red/blue) of the winning alliance. Will contain an empty string in the event of no winner, or a tie.

        :return: The winning_alliance of this Match.
        :rtype: str
        """
        return self._winning_alliance

    @winning_alliance.setter
    def winning_alliance(self, winning_alliance):
        """
        Sets the winning_alliance of this Match.
        The color (red/blue) of the winning alliance. Will contain an empty string in the event of no winner, or a tie.

        :param winning_alliance: The winning_alliance of this Match.
        :type: str
        """

        self._winning_alliance = winning_alliance

    @property
    def event_key(self):
        """
        Gets the event_key of this Match.
        Event key of the event the match was played at.

        :return: The event_key of this Match.
        :rtype: str
        """
        return self._event_key

    @event_key.setter
    def event_key(self, event_key):
        """
        Sets the event_key of this Match.
        Event key of the event the match was played at.

        :param event_key: The event_key of this Match.
        :type: str
        """
        if event_key is None:
            raise ValueError("Invalid value for `event_key`, must not be `None`")

        self._event_key = event_key

    @property
    def time(self):
        """
        Gets the time of this Match.
        UNIX timestamp (seconds since 1-Jan-1970 00:00:00) of the scheduled match time, as taken from the published schedule.

        :return: The time of this Match.
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        """
        Sets the time of this Match.
        UNIX timestamp (seconds since 1-Jan-1970 00:00:00) of the scheduled match time, as taken from the published schedule.

        :param time: The time of this Match.
        :type: int
        """

        self._time = time

    @property
    def actual_time(self):
        """
        Gets the actual_time of this Match.
        UNIX timestamp (seconds since 1-Jan-1970 00:00:00) of actual match start time.

        :return: The actual_time of this Match.
        :rtype: int
        """
        return self._actual_time

    @actual_time.setter
    def actual_time(self, actual_time):
        """
        Sets the actual_time of this Match.
        UNIX timestamp (seconds since 1-Jan-1970 00:00:00) of actual match start time.

        :param actual_time: The actual_time of this Match.
        :type: int
        """

        self._actual_time = actual_time

    @property
    def predicted_time(self):
        """
        Gets the predicted_time of this Match.
        UNIX timestamp (seconds since 1-Jan-1970 00:00:00) of the TBA predicted match start time.

        :return: The predicted_time of this Match.
        :rtype: int
        """
        return self._predicted_time

    @predicted_time.setter
    def predicted_time(self, predicted_time):
        """
        Sets the predicted_time of this Match.
        UNIX timestamp (seconds since 1-Jan-1970 00:00:00) of the TBA predicted match start time.

        :param predicted_time: The predicted_time of this Match.
        :type: int
        """

        self._predicted_time = predicted_time

    @property
    def post_result_time(self):
        """
        Gets the post_result_time of this Match.
        UNIX timestamp (seconds since 1-Jan-1970 00:00:00) when the match result was posted.

        :return: The post_result_time of this Match.
        :rtype: int
        """
        return self._post_result_time

    @post_result_time.setter
    def post_result_time(self, post_result_time):
        """
        Sets the post_result_time of this Match.
        UNIX timestamp (seconds since 1-Jan-1970 00:00:00) when the match result was posted.

        :param post_result_time: The post_result_time of this Match.
        :type: int
        """

        self._post_result_time = post_result_time

    @property
    def score_breakdown(self):
        """
        Gets the score_breakdown of this Match.
        Score breakdown for auto, teleop, etc. points. Varies from year to year. May be null.

        :return: The score_breakdown of this Match.
        :rtype: object
        """
        return self._score_breakdown

    @score_breakdown.setter
    def score_breakdown(self, score_breakdown):
        """
        Sets the score_breakdown of this Match.
        Score breakdown for auto, teleop, etc. points. Varies from year to year. May be null.

        :param score_breakdown: The score_breakdown of this Match.
        :type: object
        """

        self._score_breakdown = score_breakdown

    @property
    def videos(self):
        """
        Gets the videos of this Match.
        Array of video objects associated with this match.

        :return: The videos of this Match.
        :rtype: list[MatchVideos]
        """
        return self._videos

    @videos.setter
    def videos(self, videos):
        """
        Sets the videos of this Match.
        Array of video objects associated with this match.

        :param videos: The videos of this Match.
        :type: list[MatchVideos]
        """

        self._videos = videos

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
        if not isinstance(other, Match):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
