# coding: utf-8

"""
    The Blue Alliance API v3

    # Overview    Information and statistics about FIRST Robotics Competition teams and events. If you are looking for the old version (v2) of the API, documentation can be found [here](/apidocs/v2).   # Authentication   All endpoints require an Auth Key to be passed in the header `X-TBA-Auth-Key`. If you do not have an auth key yet, you can obtain one from your [Account Page](/account).    A `User-Agent` header may need to be set to prevent a 403 Unauthorized error.

    OpenAPI spec version: 3.0.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import models into sdk package
from .models.api_status import APIStatus
from .models.api_status_app_version import APIStatusAppVersion
from .models.award import Award
from .models.award_recipient import AwardRecipient
from .models.district_list import DistrictList
from .models.district_ranking import DistrictRanking
from .models.district_ranking_event_points import DistrictRankingEventPoints
from .models.elimination_alliance import EliminationAlliance
from .models.elimination_alliance_backup import EliminationAllianceBackup
from .models.elimination_alliance_status import EliminationAllianceStatus
from .models.event import Event
from .models.event_district_points import EventDistrictPoints
from .models.event_district_points_points import EventDistrictPointsPoints
from .models.event_district_points_tiebreakers import EventDistrictPointsTiebreakers
from .models.event_insights_2016 import EventInsights2016
from .models.event_insights_2016_detail import EventInsights2016Detail
from .models.event_insights_2017 import EventInsights2017
from .models.event_insights_2017_detail import EventInsights2017Detail
from .models.event_op_rs import EventOPRs
from .models.event_predictions import EventPredictions
from .models.event_ranking import EventRanking
from .models.event_ranking_extra_stats_info import EventRankingExtraStatsInfo
from .models.event_ranking_rankings import EventRankingRankings
from .models.event_ranking_sort_order_info import EventRankingSortOrderInfo
from .models.event_simple import EventSimple
from .models.match import Match
from .models.match_alliance import MatchAlliance
from .models.match_score_breakdown_2015 import MatchScoreBreakdown2015
from .models.match_score_breakdown_2015_alliance import MatchScoreBreakdown2015Alliance
from .models.match_score_breakdown_2016 import MatchScoreBreakdown2016
from .models.match_score_breakdown_2016_alliance import MatchScoreBreakdown2016Alliance
from .models.match_score_breakdown_2017 import MatchScoreBreakdown2017
from .models.match_score_breakdown_2017_alliance import MatchScoreBreakdown2017Alliance
from .models.match_simple import MatchSimple
from .models.match_simple_alliances import MatchSimpleAlliances
from .models.match_videos import MatchVideos
from .models.media import Media
from .models.team import Team
from .models.team_event_status import TeamEventStatus
from .models.team_event_status_alliance import TeamEventStatusAlliance
from .models.team_event_status_alliance_backup import TeamEventStatusAllianceBackup
from .models.team_event_status_playoff import TeamEventStatusPlayoff
from .models.team_event_status_rank import TeamEventStatusRank
from .models.team_event_status_rank_ranking import TeamEventStatusRankRanking
from .models.team_event_status_rank_sort_order_info import TeamEventStatusRankSortOrderInfo
from .models.team_robot import TeamRobot
from .models.team_simple import TeamSimple
from .models.wlt_record import WLTRecord
from .models.webcast import Webcast

# import apis into sdk package
from .apis.district_api import DistrictApi
from .apis.event_api import EventApi
from .apis.list_api import ListApi
from .apis.match_api import MatchApi
from .apis.tba_api import TBAApi
from .apis.team_api import TeamApi

# import ApiClient
from .api_client import ApiClient

from .configuration import Configuration

configuration = Configuration()
