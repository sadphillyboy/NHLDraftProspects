import requests
import json

nhl_api_request = requests.get("https://statsapi.web.nhl.com/api/v1/draft/prospects/")

prospect_details = nhl_api_request.text

prospect_data = json.loads(prospect_details)

all_prospects = prospect_data['prospects']

# all_prospects is a list that i need to iterate through
# i will create a variable called prospect_details which will be the dict
for prospect_details in all_prospects:
    try:
        prospect_name = prospect_details['fullName']
        position_details = prospect_details['primaryPosition']
        prospect_position = position_details['name']
        prospect_birth_country = prospect_details['birthCountry']
    except:
        print("No Data")
    else:
        print(prospect_name,prospect_position,prospect_birth_country)



# within prospect_details I will grab 'fullName', 'birthCity', 'birthStateProvince', 'birthCountry'
# 'birthCity', 'birthStateProvince', 'birthCountry' might not be listed within each entry
# 'fullName' will be prospect_name
# 'birthCity' will be prospect_birth_city
# 'birthStateProvince' will be prospect_birth_state_province
# 'birthCountry' will be prospect_birth_country
# i need to get into 'primaryPosition' dict and call out 'name'
# 'name' will be 'prospect_position'
# i will then print out