# eia test quick script

import json
import urllib.parse
import urllib.request

# setting up the parameters from eia website
API_KEY = v2BpqEvCotQIRlCgiAlmfTowZcEJl1JIaPTwooPj
BASE_URL = https://api.eia.gov/v2/electricity/rto/region-data/data/?frequency=hourly&data[0]=value&start=2019-01-01T00&end=2026-07-10T00&sort[0][column]=period&sort[0][direction]=desc&offset=0&length=5000

X-Params: {
    "frequency": "hourly",
    "data": [
        "value"
    ],
    "facets": {},
    "start": "2019-01-01T00",
    "end": "2026-07-10T00",
    "sort": [
        {
            "column": "period",
            "direction": "desc"
        }
    ],
    "offset": 0,
    "length": 5000
}
