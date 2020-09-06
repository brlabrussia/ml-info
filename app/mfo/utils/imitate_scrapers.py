import json
from pprint import pprint

import requests

scrapers = (
    'cbr',
    'zaymov',
    'vsezaimyonline',
    'banki',
)

for scraper in scrapers:
    path = f'app/mfo/utils/imitate_scrapers_input/{scraper}.json'
    with open(path) as f:
        r = requests.post(
            f'http://localhost:8080/mfo/scrapers/{scraper}/',
            json=json.load(f),
        )
        pprint(r.json())
