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


class EliminationAlliance(object):
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
        'backup': 'EliminationAllianceBackup',
        'declines': 'list[str]',
        'picks': 'list[str]',
        'status': 'EliminationAllianceStatus'
    }

    attribute_map = {
        'name': 'name',
        'backup': 'backup',
        'declines': 'declines',
        'picks': 'picks',
        'status': 'status'
    }

    def __init__(self, name=None, backup=None, declines=None, picks=None, status=None):
        """
        EliminationAlliance - a model defined in Swagger
        """

        self._name = None
        self._backup = None
        self._declines = None
        self._picks = None
        self._status = None

        if name is not None:
          self.name = name
        if backup is not None:
          self.backup = backup
        if declines is not None:
          self.declines = declines
        self.picks = picks
        if status is not None:
          self.status = status

    @property
    def name(self):
        """
        Gets the name of this EliminationAlliance.
        Alliance name, may be null.

        :return: The name of this EliminationAlliance.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this EliminationAlliance.
        Alliance name, may be null.

        :param name: The name of this EliminationAlliance.
        :type: str
        """

        self._name = name

    @property
    def backup(self):
        """
        Gets the backup of this EliminationAlliance.

        :return: The backup of this EliminationAlliance.
        :rtype: EliminationAllianceBackup
        """
        return self._backup

    @backup.setter
    def backup(self, backup):
        """
        Sets the backup of this EliminationAlliance.

        :param backup: The backup of this EliminationAlliance.
        :type: EliminationAllianceBackup
        """

        self._backup = backup

    @property
    def declines(self):
        """
        Gets the declines of this EliminationAlliance.
        List of teams that declined the alliance.

        :return: The declines of this EliminationAlliance.
        :rtype: list[str]
        """
        return self._declines

    @declines.setter
    def declines(self, declines):
        """
        Sets the declines of this EliminationAlliance.
        List of teams that declined the alliance.

        :param declines: The declines of this EliminationAlliance.
        :type: list[str]
        """

        self._declines = declines

    @property
    def picks(self):
        """
        Gets the picks of this EliminationAlliance.
        List of team keys picked for the alliance. First pick is captain.

        :return: The picks of this EliminationAlliance.
        :rtype: list[str]
        """
        return self._picks

    @picks.setter
    def picks(self, picks):
        """
        Sets the picks of this EliminationAlliance.
        List of team keys picked for the alliance. First pick is captain.

        :param picks: The picks of this EliminationAlliance.
        :type: list[str]
        """
        if picks is None:
            raise ValueError("Invalid value for `picks`, must not be `None`")

        self._picks = picks

    @property
    def status(self):
        """
        Gets the status of this EliminationAlliance.

        :return: The status of this EliminationAlliance.
        :rtype: EliminationAllianceStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this EliminationAlliance.

        :param status: The status of this EliminationAlliance.
        :type: EliminationAllianceStatus
        """

        self._status = status

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
        if not isinstance(other, EliminationAlliance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
