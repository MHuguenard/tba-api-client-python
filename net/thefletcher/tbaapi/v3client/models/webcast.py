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


class Webcast(object):
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
        'type': 'str',
        'channel': 'str',
        'file': 'str'
    }

    attribute_map = {
        'type': 'type',
        'channel': 'channel',
        'file': 'file'
    }

    def __init__(self, type=None, channel=None, file=None):
        """
        Webcast - a model defined in Swagger
        """

        self._type = None
        self._channel = None
        self._file = None

        self.type = type
        self.channel = channel
        if file is not None:
          self.file = file

    @property
    def type(self):
        """
        Gets the type of this Webcast.
        Type of webcast, typically descriptive of the streaming provider.

        :return: The type of this Webcast.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Webcast.
        Type of webcast, typically descriptive of the streaming provider.

        :param type: The type of this Webcast.
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")
        allowed_values = ["youtube", "twitch", "ustream", "iframe", "html5", "rtmp", "livestream"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def channel(self):
        """
        Gets the channel of this Webcast.
        Type specific channel information. May be the YouTube stream, or Twitch channel name. In the case of iframe types, contains HTML to embed the stream in an HTML iframe.

        :return: The channel of this Webcast.
        :rtype: str
        """
        return self._channel

    @channel.setter
    def channel(self, channel):
        """
        Sets the channel of this Webcast.
        Type specific channel information. May be the YouTube stream, or Twitch channel name. In the case of iframe types, contains HTML to embed the stream in an HTML iframe.

        :param channel: The channel of this Webcast.
        :type: str
        """
        if channel is None:
            raise ValueError("Invalid value for `channel`, must not be `None`")

        self._channel = channel

    @property
    def file(self):
        """
        Gets the file of this Webcast.
        File identification as may be required for some types. May be null.

        :return: The file of this Webcast.
        :rtype: str
        """
        return self._file

    @file.setter
    def file(self, file):
        """
        Sets the file of this Webcast.
        File identification as may be required for some types. May be null.

        :param file: The file of this Webcast.
        :type: str
        """

        self._file = file

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
        if not isinstance(other, Webcast):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
