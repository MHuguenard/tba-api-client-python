# coding: utf-8

"""
    The Blue Alliance API v3

    # Overview    Information and statistics about FIRST Robotics Competition teams and events.   # Authentication   All endpoints require an Auth Key to be passed in the header `X-TBA-Auth-Key`. If you do not have an auth key yet, you can obtain one from your [Account Page](/account).    A `User-Agent` header may need to be set to prevent a 403 Unauthorized error.

    OpenAPI spec version: 3.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class EventOPRs(object):
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
        'oprs': 'dict(str, float)',
        'dprs': 'dict(str, float)',
        'ccwms': 'dict(str, float)'
    }

    attribute_map = {
        'oprs': 'oprs',
        'dprs': 'dprs',
        'ccwms': 'ccwms'
    }

    def __init__(self, oprs=None, dprs=None, ccwms=None):
        """
        EventOPRs - a model defined in Swagger
        """

        self._oprs = None
        self._dprs = None
        self._ccwms = None

        if oprs is not None:
          self.oprs = oprs
        if dprs is not None:
          self.dprs = dprs
        if ccwms is not None:
          self.ccwms = ccwms

    @property
    def oprs(self):
        """
        Gets the oprs of this EventOPRs.
        A key-value pair with team key (eg `frc254`) as key and OPR as value.

        :return: The oprs of this EventOPRs.
        :rtype: dict(str, float)
        """
        return self._oprs

    @oprs.setter
    def oprs(self, oprs):
        """
        Sets the oprs of this EventOPRs.
        A key-value pair with team key (eg `frc254`) as key and OPR as value.

        :param oprs: The oprs of this EventOPRs.
        :type: dict(str, float)
        """

        self._oprs = oprs

    @property
    def dprs(self):
        """
        Gets the dprs of this EventOPRs.
        A key-value pair with team key (eg `frc254`) as key and DPR as value.

        :return: The dprs of this EventOPRs.
        :rtype: dict(str, float)
        """
        return self._dprs

    @dprs.setter
    def dprs(self, dprs):
        """
        Sets the dprs of this EventOPRs.
        A key-value pair with team key (eg `frc254`) as key and DPR as value.

        :param dprs: The dprs of this EventOPRs.
        :type: dict(str, float)
        """

        self._dprs = dprs

    @property
    def ccwms(self):
        """
        Gets the ccwms of this EventOPRs.
        A key-value pair with team key (eg `frc254`) as key and CCWM as value.

        :return: The ccwms of this EventOPRs.
        :rtype: dict(str, float)
        """
        return self._ccwms

    @ccwms.setter
    def ccwms(self, ccwms):
        """
        Sets the ccwms of this EventOPRs.
        A key-value pair with team key (eg `frc254`) as key and CCWM as value.

        :param ccwms: The ccwms of this EventOPRs.
        :type: dict(str, float)
        """

        self._ccwms = ccwms

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
        if not isinstance(other, EventOPRs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
