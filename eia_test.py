# eia test quick script

import json
import ssl
import urllib.parse
import urllib.request

# setting up the parameters from eia website
API_KEY = v2BpqEvCotQIRlCgiAlmfTowZcEJl1JIaPTwooPj # my API Key
BASE_URL = "https://api.eia.gov/v2/electricity/rto/region-data/data/"

params= { # creating dictionary
    "api_key": API_KEY, # Sends API key for authentication
    "frequency": "hourly", # request hourly data
    "data[0]": "value", # request value field from API
    "facets[respondent][]": "SOCO", # filter data so only SOCO (Southern Company) are returned 
    "start": "2026-05-01T00", # start date and time are 1 May 2026 12:00 AM
    "end": "2026-05-31T23", # end date and time 31 May 2026 11:00 PM
    # Total time 31 days X 24 hours = 744 hours return value
    "sort[0][column]": "period", # sort order by timestamp
    "sprt[0][direction]": "asc", # sort in ascending order
}

# Encode parameters and request data
url_mod = f"{BASE_URL}?{urllib.parse.urlencode(params)}"

try:
    with urllib.request.urlopen(url_mod) as response:
        raw_data = json.loads(response.read().decode())

        # print verification information
        records = raw_data["response"]["data"]
        print(f"Success! Retrieved {len(records)} hourly data points.")

        # Print the first sample hour to inspect data format
        print("\n First data point sample:")
        print(json.dumos(records[0], indent=2))

except Exception as e:
    print(f"An error occurred: {e}")
