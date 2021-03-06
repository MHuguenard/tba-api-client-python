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
from net.thefletcher.tbaapi.v3client.apis.event_api import EventApi


class TestEventApi(unittest.TestCase):
    """ EventApi unit test stubs """

    def setUp(self):
        self.api = net.thefletcher.tbaapi.v3client.apis.event_api.EventApi()

    def tearDown(self):
        pass

    def test_get_district_events(self):
        """
        Test case for get_district_events

        
        """
        pass

    def test_get_district_events_keys(self):
        """
        Test case for get_district_events_keys

        
        """
        pass

    def test_get_district_events_simple(self):
        """
        Test case for get_district_events_simple

        
        """
        pass

    def test_get_event(self):
        """
        Test case for get_event

        
        """
        pass

    def test_get_event_alliances(self):
        """
        Test case for get_event_alliances

        
        """
        pass

    def test_get_event_awards(self):
        """
        Test case for get_event_awards

        
        """
        pass

    def test_get_event_district_points(self):
        """
        Test case for get_event_district_points

        
        """
        pass

    def test_get_event_insights(self):
        """
        Test case for get_event_insights

        
        """
        pass

    def test_get_event_matches(self):
        """
        Test case for get_event_matches

        
        """
        pass

    def test_get_event_matches_keys(self):
        """
        Test case for get_event_matches_keys

        
        """
        pass

    def test_get_event_matches_simple(self):
        """
        Test case for get_event_matches_simple

        
        """
        pass

    def test_get_event_op_rs(self):
        """
        Test case for get_event_op_rs

        
        """
        pass

    def test_get_event_predictions(self):
        """
        Test case for get_event_predictions

        
        """
        pass

    def test_get_event_rankings(self):
        """
        Test case for get_event_rankings

        
        """
        pass

    def test_get_event_simple(self):
        """
        Test case for get_event_simple

        
        """
        pass

    def test_get_event_teams(self):
        """
        Test case for get_event_teams

        
        """
        pass

    def test_get_event_teams_keys(self):
        """
        Test case for get_event_teams_keys

        
        """
        pass

    def test_get_event_teams_simple(self):
        """
        Test case for get_event_teams_simple

        
        """
        pass

    def test_get_events_by_year(self):
        """
        Test case for get_events_by_year

        
        """
        pass

    def test_get_events_by_year_keys(self):
        """
        Test case for get_events_by_year_keys

        
        """
        pass

    def test_get_events_by_year_simple(self):
        """
        Test case for get_events_by_year_simple

        
        """
        pass

    def test_get_team_event_awards(self):
        """
        Test case for get_team_event_awards

        
        """
        pass

    def test_get_team_event_matches(self):
        """
        Test case for get_team_event_matches

        
        """
        pass

    def test_get_team_event_matches_keys(self):
        """
        Test case for get_team_event_matches_keys

        
        """
        pass

    def test_get_team_event_matches_simple(self):
        """
        Test case for get_team_event_matches_simple

        
        """
        pass

    def test_get_team_event_status(self):
        """
        Test case for get_team_event_status

        
        """
        pass

    def test_get_team_events(self):
        """
        Test case for get_team_events

        
        """
        pass

    def test_get_team_events_by_year(self):
        """
        Test case for get_team_events_by_year

        
        """
        pass

    def test_get_team_events_by_year_keys(self):
        """
        Test case for get_team_events_by_year_keys

        
        """
        pass

    def test_get_team_events_by_year_simple(self):
        """
        Test case for get_team_events_by_year_simple

        
        """
        pass

    def test_get_team_events_keys(self):
        """
        Test case for get_team_events_keys

        
        """
        pass

    def test_get_team_events_simple(self):
        """
        Test case for get_team_events_simple

        
        """
        pass


if __name__ == '__main__':
    unittest.main()
