# coding: utf-8

"""
    The Blue Alliance API v3

    # Overview    Information and statistics about FIRST Robotics Competition teams and events. If you are looking for the old version (v2) of the API, documentation can be found [here](/apidocs/v2).   # Authentication   All endpoints require an Auth Key to be passed in the header `X-TBA-Auth-Key`. If you do not have an auth key yet, you can obtain one from your [Account Page](/account).    A `User-Agent` header may need to be set to prevent a 403 Unauthorized error.

    OpenAPI spec version: 3.0.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import net.thefletcher.tbaapi.v3client
from net.thefletcher.tbaapi.v3client.rest import ApiException
from net.thefletcher.tbaapi.v3client.models.team_event_status_alliance_backup import TeamEventStatusAllianceBackup


class TestTeamEventStatusAllianceBackup(unittest.TestCase):
    """ TeamEventStatusAllianceBackup unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTeamEventStatusAllianceBackup(self):
        """
        Test TeamEventStatusAllianceBackup
        """
        # FIXME: construct object with mandatory attributes with example values
        #model = net.thefletcher.tbaapi.v3client.models.team_event_status_alliance_backup.TeamEventStatusAllianceBackup()
        pass


if __name__ == '__main__':
    unittest.main()
