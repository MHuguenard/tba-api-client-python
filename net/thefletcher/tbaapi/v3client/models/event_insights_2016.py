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


class EventInsights2016(object):
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
        'low_bar': 'list[float]',
        'a_cheval_de_frise': 'list[float]',
        'a_portcullis': 'list[float]',
        'b_ramparts': 'list[float]',
        'b_moat': 'list[float]',
        'c_sally_port': 'list[float]',
        'c_drawbridge': 'list[float]',
        'd_rough_terrain': 'list[float]',
        'd_rock_wall': 'list[float]',
        'average_high_goals': 'float',
        'average_low_goals': 'float',
        'breaches': 'list[float]',
        'scales': 'list[float]',
        'challenges': 'list[float]',
        'captures': 'list[float]',
        'average_win_score': 'float',
        'average_win_margin': 'float',
        'average_score': 'float',
        'average_auto_score': 'float',
        'average_crossing_score': 'float',
        'average_boulder_score': 'float',
        'average_tower_score': 'float',
        'average_foul_score': 'float',
        'high_score': 'list[str]'
    }

    attribute_map = {
        'low_bar': 'LowBar',
        'a_cheval_de_frise': 'A_ChevalDeFrise',
        'a_portcullis': 'A_Portcullis',
        'b_ramparts': 'B_Ramparts',
        'b_moat': 'B_Moat',
        'c_sally_port': 'C_SallyPort',
        'c_drawbridge': 'C_Drawbridge',
        'd_rough_terrain': 'D_RoughTerrain',
        'd_rock_wall': 'D_RockWall',
        'average_high_goals': 'average_high_goals',
        'average_low_goals': 'average_low_goals',
        'breaches': 'breaches',
        'scales': 'scales',
        'challenges': 'challenges',
        'captures': 'captures',
        'average_win_score': 'average_win_score',
        'average_win_margin': 'average_win_margin',
        'average_score': 'average_score',
        'average_auto_score': 'average_auto_score',
        'average_crossing_score': 'average_crossing_score',
        'average_boulder_score': 'average_boulder_score',
        'average_tower_score': 'average_tower_score',
        'average_foul_score': 'average_foul_score',
        'high_score': 'high_score'
    }

    def __init__(self, low_bar=None, a_cheval_de_frise=None, a_portcullis=None, b_ramparts=None, b_moat=None, c_sally_port=None, c_drawbridge=None, d_rough_terrain=None, d_rock_wall=None, average_high_goals=None, average_low_goals=None, breaches=None, scales=None, challenges=None, captures=None, average_win_score=None, average_win_margin=None, average_score=None, average_auto_score=None, average_crossing_score=None, average_boulder_score=None, average_tower_score=None, average_foul_score=None, high_score=None):
        """
        EventInsights2016 - a model defined in Swagger
        """

        self._low_bar = None
        self._a_cheval_de_frise = None
        self._a_portcullis = None
        self._b_ramparts = None
        self._b_moat = None
        self._c_sally_port = None
        self._c_drawbridge = None
        self._d_rough_terrain = None
        self._d_rock_wall = None
        self._average_high_goals = None
        self._average_low_goals = None
        self._breaches = None
        self._scales = None
        self._challenges = None
        self._captures = None
        self._average_win_score = None
        self._average_win_margin = None
        self._average_score = None
        self._average_auto_score = None
        self._average_crossing_score = None
        self._average_boulder_score = None
        self._average_tower_score = None
        self._average_foul_score = None
        self._high_score = None

        self.low_bar = low_bar
        self.a_cheval_de_frise = a_cheval_de_frise
        self.a_portcullis = a_portcullis
        self.b_ramparts = b_ramparts
        self.b_moat = b_moat
        self.c_sally_port = c_sally_port
        self.c_drawbridge = c_drawbridge
        self.d_rough_terrain = d_rough_terrain
        self.d_rock_wall = d_rock_wall
        self.average_high_goals = average_high_goals
        self.average_low_goals = average_low_goals
        self.breaches = breaches
        self.scales = scales
        self.challenges = challenges
        self.captures = captures
        self.average_win_score = average_win_score
        self.average_win_margin = average_win_margin
        self.average_score = average_score
        self.average_auto_score = average_auto_score
        self.average_crossing_score = average_crossing_score
        self.average_boulder_score = average_boulder_score
        self.average_tower_score = average_tower_score
        self.average_foul_score = average_foul_score
        self.high_score = high_score

    @property
    def low_bar(self):
        """
        Gets the low_bar of this EventInsights2016.
        For the Low Bar - An array with three values, number of times damaged, number of opportunities to damage, and percentage.

        :return: The low_bar of this EventInsights2016.
        :rtype: list[float]
        """
        return self._low_bar

    @low_bar.setter
    def low_bar(self, low_bar):
        """
        Sets the low_bar of this EventInsights2016.
        For the Low Bar - An array with three values, number of times damaged, number of opportunities to damage, and percentage.

        :param low_bar: The low_bar of this EventInsights2016.
        :type: list[float]
        """
        if low_bar is None:
            raise ValueError("Invalid value for `low_bar`, must not be `None`")

        self._low_bar = low_bar

    @property
    def a_cheval_de_frise(self):
        """
        Gets the a_cheval_de_frise of this EventInsights2016.
        For the Cheval De Frise - An array with three values, number of times damaged, number of opportunities to damage, and percentage.

        :return: The a_cheval_de_frise of this EventInsights2016.
        :rtype: list[float]
        """
        return self._a_cheval_de_frise

    @a_cheval_de_frise.setter
    def a_cheval_de_frise(self, a_cheval_de_frise):
        """
        Sets the a_cheval_de_frise of this EventInsights2016.
        For the Cheval De Frise - An array with three values, number of times damaged, number of opportunities to damage, and percentage.

        :param a_cheval_de_frise: The a_cheval_de_frise of this EventInsights2016.
        :type: list[float]
        """
        if a_cheval_de_frise is None:
            raise ValueError("Invalid value for `a_cheval_de_frise`, must not be `None`")

        self._a_cheval_de_frise = a_cheval_de_frise

    @property
    def a_portcullis(self):
        """
        Gets the a_portcullis of this EventInsights2016.
        For the Portcullis - An array with three values, number of times damaged, number of opportunities to damage, and percentage.

        :return: The a_portcullis of this EventInsights2016.
        :rtype: list[float]
        """
        return self._a_portcullis

    @a_portcullis.setter
    def a_portcullis(self, a_portcullis):
        """
        Sets the a_portcullis of this EventInsights2016.
        For the Portcullis - An array with three values, number of times damaged, number of opportunities to damage, and percentage.

        :param a_portcullis: The a_portcullis of this EventInsights2016.
        :type: list[float]
        """
        if a_portcullis is None:
            raise ValueError("Invalid value for `a_portcullis`, must not be `None`")

        self._a_portcullis = a_portcullis

    @property
    def b_ramparts(self):
        """
        Gets the b_ramparts of this EventInsights2016.
        For the Ramparts - An array with three values, number of times damaged, number of opportunities to damage, and percentage.

        :return: The b_ramparts of this EventInsights2016.
        :rtype: list[float]
        """
        return self._b_ramparts

    @b_ramparts.setter
    def b_ramparts(self, b_ramparts):
        """
        Sets the b_ramparts of this EventInsights2016.
        For the Ramparts - An array with three values, number of times damaged, number of opportunities to damage, and percentage.

        :param b_ramparts: The b_ramparts of this EventInsights2016.
        :type: list[float]
        """
        if b_ramparts is None:
            raise ValueError("Invalid value for `b_ramparts`, must not be `None`")

        self._b_ramparts = b_ramparts

    @property
    def b_moat(self):
        """
        Gets the b_moat of this EventInsights2016.
        For the Moat - An array with three values, number of times damaged, number of opportunities to damage, and percentage.

        :return: The b_moat of this EventInsights2016.
        :rtype: list[float]
        """
        return self._b_moat

    @b_moat.setter
    def b_moat(self, b_moat):
        """
        Sets the b_moat of this EventInsights2016.
        For the Moat - An array with three values, number of times damaged, number of opportunities to damage, and percentage.

        :param b_moat: The b_moat of this EventInsights2016.
        :type: list[float]
        """
        if b_moat is None:
            raise ValueError("Invalid value for `b_moat`, must not be `None`")

        self._b_moat = b_moat

    @property
    def c_sally_port(self):
        """
        Gets the c_sally_port of this EventInsights2016.
        For the Sally Port - An array with three values, number of times damaged, number of opportunities to damage, and percentage.

        :return: The c_sally_port of this EventInsights2016.
        :rtype: list[float]
        """
        return self._c_sally_port

    @c_sally_port.setter
    def c_sally_port(self, c_sally_port):
        """
        Sets the c_sally_port of this EventInsights2016.
        For the Sally Port - An array with three values, number of times damaged, number of opportunities to damage, and percentage.

        :param c_sally_port: The c_sally_port of this EventInsights2016.
        :type: list[float]
        """
        if c_sally_port is None:
            raise ValueError("Invalid value for `c_sally_port`, must not be `None`")

        self._c_sally_port = c_sally_port

    @property
    def c_drawbridge(self):
        """
        Gets the c_drawbridge of this EventInsights2016.
        For the Drawbridge - An array with three values, number of times damaged, number of opportunities to damage, and percentage.

        :return: The c_drawbridge of this EventInsights2016.
        :rtype: list[float]
        """
        return self._c_drawbridge

    @c_drawbridge.setter
    def c_drawbridge(self, c_drawbridge):
        """
        Sets the c_drawbridge of this EventInsights2016.
        For the Drawbridge - An array with three values, number of times damaged, number of opportunities to damage, and percentage.

        :param c_drawbridge: The c_drawbridge of this EventInsights2016.
        :type: list[float]
        """
        if c_drawbridge is None:
            raise ValueError("Invalid value for `c_drawbridge`, must not be `None`")

        self._c_drawbridge = c_drawbridge

    @property
    def d_rough_terrain(self):
        """
        Gets the d_rough_terrain of this EventInsights2016.
        For the Rough Terrain - An array with three values, number of times damaged, number of opportunities to damage, and percentage.

        :return: The d_rough_terrain of this EventInsights2016.
        :rtype: list[float]
        """
        return self._d_rough_terrain

    @d_rough_terrain.setter
    def d_rough_terrain(self, d_rough_terrain):
        """
        Sets the d_rough_terrain of this EventInsights2016.
        For the Rough Terrain - An array with three values, number of times damaged, number of opportunities to damage, and percentage.

        :param d_rough_terrain: The d_rough_terrain of this EventInsights2016.
        :type: list[float]
        """
        if d_rough_terrain is None:
            raise ValueError("Invalid value for `d_rough_terrain`, must not be `None`")

        self._d_rough_terrain = d_rough_terrain

    @property
    def d_rock_wall(self):
        """
        Gets the d_rock_wall of this EventInsights2016.
        For the Rock Wall - An array with three values, number of times damaged, number of opportunities to damage, and percentage.

        :return: The d_rock_wall of this EventInsights2016.
        :rtype: list[float]
        """
        return self._d_rock_wall

    @d_rock_wall.setter
    def d_rock_wall(self, d_rock_wall):
        """
        Sets the d_rock_wall of this EventInsights2016.
        For the Rock Wall - An array with three values, number of times damaged, number of opportunities to damage, and percentage.

        :param d_rock_wall: The d_rock_wall of this EventInsights2016.
        :type: list[float]
        """
        if d_rock_wall is None:
            raise ValueError("Invalid value for `d_rock_wall`, must not be `None`")

        self._d_rock_wall = d_rock_wall

    @property
    def average_high_goals(self):
        """
        Gets the average_high_goals of this EventInsights2016.
        Average number of high goals scored.

        :return: The average_high_goals of this EventInsights2016.
        :rtype: float
        """
        return self._average_high_goals

    @average_high_goals.setter
    def average_high_goals(self, average_high_goals):
        """
        Sets the average_high_goals of this EventInsights2016.
        Average number of high goals scored.

        :param average_high_goals: The average_high_goals of this EventInsights2016.
        :type: float
        """
        if average_high_goals is None:
            raise ValueError("Invalid value for `average_high_goals`, must not be `None`")

        self._average_high_goals = average_high_goals

    @property
    def average_low_goals(self):
        """
        Gets the average_low_goals of this EventInsights2016.
        Average number of low goals scored.

        :return: The average_low_goals of this EventInsights2016.
        :rtype: float
        """
        return self._average_low_goals

    @average_low_goals.setter
    def average_low_goals(self, average_low_goals):
        """
        Sets the average_low_goals of this EventInsights2016.
        Average number of low goals scored.

        :param average_low_goals: The average_low_goals of this EventInsights2016.
        :type: float
        """
        if average_low_goals is None:
            raise ValueError("Invalid value for `average_low_goals`, must not be `None`")

        self._average_low_goals = average_low_goals

    @property
    def breaches(self):
        """
        Gets the breaches of this EventInsights2016.
        An array with three values, number of times breached, number of opportunities to breach, and percentage.

        :return: The breaches of this EventInsights2016.
        :rtype: list[float]
        """
        return self._breaches

    @breaches.setter
    def breaches(self, breaches):
        """
        Sets the breaches of this EventInsights2016.
        An array with three values, number of times breached, number of opportunities to breach, and percentage.

        :param breaches: The breaches of this EventInsights2016.
        :type: list[float]
        """
        if breaches is None:
            raise ValueError("Invalid value for `breaches`, must not be `None`")

        self._breaches = breaches

    @property
    def scales(self):
        """
        Gets the scales of this EventInsights2016.
        An array with three values, number of times scaled, number of opportunities to scale, and percentage.

        :return: The scales of this EventInsights2016.
        :rtype: list[float]
        """
        return self._scales

    @scales.setter
    def scales(self, scales):
        """
        Sets the scales of this EventInsights2016.
        An array with three values, number of times scaled, number of opportunities to scale, and percentage.

        :param scales: The scales of this EventInsights2016.
        :type: list[float]
        """
        if scales is None:
            raise ValueError("Invalid value for `scales`, must not be `None`")

        self._scales = scales

    @property
    def challenges(self):
        """
        Gets the challenges of this EventInsights2016.
        An array with three values, number of times challenged, number of opportunities to challenge, and percentage.

        :return: The challenges of this EventInsights2016.
        :rtype: list[float]
        """
        return self._challenges

    @challenges.setter
    def challenges(self, challenges):
        """
        Sets the challenges of this EventInsights2016.
        An array with three values, number of times challenged, number of opportunities to challenge, and percentage.

        :param challenges: The challenges of this EventInsights2016.
        :type: list[float]
        """
        if challenges is None:
            raise ValueError("Invalid value for `challenges`, must not be `None`")

        self._challenges = challenges

    @property
    def captures(self):
        """
        Gets the captures of this EventInsights2016.
        An array with three values, number of times captured, number of opportunities to capture, and percentage.

        :return: The captures of this EventInsights2016.
        :rtype: list[float]
        """
        return self._captures

    @captures.setter
    def captures(self, captures):
        """
        Sets the captures of this EventInsights2016.
        An array with three values, number of times captured, number of opportunities to capture, and percentage.

        :param captures: The captures of this EventInsights2016.
        :type: list[float]
        """
        if captures is None:
            raise ValueError("Invalid value for `captures`, must not be `None`")

        self._captures = captures

    @property
    def average_win_score(self):
        """
        Gets the average_win_score of this EventInsights2016.
        Average winning score.

        :return: The average_win_score of this EventInsights2016.
        :rtype: float
        """
        return self._average_win_score

    @average_win_score.setter
    def average_win_score(self, average_win_score):
        """
        Sets the average_win_score of this EventInsights2016.
        Average winning score.

        :param average_win_score: The average_win_score of this EventInsights2016.
        :type: float
        """
        if average_win_score is None:
            raise ValueError("Invalid value for `average_win_score`, must not be `None`")

        self._average_win_score = average_win_score

    @property
    def average_win_margin(self):
        """
        Gets the average_win_margin of this EventInsights2016.
        Average margin of victory.

        :return: The average_win_margin of this EventInsights2016.
        :rtype: float
        """
        return self._average_win_margin

    @average_win_margin.setter
    def average_win_margin(self, average_win_margin):
        """
        Sets the average_win_margin of this EventInsights2016.
        Average margin of victory.

        :param average_win_margin: The average_win_margin of this EventInsights2016.
        :type: float
        """
        if average_win_margin is None:
            raise ValueError("Invalid value for `average_win_margin`, must not be `None`")

        self._average_win_margin = average_win_margin

    @property
    def average_score(self):
        """
        Gets the average_score of this EventInsights2016.
        Average total score.

        :return: The average_score of this EventInsights2016.
        :rtype: float
        """
        return self._average_score

    @average_score.setter
    def average_score(self, average_score):
        """
        Sets the average_score of this EventInsights2016.
        Average total score.

        :param average_score: The average_score of this EventInsights2016.
        :type: float
        """
        if average_score is None:
            raise ValueError("Invalid value for `average_score`, must not be `None`")

        self._average_score = average_score

    @property
    def average_auto_score(self):
        """
        Gets the average_auto_score of this EventInsights2016.
        Average autonomous score.

        :return: The average_auto_score of this EventInsights2016.
        :rtype: float
        """
        return self._average_auto_score

    @average_auto_score.setter
    def average_auto_score(self, average_auto_score):
        """
        Sets the average_auto_score of this EventInsights2016.
        Average autonomous score.

        :param average_auto_score: The average_auto_score of this EventInsights2016.
        :type: float
        """
        if average_auto_score is None:
            raise ValueError("Invalid value for `average_auto_score`, must not be `None`")

        self._average_auto_score = average_auto_score

    @property
    def average_crossing_score(self):
        """
        Gets the average_crossing_score of this EventInsights2016.
        Average crossing score.

        :return: The average_crossing_score of this EventInsights2016.
        :rtype: float
        """
        return self._average_crossing_score

    @average_crossing_score.setter
    def average_crossing_score(self, average_crossing_score):
        """
        Sets the average_crossing_score of this EventInsights2016.
        Average crossing score.

        :param average_crossing_score: The average_crossing_score of this EventInsights2016.
        :type: float
        """
        if average_crossing_score is None:
            raise ValueError("Invalid value for `average_crossing_score`, must not be `None`")

        self._average_crossing_score = average_crossing_score

    @property
    def average_boulder_score(self):
        """
        Gets the average_boulder_score of this EventInsights2016.
        Average boulder score.

        :return: The average_boulder_score of this EventInsights2016.
        :rtype: float
        """
        return self._average_boulder_score

    @average_boulder_score.setter
    def average_boulder_score(self, average_boulder_score):
        """
        Sets the average_boulder_score of this EventInsights2016.
        Average boulder score.

        :param average_boulder_score: The average_boulder_score of this EventInsights2016.
        :type: float
        """
        if average_boulder_score is None:
            raise ValueError("Invalid value for `average_boulder_score`, must not be `None`")

        self._average_boulder_score = average_boulder_score

    @property
    def average_tower_score(self):
        """
        Gets the average_tower_score of this EventInsights2016.
        Average tower score.

        :return: The average_tower_score of this EventInsights2016.
        :rtype: float
        """
        return self._average_tower_score

    @average_tower_score.setter
    def average_tower_score(self, average_tower_score):
        """
        Sets the average_tower_score of this EventInsights2016.
        Average tower score.

        :param average_tower_score: The average_tower_score of this EventInsights2016.
        :type: float
        """
        if average_tower_score is None:
            raise ValueError("Invalid value for `average_tower_score`, must not be `None`")

        self._average_tower_score = average_tower_score

    @property
    def average_foul_score(self):
        """
        Gets the average_foul_score of this EventInsights2016.
        Average foul score.

        :return: The average_foul_score of this EventInsights2016.
        :rtype: float
        """
        return self._average_foul_score

    @average_foul_score.setter
    def average_foul_score(self, average_foul_score):
        """
        Sets the average_foul_score of this EventInsights2016.
        Average foul score.

        :param average_foul_score: The average_foul_score of this EventInsights2016.
        :type: float
        """
        if average_foul_score is None:
            raise ValueError("Invalid value for `average_foul_score`, must not be `None`")

        self._average_foul_score = average_foul_score

    @property
    def high_score(self):
        """
        Gets the high_score of this EventInsights2016.
        An array with three values, high score, match key from the match with the high score, and the name of the match.

        :return: The high_score of this EventInsights2016.
        :rtype: list[str]
        """
        return self._high_score

    @high_score.setter
    def high_score(self, high_score):
        """
        Sets the high_score of this EventInsights2016.
        An array with three values, high score, match key from the match with the high score, and the name of the match.

        :param high_score: The high_score of this EventInsights2016.
        :type: list[str]
        """
        if high_score is None:
            raise ValueError("Invalid value for `high_score`, must not be `None`")

        self._high_score = high_score

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
        if not isinstance(other, EventInsights2016):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
