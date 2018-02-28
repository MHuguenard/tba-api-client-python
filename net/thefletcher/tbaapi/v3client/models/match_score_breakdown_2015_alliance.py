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


class MatchScoreBreakdown2015Alliance(object):
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
        'auto_points': 'int',
        'teleop_points': 'int',
        'container_points': 'int',
        'tote_points': 'int',
        'litter_points': 'int',
        'foul_points': 'int',
        'adjust_points': 'int',
        'total_points': 'int',
        'foul_count': 'int',
        'tote_count_far': 'int',
        'tote_count_near': 'int',
        'tote_set': 'bool',
        'tote_stack': 'bool',
        'container_count_level1': 'int',
        'container_count_level2': 'int',
        'container_count_level3': 'int',
        'container_count_level4': 'int',
        'container_count_level5': 'int',
        'container_count_level6': 'int',
        'container_set': 'bool',
        'litter_count_container': 'int',
        'litter_count_landfill': 'int',
        'litter_count_unprocessed': 'int',
        'robot_set': 'bool'
    }

    attribute_map = {
        'auto_points': 'auto_points',
        'teleop_points': 'teleop_points',
        'container_points': 'container_points',
        'tote_points': 'tote_points',
        'litter_points': 'litter_points',
        'foul_points': 'foul_points',
        'adjust_points': 'adjust_points',
        'total_points': 'total_points',
        'foul_count': 'foul_count',
        'tote_count_far': 'tote_count_far',
        'tote_count_near': 'tote_count_near',
        'tote_set': 'tote_set',
        'tote_stack': 'tote_stack',
        'container_count_level1': 'container_count_level1',
        'container_count_level2': 'container_count_level2',
        'container_count_level3': 'container_count_level3',
        'container_count_level4': 'container_count_level4',
        'container_count_level5': 'container_count_level5',
        'container_count_level6': 'container_count_level6',
        'container_set': 'container_set',
        'litter_count_container': 'litter_count_container',
        'litter_count_landfill': 'litter_count_landfill',
        'litter_count_unprocessed': 'litter_count_unprocessed',
        'robot_set': 'robot_set'
    }

    def __init__(self, auto_points=None, teleop_points=None, container_points=None, tote_points=None, litter_points=None, foul_points=None, adjust_points=None, total_points=None, foul_count=None, tote_count_far=None, tote_count_near=None, tote_set=None, tote_stack=None, container_count_level1=None, container_count_level2=None, container_count_level3=None, container_count_level4=None, container_count_level5=None, container_count_level6=None, container_set=None, litter_count_container=None, litter_count_landfill=None, litter_count_unprocessed=None, robot_set=None):
        """
        MatchScoreBreakdown2015Alliance - a model defined in Swagger
        """

        self._auto_points = None
        self._teleop_points = None
        self._container_points = None
        self._tote_points = None
        self._litter_points = None
        self._foul_points = None
        self._adjust_points = None
        self._total_points = None
        self._foul_count = None
        self._tote_count_far = None
        self._tote_count_near = None
        self._tote_set = None
        self._tote_stack = None
        self._container_count_level1 = None
        self._container_count_level2 = None
        self._container_count_level3 = None
        self._container_count_level4 = None
        self._container_count_level5 = None
        self._container_count_level6 = None
        self._container_set = None
        self._litter_count_container = None
        self._litter_count_landfill = None
        self._litter_count_unprocessed = None
        self._robot_set = None

        if auto_points is not None:
          self.auto_points = auto_points
        if teleop_points is not None:
          self.teleop_points = teleop_points
        if container_points is not None:
          self.container_points = container_points
        if tote_points is not None:
          self.tote_points = tote_points
        if litter_points is not None:
          self.litter_points = litter_points
        if foul_points is not None:
          self.foul_points = foul_points
        if adjust_points is not None:
          self.adjust_points = adjust_points
        if total_points is not None:
          self.total_points = total_points
        if foul_count is not None:
          self.foul_count = foul_count
        if tote_count_far is not None:
          self.tote_count_far = tote_count_far
        if tote_count_near is not None:
          self.tote_count_near = tote_count_near
        if tote_set is not None:
          self.tote_set = tote_set
        if tote_stack is not None:
          self.tote_stack = tote_stack
        if container_count_level1 is not None:
          self.container_count_level1 = container_count_level1
        if container_count_level2 is not None:
          self.container_count_level2 = container_count_level2
        if container_count_level3 is not None:
          self.container_count_level3 = container_count_level3
        if container_count_level4 is not None:
          self.container_count_level4 = container_count_level4
        if container_count_level5 is not None:
          self.container_count_level5 = container_count_level5
        if container_count_level6 is not None:
          self.container_count_level6 = container_count_level6
        if container_set is not None:
          self.container_set = container_set
        if litter_count_container is not None:
          self.litter_count_container = litter_count_container
        if litter_count_landfill is not None:
          self.litter_count_landfill = litter_count_landfill
        if litter_count_unprocessed is not None:
          self.litter_count_unprocessed = litter_count_unprocessed
        if robot_set is not None:
          self.robot_set = robot_set

    @property
    def auto_points(self):
        """
        Gets the auto_points of this MatchScoreBreakdown2015Alliance.

        :return: The auto_points of this MatchScoreBreakdown2015Alliance.
        :rtype: int
        """
        return self._auto_points

    @auto_points.setter
    def auto_points(self, auto_points):
        """
        Sets the auto_points of this MatchScoreBreakdown2015Alliance.

        :param auto_points: The auto_points of this MatchScoreBreakdown2015Alliance.
        :type: int
        """

        self._auto_points = auto_points

    @property
    def teleop_points(self):
        """
        Gets the teleop_points of this MatchScoreBreakdown2015Alliance.

        :return: The teleop_points of this MatchScoreBreakdown2015Alliance.
        :rtype: int
        """
        return self._teleop_points

    @teleop_points.setter
    def teleop_points(self, teleop_points):
        """
        Sets the teleop_points of this MatchScoreBreakdown2015Alliance.

        :param teleop_points: The teleop_points of this MatchScoreBreakdown2015Alliance.
        :type: int
        """

        self._teleop_points = teleop_points

    @property
    def container_points(self):
        """
        Gets the container_points of this MatchScoreBreakdown2015Alliance.

        :return: The container_points of this MatchScoreBreakdown2015Alliance.
        :rtype: int
        """
        return self._container_points

    @container_points.setter
    def container_points(self, container_points):
        """
        Sets the container_points of this MatchScoreBreakdown2015Alliance.

        :param container_points: The container_points of this MatchScoreBreakdown2015Alliance.
        :type: int
        """

        self._container_points = container_points

    @property
    def tote_points(self):
        """
        Gets the tote_points of this MatchScoreBreakdown2015Alliance.

        :return: The tote_points of this MatchScoreBreakdown2015Alliance.
        :rtype: int
        """
        return self._tote_points

    @tote_points.setter
    def tote_points(self, tote_points):
        """
        Sets the tote_points of this MatchScoreBreakdown2015Alliance.

        :param tote_points: The tote_points of this MatchScoreBreakdown2015Alliance.
        :type: int
        """

        self._tote_points = tote_points

    @property
    def litter_points(self):
        """
        Gets the litter_points of this MatchScoreBreakdown2015Alliance.

        :return: The litter_points of this MatchScoreBreakdown2015Alliance.
        :rtype: int
        """
        return self._litter_points

    @litter_points.setter
    def litter_points(self, litter_points):
        """
        Sets the litter_points of this MatchScoreBreakdown2015Alliance.

        :param litter_points: The litter_points of this MatchScoreBreakdown2015Alliance.
        :type: int
        """

        self._litter_points = litter_points

    @property
    def foul_points(self):
        """
        Gets the foul_points of this MatchScoreBreakdown2015Alliance.

        :return: The foul_points of this MatchScoreBreakdown2015Alliance.
        :rtype: int
        """
        return self._foul_points

    @foul_points.setter
    def foul_points(self, foul_points):
        """
        Sets the foul_points of this MatchScoreBreakdown2015Alliance.

        :param foul_points: The foul_points of this MatchScoreBreakdown2015Alliance.
        :type: int
        """

        self._foul_points = foul_points

    @property
    def adjust_points(self):
        """
        Gets the adjust_points of this MatchScoreBreakdown2015Alliance.

        :return: The adjust_points of this MatchScoreBreakdown2015Alliance.
        :rtype: int
        """
        return self._adjust_points

    @adjust_points.setter
    def adjust_points(self, adjust_points):
        """
        Sets the adjust_points of this MatchScoreBreakdown2015Alliance.

        :param adjust_points: The adjust_points of this MatchScoreBreakdown2015Alliance.
        :type: int
        """

        self._adjust_points = adjust_points

    @property
    def total_points(self):
        """
        Gets the total_points of this MatchScoreBreakdown2015Alliance.

        :return: The total_points of this MatchScoreBreakdown2015Alliance.
        :rtype: int
        """
        return self._total_points

    @total_points.setter
    def total_points(self, total_points):
        """
        Sets the total_points of this MatchScoreBreakdown2015Alliance.

        :param total_points: The total_points of this MatchScoreBreakdown2015Alliance.
        :type: int
        """

        self._total_points = total_points

    @property
    def foul_count(self):
        """
        Gets the foul_count of this MatchScoreBreakdown2015Alliance.

        :return: The foul_count of this MatchScoreBreakdown2015Alliance.
        :rtype: int
        """
        return self._foul_count

    @foul_count.setter
    def foul_count(self, foul_count):
        """
        Sets the foul_count of this MatchScoreBreakdown2015Alliance.

        :param foul_count: The foul_count of this MatchScoreBreakdown2015Alliance.
        :type: int
        """

        self._foul_count = foul_count

    @property
    def tote_count_far(self):
        """
        Gets the tote_count_far of this MatchScoreBreakdown2015Alliance.

        :return: The tote_count_far of this MatchScoreBreakdown2015Alliance.
        :rtype: int
        """
        return self._tote_count_far

    @tote_count_far.setter
    def tote_count_far(self, tote_count_far):
        """
        Sets the tote_count_far of this MatchScoreBreakdown2015Alliance.

        :param tote_count_far: The tote_count_far of this MatchScoreBreakdown2015Alliance.
        :type: int
        """

        self._tote_count_far = tote_count_far

    @property
    def tote_count_near(self):
        """
        Gets the tote_count_near of this MatchScoreBreakdown2015Alliance.

        :return: The tote_count_near of this MatchScoreBreakdown2015Alliance.
        :rtype: int
        """
        return self._tote_count_near

    @tote_count_near.setter
    def tote_count_near(self, tote_count_near):
        """
        Sets the tote_count_near of this MatchScoreBreakdown2015Alliance.

        :param tote_count_near: The tote_count_near of this MatchScoreBreakdown2015Alliance.
        :type: int
        """

        self._tote_count_near = tote_count_near

    @property
    def tote_set(self):
        """
        Gets the tote_set of this MatchScoreBreakdown2015Alliance.

        :return: The tote_set of this MatchScoreBreakdown2015Alliance.
        :rtype: bool
        """
        return self._tote_set

    @tote_set.setter
    def tote_set(self, tote_set):
        """
        Sets the tote_set of this MatchScoreBreakdown2015Alliance.

        :param tote_set: The tote_set of this MatchScoreBreakdown2015Alliance.
        :type: bool
        """

        self._tote_set = tote_set

    @property
    def tote_stack(self):
        """
        Gets the tote_stack of this MatchScoreBreakdown2015Alliance.

        :return: The tote_stack of this MatchScoreBreakdown2015Alliance.
        :rtype: bool
        """
        return self._tote_stack

    @tote_stack.setter
    def tote_stack(self, tote_stack):
        """
        Sets the tote_stack of this MatchScoreBreakdown2015Alliance.

        :param tote_stack: The tote_stack of this MatchScoreBreakdown2015Alliance.
        :type: bool
        """

        self._tote_stack = tote_stack

    @property
    def container_count_level1(self):
        """
        Gets the container_count_level1 of this MatchScoreBreakdown2015Alliance.

        :return: The container_count_level1 of this MatchScoreBreakdown2015Alliance.
        :rtype: int
        """
        return self._container_count_level1

    @container_count_level1.setter
    def container_count_level1(self, container_count_level1):
        """
        Sets the container_count_level1 of this MatchScoreBreakdown2015Alliance.

        :param container_count_level1: The container_count_level1 of this MatchScoreBreakdown2015Alliance.
        :type: int
        """

        self._container_count_level1 = container_count_level1

    @property
    def container_count_level2(self):
        """
        Gets the container_count_level2 of this MatchScoreBreakdown2015Alliance.

        :return: The container_count_level2 of this MatchScoreBreakdown2015Alliance.
        :rtype: int
        """
        return self._container_count_level2

    @container_count_level2.setter
    def container_count_level2(self, container_count_level2):
        """
        Sets the container_count_level2 of this MatchScoreBreakdown2015Alliance.

        :param container_count_level2: The container_count_level2 of this MatchScoreBreakdown2015Alliance.
        :type: int
        """

        self._container_count_level2 = container_count_level2

    @property
    def container_count_level3(self):
        """
        Gets the container_count_level3 of this MatchScoreBreakdown2015Alliance.

        :return: The container_count_level3 of this MatchScoreBreakdown2015Alliance.
        :rtype: int
        """
        return self._container_count_level3

    @container_count_level3.setter
    def container_count_level3(self, container_count_level3):
        """
        Sets the container_count_level3 of this MatchScoreBreakdown2015Alliance.

        :param container_count_level3: The container_count_level3 of this MatchScoreBreakdown2015Alliance.
        :type: int
        """

        self._container_count_level3 = container_count_level3

    @property
    def container_count_level4(self):
        """
        Gets the container_count_level4 of this MatchScoreBreakdown2015Alliance.

        :return: The container_count_level4 of this MatchScoreBreakdown2015Alliance.
        :rtype: int
        """
        return self._container_count_level4

    @container_count_level4.setter
    def container_count_level4(self, container_count_level4):
        """
        Sets the container_count_level4 of this MatchScoreBreakdown2015Alliance.

        :param container_count_level4: The container_count_level4 of this MatchScoreBreakdown2015Alliance.
        :type: int
        """

        self._container_count_level4 = container_count_level4

    @property
    def container_count_level5(self):
        """
        Gets the container_count_level5 of this MatchScoreBreakdown2015Alliance.

        :return: The container_count_level5 of this MatchScoreBreakdown2015Alliance.
        :rtype: int
        """
        return self._container_count_level5

    @container_count_level5.setter
    def container_count_level5(self, container_count_level5):
        """
        Sets the container_count_level5 of this MatchScoreBreakdown2015Alliance.

        :param container_count_level5: The container_count_level5 of this MatchScoreBreakdown2015Alliance.
        :type: int
        """

        self._container_count_level5 = container_count_level5

    @property
    def container_count_level6(self):
        """
        Gets the container_count_level6 of this MatchScoreBreakdown2015Alliance.

        :return: The container_count_level6 of this MatchScoreBreakdown2015Alliance.
        :rtype: int
        """
        return self._container_count_level6

    @container_count_level6.setter
    def container_count_level6(self, container_count_level6):
        """
        Sets the container_count_level6 of this MatchScoreBreakdown2015Alliance.

        :param container_count_level6: The container_count_level6 of this MatchScoreBreakdown2015Alliance.
        :type: int
        """

        self._container_count_level6 = container_count_level6

    @property
    def container_set(self):
        """
        Gets the container_set of this MatchScoreBreakdown2015Alliance.

        :return: The container_set of this MatchScoreBreakdown2015Alliance.
        :rtype: bool
        """
        return self._container_set

    @container_set.setter
    def container_set(self, container_set):
        """
        Sets the container_set of this MatchScoreBreakdown2015Alliance.

        :param container_set: The container_set of this MatchScoreBreakdown2015Alliance.
        :type: bool
        """

        self._container_set = container_set

    @property
    def litter_count_container(self):
        """
        Gets the litter_count_container of this MatchScoreBreakdown2015Alliance.

        :return: The litter_count_container of this MatchScoreBreakdown2015Alliance.
        :rtype: int
        """
        return self._litter_count_container

    @litter_count_container.setter
    def litter_count_container(self, litter_count_container):
        """
        Sets the litter_count_container of this MatchScoreBreakdown2015Alliance.

        :param litter_count_container: The litter_count_container of this MatchScoreBreakdown2015Alliance.
        :type: int
        """

        self._litter_count_container = litter_count_container

    @property
    def litter_count_landfill(self):
        """
        Gets the litter_count_landfill of this MatchScoreBreakdown2015Alliance.

        :return: The litter_count_landfill of this MatchScoreBreakdown2015Alliance.
        :rtype: int
        """
        return self._litter_count_landfill

    @litter_count_landfill.setter
    def litter_count_landfill(self, litter_count_landfill):
        """
        Sets the litter_count_landfill of this MatchScoreBreakdown2015Alliance.

        :param litter_count_landfill: The litter_count_landfill of this MatchScoreBreakdown2015Alliance.
        :type: int
        """

        self._litter_count_landfill = litter_count_landfill

    @property
    def litter_count_unprocessed(self):
        """
        Gets the litter_count_unprocessed of this MatchScoreBreakdown2015Alliance.

        :return: The litter_count_unprocessed of this MatchScoreBreakdown2015Alliance.
        :rtype: int
        """
        return self._litter_count_unprocessed

    @litter_count_unprocessed.setter
    def litter_count_unprocessed(self, litter_count_unprocessed):
        """
        Sets the litter_count_unprocessed of this MatchScoreBreakdown2015Alliance.

        :param litter_count_unprocessed: The litter_count_unprocessed of this MatchScoreBreakdown2015Alliance.
        :type: int
        """

        self._litter_count_unprocessed = litter_count_unprocessed

    @property
    def robot_set(self):
        """
        Gets the robot_set of this MatchScoreBreakdown2015Alliance.

        :return: The robot_set of this MatchScoreBreakdown2015Alliance.
        :rtype: bool
        """
        return self._robot_set

    @robot_set.setter
    def robot_set(self, robot_set):
        """
        Sets the robot_set of this MatchScoreBreakdown2015Alliance.

        :param robot_set: The robot_set of this MatchScoreBreakdown2015Alliance.
        :type: bool
        """

        self._robot_set = robot_set

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
        if not isinstance(other, MatchScoreBreakdown2015Alliance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
