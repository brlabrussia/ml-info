import json
from pprint import pprint

import requests

SCRAPERS = (
    'cbr',
    'zaymov',
    'vsezaimyonline',
    'banki',
)

for scraper in SCRAPERS:
    path = f'mfo/utils/imitate_scrapers_input/{scraper}.json'
    with open(path) as f:
        r = requests.post(
            f'http://localhost:8080/mfo/scrapers/{scraper}/',
            json=json.load(f),
            verify=False,
            timeout=None,
        )
        try:
            pprint(r.json())
        except Exception:
            print(r.text)
