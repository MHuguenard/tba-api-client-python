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


class TeamEventStatusAllianceBackup(object):
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
        'out': 'str',
        '_in': 'str'
    }

    attribute_map = {
        'out': 'out',
        '_in': 'in'
    }

    def __init__(self, out=None, _in=None):
        """
        TeamEventStatusAllianceBackup - a model defined in Swagger
        """

        self._out = None
        self.__in = None

        if out is not None:
          self.out = out
        if _in is not None:
          self._in = _in

    @property
    def out(self):
        """
        Gets the out of this TeamEventStatusAllianceBackup.
        TBA key for the team replaced by the backup.

        :return: The out of this TeamEventStatusAllianceBackup.
        :rtype: str
        """
        return self._out

    @out.setter
    def out(self, out):
        """
        Sets the out of this TeamEventStatusAllianceBackup.
        TBA key for the team replaced by the backup.

        :param out: The out of this TeamEventStatusAllianceBackup.
        :type: str
        """

        self._out = out

    @property
    def _in(self):
        """
        Gets the _in of this TeamEventStatusAllianceBackup.
        TBA key for the backup team called in.

        :return: The _in of this TeamEventStatusAllianceBackup.
        :rtype: str
        """
        return self.__in

    @_in.setter
    def _in(self, _in):
        """
        Sets the _in of this TeamEventStatusAllianceBackup.
        TBA key for the backup team called in.

        :param _in: The _in of this TeamEventStatusAllianceBackup.
        :type: str
        """

        self.__in = _in

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
        if not isinstance(other, TeamEventStatusAllianceBackup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other