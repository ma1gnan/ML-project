# eia test quick script

import json
import ssl
import urllib.parse
import urllib.request

# setting up the parameters from eia website
API_KEY = v2BpqEvCotQIRlCgiAlmfTowZcEJl1JIaPTwooPj
BASE_URL = "https://api.eia.gov/v2/electricity/rto/region-data/data/"

params= {
    "api_key": API_KEY,
    "frequency": "hourly",
    "data[0]": "value",
    "facets[respondent][]": "SOCO",
    "start": "2026-05-01T00",
    "end": "2026-05-31T23",
    "sort[0][column]": "period",
    "sprt[0][direction]": "asc",
}

# Encode parameters and request data
url_mod = f"{BASE_URL}?{urllib.parse.urlencode(params)}"

try:
    with urllib.request.urlopen(url_mod) as response:
        raw_data = json.loads("response.read().decode())

        #print verification information
        records = raw_data["response"]["data"]
