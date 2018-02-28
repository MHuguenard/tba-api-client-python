# tba-api-v3client
# Overview    Information and statistics about FIRST Robotics Competition teams and events.   # Authentication   All endpoints require an Auth Key to be passed in the header `X-TBA-Auth-Key`. If you do not have an auth key yet, you can obtain one from your [Account Page](/account).    A `User-Agent` header may need to be set to prevent a 403 Unauthorized error.

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 3.02.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import net.thefletcher.tbaapi.v3client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import net.thefletcher.tbaapi.v3client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import net.thefletcher.tbaapi.v3client
from net.thefletcher.tbaapi.v3client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
net.thefletcher.tbaapi.v3client.configuration.api_key['X-TBA-Auth-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# net.thefletcher.tbaapi.v3client.configuration.api_key_prefix['X-TBA-Auth-Key'] = 'Bearer'
# create an instance of the API class
api_instance = net.thefletcher.tbaapi.v3client.DistrictApi()
district_key = 'district_key_example' # str | TBA District Key, eg `2016fim`
if_modified_since = 'if_modified_since_example' # str | Value of the `Last-Modified` header in the most recently cached response by the client. (optional)

try:
    api_response = api_instance.get_district_events(district_key, if_modified_since=if_modified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DistrictApi->get_district_events: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://www.thebluealliance.com/api/v3*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DistrictApi* | [**get_district_events**](docs/DistrictApi.md#get_district_events) | **GET** /district/{district_key}/events | 
*DistrictApi* | [**get_district_events_keys**](docs/DistrictApi.md#get_district_events_keys) | **GET** /district/{district_key}/events/keys | 
*DistrictApi* | [**get_district_events_simple**](docs/DistrictApi.md#get_district_events_simple) | **GET** /district/{district_key}/events/simple | 
*DistrictApi* | [**get_district_rankings**](docs/DistrictApi.md#get_district_rankings) | **GET** /district/{district_key}/rankings | 
*DistrictApi* | [**get_district_teams**](docs/DistrictApi.md#get_district_teams) | **GET** /district/{district_key}/teams | 
*DistrictApi* | [**get_district_teams_keys**](docs/DistrictApi.md#get_district_teams_keys) | **GET** /district/{district_key}/teams/keys | 
*DistrictApi* | [**get_district_teams_simple**](docs/DistrictApi.md#get_district_teams_simple) | **GET** /district/{district_key}/teams/simple | 
*DistrictApi* | [**get_districts_by_year**](docs/DistrictApi.md#get_districts_by_year) | **GET** /districts/{year} | 
*DistrictApi* | [**get_event_district_points**](docs/DistrictApi.md#get_event_district_points) | **GET** /event/{event_key}/district_points | 
*DistrictApi* | [**get_team_districts**](docs/DistrictApi.md#get_team_districts) | **GET** /team/{team_key}/districts | 
*EventApi* | [**get_district_events**](docs/EventApi.md#get_district_events) | **GET** /district/{district_key}/events | 
*EventApi* | [**get_district_events_keys**](docs/EventApi.md#get_district_events_keys) | **GET** /district/{district_key}/events/keys | 
*EventApi* | [**get_district_events_simple**](docs/EventApi.md#get_district_events_simple) | **GET** /district/{district_key}/events/simple | 
*EventApi* | [**get_event**](docs/EventApi.md#get_event) | **GET** /event/{event_key} | 
*EventApi* | [**get_event_alliances**](docs/EventApi.md#get_event_alliances) | **GET** /event/{event_key}/alliances | 
*EventApi* | [**get_event_awards**](docs/EventApi.md#get_event_awards) | **GET** /event/{event_key}/awards | 
*EventApi* | [**get_event_district_points**](docs/EventApi.md#get_event_district_points) | **GET** /event/{event_key}/district_points | 
*EventApi* | [**get_event_insights**](docs/EventApi.md#get_event_insights) | **GET** /event/{event_key}/insights | 
*EventApi* | [**get_event_matches**](docs/EventApi.md#get_event_matches) | **GET** /event/{event_key}/matches | 
*EventApi* | [**get_event_matches_keys**](docs/EventApi.md#get_event_matches_keys) | **GET** /event/{event_key}/matches/keys | 
*EventApi* | [**get_event_matches_simple**](docs/EventApi.md#get_event_matches_simple) | **GET** /event/{event_key}/matches/simple | 
*EventApi* | [**get_event_op_rs**](docs/EventApi.md#get_event_op_rs) | **GET** /event/{event_key}/oprs | 
*EventApi* | [**get_event_predictions**](docs/EventApi.md#get_event_predictions) | **GET** /event/{event_key}/predictions | 
*EventApi* | [**get_event_rankings**](docs/EventApi.md#get_event_rankings) | **GET** /event/{event_key}/rankings | 
*EventApi* | [**get_event_simple**](docs/EventApi.md#get_event_simple) | **GET** /event/{event_key}/simple | 
*EventApi* | [**get_event_teams**](docs/EventApi.md#get_event_teams) | **GET** /event/{event_key}/teams | 
*EventApi* | [**get_event_teams_keys**](docs/EventApi.md#get_event_teams_keys) | **GET** /event/{event_key}/teams/keys | 
*EventApi* | [**get_event_teams_simple**](docs/EventApi.md#get_event_teams_simple) | **GET** /event/{event_key}/teams/simple | 
*EventApi* | [**get_event_teams_statuses**](docs/EventApi.md#get_event_teams_statuses) | **GET** /event/{event_key}/teams/statuses | 
*EventApi* | [**get_events_by_year**](docs/EventApi.md#get_events_by_year) | **GET** /events/{year} | 
*EventApi* | [**get_events_by_year_keys**](docs/EventApi.md#get_events_by_year_keys) | **GET** /events/{year}/keys | 
*EventApi* | [**get_events_by_year_simple**](docs/EventApi.md#get_events_by_year_simple) | **GET** /events/{year}/simple | 
*EventApi* | [**get_team_event_awards**](docs/EventApi.md#get_team_event_awards) | **GET** /team/{team_key}/event/{event_key}/awards | 
*EventApi* | [**get_team_event_matches**](docs/EventApi.md#get_team_event_matches) | **GET** /team/{team_key}/event/{event_key}/matches | 
*EventApi* | [**get_team_event_matches_keys**](docs/EventApi.md#get_team_event_matches_keys) | **GET** /team/{team_key}/event/{event_key}/matches/keys | 
*EventApi* | [**get_team_event_matches_simple**](docs/EventApi.md#get_team_event_matches_simple) | **GET** /team/{team_key}/event/{event_key}/matches/simple | 
*EventApi* | [**get_team_event_status**](docs/EventApi.md#get_team_event_status) | **GET** /team/{team_key}/event/{event_key}/status | 
*EventApi* | [**get_team_events**](docs/EventApi.md#get_team_events) | **GET** /team/{team_key}/events | 
*EventApi* | [**get_team_events_by_year**](docs/EventApi.md#get_team_events_by_year) | **GET** /team/{team_key}/events/{year} | 
*EventApi* | [**get_team_events_by_year_keys**](docs/EventApi.md#get_team_events_by_year_keys) | **GET** /team/{team_key}/events/{year}/keys | 
*EventApi* | [**get_team_events_by_year_simple**](docs/EventApi.md#get_team_events_by_year_simple) | **GET** /team/{team_key}/events/{year}/simple | 
*EventApi* | [**get_team_events_keys**](docs/EventApi.md#get_team_events_keys) | **GET** /team/{team_key}/events/keys | 
*EventApi* | [**get_team_events_simple**](docs/EventApi.md#get_team_events_simple) | **GET** /team/{team_key}/events/simple | 
*EventApi* | [**get_team_events_statuses_by_year**](docs/EventApi.md#get_team_events_statuses_by_year) | **GET** /team/{team_key}/events/{year}/statuses | 
*ListApi* | [**get_district_events**](docs/ListApi.md#get_district_events) | **GET** /district/{district_key}/events | 
*ListApi* | [**get_district_events_keys**](docs/ListApi.md#get_district_events_keys) | **GET** /district/{district_key}/events/keys | 
*ListApi* | [**get_district_events_simple**](docs/ListApi.md#get_district_events_simple) | **GET** /district/{district_key}/events/simple | 
*ListApi* | [**get_district_rankings**](docs/ListApi.md#get_district_rankings) | **GET** /district/{district_key}/rankings | 
*ListApi* | [**get_district_teams**](docs/ListApi.md#get_district_teams) | **GET** /district/{district_key}/teams | 
*ListApi* | [**get_district_teams_keys**](docs/ListApi.md#get_district_teams_keys) | **GET** /district/{district_key}/teams/keys | 
*ListApi* | [**get_district_teams_simple**](docs/ListApi.md#get_district_teams_simple) | **GET** /district/{district_key}/teams/simple | 
*ListApi* | [**get_event_teams**](docs/ListApi.md#get_event_teams) | **GET** /event/{event_key}/teams | 
*ListApi* | [**get_event_teams_keys**](docs/ListApi.md#get_event_teams_keys) | **GET** /event/{event_key}/teams/keys | 
*ListApi* | [**get_event_teams_simple**](docs/ListApi.md#get_event_teams_simple) | **GET** /event/{event_key}/teams/simple | 
*ListApi* | [**get_event_teams_statuses**](docs/ListApi.md#get_event_teams_statuses) | **GET** /event/{event_key}/teams/statuses | 
*ListApi* | [**get_events_by_year**](docs/ListApi.md#get_events_by_year) | **GET** /events/{year} | 
*ListApi* | [**get_events_by_year_keys**](docs/ListApi.md#get_events_by_year_keys) | **GET** /events/{year}/keys | 
*ListApi* | [**get_events_by_year_simple**](docs/ListApi.md#get_events_by_year_simple) | **GET** /events/{year}/simple | 
*ListApi* | [**get_team_events_statuses_by_year**](docs/ListApi.md#get_team_events_statuses_by_year) | **GET** /team/{team_key}/events/{year}/statuses | 
*ListApi* | [**get_teams**](docs/ListApi.md#get_teams) | **GET** /teams/{page_num} | 
*ListApi* | [**get_teams_by_year**](docs/ListApi.md#get_teams_by_year) | **GET** /teams/{year}/{page_num} | 
*ListApi* | [**get_teams_by_year_keys**](docs/ListApi.md#get_teams_by_year_keys) | **GET** /teams/{year}/{page_num}/keys | 
*ListApi* | [**get_teams_by_year_simple**](docs/ListApi.md#get_teams_by_year_simple) | **GET** /teams/{year}/{page_num}/simple | 
*ListApi* | [**get_teams_keys**](docs/ListApi.md#get_teams_keys) | **GET** /teams/{page_num}/keys | 
*ListApi* | [**get_teams_simple**](docs/ListApi.md#get_teams_simple) | **GET** /teams/{page_num}/simple | 
*MatchApi* | [**get_event_matches**](docs/MatchApi.md#get_event_matches) | **GET** /event/{event_key}/matches | 
*MatchApi* | [**get_event_matches_keys**](docs/MatchApi.md#get_event_matches_keys) | **GET** /event/{event_key}/matches/keys | 
*MatchApi* | [**get_event_matches_simple**](docs/MatchApi.md#get_event_matches_simple) | **GET** /event/{event_key}/matches/simple | 
*MatchApi* | [**get_match**](docs/MatchApi.md#get_match) | **GET** /match/{match_key} | 
*MatchApi* | [**get_match_simple**](docs/MatchApi.md#get_match_simple) | **GET** /match/{match_key}/simple | 
*MatchApi* | [**get_team_event_matches**](docs/MatchApi.md#get_team_event_matches) | **GET** /team/{team_key}/event/{event_key}/matches | 
*MatchApi* | [**get_team_event_matches_keys**](docs/MatchApi.md#get_team_event_matches_keys) | **GET** /team/{team_key}/event/{event_key}/matches/keys | 
*MatchApi* | [**get_team_event_matches_simple**](docs/MatchApi.md#get_team_event_matches_simple) | **GET** /team/{team_key}/event/{event_key}/matches/simple | 
*MatchApi* | [**get_team_matches_by_year**](docs/MatchApi.md#get_team_matches_by_year) | **GET** /team/{team_key}/matches/{year} | 
*MatchApi* | [**get_team_matches_by_year_keys**](docs/MatchApi.md#get_team_matches_by_year_keys) | **GET** /team/{team_key}/matches/{year}/keys | 
*MatchApi* | [**get_team_matches_by_year_simple**](docs/MatchApi.md#get_team_matches_by_year_simple) | **GET** /team/{team_key}/matches/{year}/simple | 
*TBAApi* | [**get_status**](docs/TBAApi.md#get_status) | **GET** /status | 
*TeamApi* | [**get_district_rankings**](docs/TeamApi.md#get_district_rankings) | **GET** /district/{district_key}/rankings | 
*TeamApi* | [**get_district_teams**](docs/TeamApi.md#get_district_teams) | **GET** /district/{district_key}/teams | 
*TeamApi* | [**get_district_teams_keys**](docs/TeamApi.md#get_district_teams_keys) | **GET** /district/{district_key}/teams/keys | 
*TeamApi* | [**get_district_teams_simple**](docs/TeamApi.md#get_district_teams_simple) | **GET** /district/{district_key}/teams/simple | 
*TeamApi* | [**get_event_teams**](docs/TeamApi.md#get_event_teams) | **GET** /event/{event_key}/teams | 
*TeamApi* | [**get_event_teams_keys**](docs/TeamApi.md#get_event_teams_keys) | **GET** /event/{event_key}/teams/keys | 
*TeamApi* | [**get_event_teams_simple**](docs/TeamApi.md#get_event_teams_simple) | **GET** /event/{event_key}/teams/simple | 
*TeamApi* | [**get_event_teams_statuses**](docs/TeamApi.md#get_event_teams_statuses) | **GET** /event/{event_key}/teams/statuses | 
*TeamApi* | [**get_team**](docs/TeamApi.md#get_team) | **GET** /team/{team_key} | 
*TeamApi* | [**get_team_awards**](docs/TeamApi.md#get_team_awards) | **GET** /team/{team_key}/awards | 
*TeamApi* | [**get_team_awards_by_year**](docs/TeamApi.md#get_team_awards_by_year) | **GET** /team/{team_key}/awards/{year} | 
*TeamApi* | [**get_team_districts**](docs/TeamApi.md#get_team_districts) | **GET** /team/{team_key}/districts | 
*TeamApi* | [**get_team_event_awards**](docs/TeamApi.md#get_team_event_awards) | **GET** /team/{team_key}/event/{event_key}/awards | 
*TeamApi* | [**get_team_event_matches**](docs/TeamApi.md#get_team_event_matches) | **GET** /team/{team_key}/event/{event_key}/matches | 
*TeamApi* | [**get_team_event_matches_keys**](docs/TeamApi.md#get_team_event_matches_keys) | **GET** /team/{team_key}/event/{event_key}/matches/keys | 
*TeamApi* | [**get_team_event_matches_simple**](docs/TeamApi.md#get_team_event_matches_simple) | **GET** /team/{team_key}/event/{event_key}/matches/simple | 
*TeamApi* | [**get_team_event_status**](docs/TeamApi.md#get_team_event_status) | **GET** /team/{team_key}/event/{event_key}/status | 
*TeamApi* | [**get_team_events**](docs/TeamApi.md#get_team_events) | **GET** /team/{team_key}/events | 
*TeamApi* | [**get_team_events_by_year**](docs/TeamApi.md#get_team_events_by_year) | **GET** /team/{team_key}/events/{year} | 
*TeamApi* | [**get_team_events_by_year_keys**](docs/TeamApi.md#get_team_events_by_year_keys) | **GET** /team/{team_key}/events/{year}/keys | 
*TeamApi* | [**get_team_events_by_year_simple**](docs/TeamApi.md#get_team_events_by_year_simple) | **GET** /team/{team_key}/events/{year}/simple | 
*TeamApi* | [**get_team_events_keys**](docs/TeamApi.md#get_team_events_keys) | **GET** /team/{team_key}/events/keys | 
*TeamApi* | [**get_team_events_simple**](docs/TeamApi.md#get_team_events_simple) | **GET** /team/{team_key}/events/simple | 
*TeamApi* | [**get_team_events_statuses_by_year**](docs/TeamApi.md#get_team_events_statuses_by_year) | **GET** /team/{team_key}/events/{year}/statuses | 
*TeamApi* | [**get_team_matches_by_year**](docs/TeamApi.md#get_team_matches_by_year) | **GET** /team/{team_key}/matches/{year} | 
*TeamApi* | [**get_team_matches_by_year_keys**](docs/TeamApi.md#get_team_matches_by_year_keys) | **GET** /team/{team_key}/matches/{year}/keys | 
*TeamApi* | [**get_team_matches_by_year_simple**](docs/TeamApi.md#get_team_matches_by_year_simple) | **GET** /team/{team_key}/matches/{year}/simple | 
*TeamApi* | [**get_team_media_by_tag**](docs/TeamApi.md#get_team_media_by_tag) | **GET** /team/{team_key}/media/tag/{media_tag} | 
*TeamApi* | [**get_team_media_by_tag_year**](docs/TeamApi.md#get_team_media_by_tag_year) | **GET** /team/{team_key}/media/tag/{media_tag}/{year} | 
*TeamApi* | [**get_team_media_by_year**](docs/TeamApi.md#get_team_media_by_year) | **GET** /team/{team_key}/media/{year} | 
*TeamApi* | [**get_team_robots**](docs/TeamApi.md#get_team_robots) | **GET** /team/{team_key}/robots | 
*TeamApi* | [**get_team_simple**](docs/TeamApi.md#get_team_simple) | **GET** /team/{team_key}/simple | 
*TeamApi* | [**get_team_social_media**](docs/TeamApi.md#get_team_social_media) | **GET** /team/{team_key}/social_media | 
*TeamApi* | [**get_team_years_participated**](docs/TeamApi.md#get_team_years_participated) | **GET** /team/{team_key}/years_participated | 
*TeamApi* | [**get_teams**](docs/TeamApi.md#get_teams) | **GET** /teams/{page_num} | 
*TeamApi* | [**get_teams_by_year**](docs/TeamApi.md#get_teams_by_year) | **GET** /teams/{year}/{page_num} | 
*TeamApi* | [**get_teams_by_year_keys**](docs/TeamApi.md#get_teams_by_year_keys) | **GET** /teams/{year}/{page_num}/keys | 
*TeamApi* | [**get_teams_by_year_simple**](docs/TeamApi.md#get_teams_by_year_simple) | **GET** /teams/{year}/{page_num}/simple | 
*TeamApi* | [**get_teams_keys**](docs/TeamApi.md#get_teams_keys) | **GET** /teams/{page_num}/keys | 
*TeamApi* | [**get_teams_simple**](docs/TeamApi.md#get_teams_simple) | **GET** /teams/{page_num}/simple | 


## Documentation For Models

 - [APIStatus](docs/APIStatus.md)
 - [APIStatusAppVersion](docs/APIStatusAppVersion.md)
 - [Award](docs/Award.md)
 - [AwardRecipient](docs/AwardRecipient.md)
 - [DistrictList](docs/DistrictList.md)
 - [DistrictRanking](docs/DistrictRanking.md)
 - [DistrictRankingEventPoints](docs/DistrictRankingEventPoints.md)
 - [EliminationAlliance](docs/EliminationAlliance.md)
 - [EliminationAllianceBackup](docs/EliminationAllianceBackup.md)
 - [EliminationAllianceStatus](docs/EliminationAllianceStatus.md)
 - [Event](docs/Event.md)
 - [EventDistrictPoints](docs/EventDistrictPoints.md)
 - [EventDistrictPointsPoints](docs/EventDistrictPointsPoints.md)
 - [EventDistrictPointsTiebreakers](docs/EventDistrictPointsTiebreakers.md)
 - [EventInsights2016](docs/EventInsights2016.md)
 - [EventInsights2016Detail](docs/EventInsights2016Detail.md)
 - [EventInsights2017](docs/EventInsights2017.md)
 - [EventInsights2017Detail](docs/EventInsights2017Detail.md)
 - [EventOPRs](docs/EventOPRs.md)
 - [EventPredictions](docs/EventPredictions.md)
 - [EventRanking](docs/EventRanking.md)
 - [EventRankingExtraStatsInfo](docs/EventRankingExtraStatsInfo.md)
 - [EventRankingRankings](docs/EventRankingRankings.md)
 - [EventRankingSortOrderInfo](docs/EventRankingSortOrderInfo.md)
 - [EventSimple](docs/EventSimple.md)
 - [Match](docs/Match.md)
 - [MatchAlliance](docs/MatchAlliance.md)
 - [MatchScoreBreakdown2015](docs/MatchScoreBreakdown2015.md)
 - [MatchScoreBreakdown2015Alliance](docs/MatchScoreBreakdown2015Alliance.md)
 - [MatchScoreBreakdown2016](docs/MatchScoreBreakdown2016.md)
 - [MatchScoreBreakdown2016Alliance](docs/MatchScoreBreakdown2016Alliance.md)
 - [MatchScoreBreakdown2017](docs/MatchScoreBreakdown2017.md)
 - [MatchScoreBreakdown2017Alliance](docs/MatchScoreBreakdown2017Alliance.md)
 - [MatchScoreBreakdown2018](docs/MatchScoreBreakdown2018.md)
 - [MatchScoreBreakdown2018Alliance](docs/MatchScoreBreakdown2018Alliance.md)
 - [MatchSimple](docs/MatchSimple.md)
 - [MatchSimpleAlliances](docs/MatchSimpleAlliances.md)
 - [MatchVideos](docs/MatchVideos.md)
 - [Media](docs/Media.md)
 - [Team](docs/Team.md)
 - [TeamEventStatus](docs/TeamEventStatus.md)
 - [TeamEventStatusAlliance](docs/TeamEventStatusAlliance.md)
 - [TeamEventStatusAllianceBackup](docs/TeamEventStatusAllianceBackup.md)
 - [TeamEventStatusPlayoff](docs/TeamEventStatusPlayoff.md)
 - [TeamEventStatusRank](docs/TeamEventStatusRank.md)
 - [TeamEventStatusRankRanking](docs/TeamEventStatusRankRanking.md)
 - [TeamEventStatusRankSortOrderInfo](docs/TeamEventStatusRankSortOrderInfo.md)
 - [TeamRobot](docs/TeamRobot.md)
 - [TeamSimple](docs/TeamSimple.md)
 - [WLTRecord](docs/WLTRecord.md)
 - [Webcast](docs/Webcast.md)


## Documentation For Authorization


## apiKey

- **Type**: API key
- **API key parameter name**: X-TBA-Auth-Key
- **Location**: HTTP header


## Author



