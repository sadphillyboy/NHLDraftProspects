import requests
import json

nhl_api_request = requests.get("https://statsapi.web.nhl.com/api/v1/draft")

draft_details = nhl_api_request.text

data = json.loads(draft_details)

drafts = data['drafts']

draft_year = drafts[0]

rounds = draft_year['rounds']

# I need to loop through rounds which is a list
# the variable for each round is rnd which will be a dictionary
for rnd in rounds:
    pick_round = rnd['round']
# in each rnd I need the 'picks' which I will call draft_picks which will be a list
# I need each draftee in draft_picks
    draft_picks = rnd['picks']
    for draftee in draft_picks:
        pick_year = draftee['year']
        
        pick_team = draftee['team']
        pick_team_name = pick_team['name']
        
        pick_details = draftee['prospect']
        pick_stat_name = pick_details['fullName']
        pick_stat_link = pick_details['link']
        
        print(pick_year, pick_round, pick_stat_name, pick_team_name)
        
# I will grab 'year'(int), 'pickinround'(int), 'team'(dict), 'prospect'(dict) from draft_picks
# I will call 'year' as pick_year, 'pickinround' as pick_round, 'team' as pick_team, 'prospect' as pick_details
# I will then call out 'name' in 'team as pick_team_name
# I will then call out 'fullName' and 'link' in 'prospect as as pick_stat_fullName and pick_stat_link
# i would then like to print year, round, fullname, team, and link on one line