import json
import os

import requests

from core.celery import app
from tables.models import Table

SCRAPYD_URL = os.getenv('SCRAPYD_URL')
SCRAPYD_LOGIN = os.getenv('SCRAPYD_LOGIN')
SCRAPYD_PASS = os.getenv('SCRAPYD_PASS')


@app.task(ignore_result=True)
def schedule_scrapers():
    project = 'tables'
    webhook = f'https://{os.getenv("VIRTUAL_HOST")}/tables/scrapers/'
    tables = Table.objects.filter(driver__isnull=False)
    for table in tables:
        spider = table.driver.scraper
        args = [table.pk, table.url, *table.driver_args]
        data = [
            ('project', project),
            ('spider', spider),
            ('request_args', json.dumps(args)),
            ('setting', f'WEBHOOK_ENDPOINT={webhook}'),
        ]
        requests.post(
            f'{SCRAPYD_URL}/schedule.json',
            data=data,
            auth=(SCRAPYD_LOGIN, SCRAPYD_PASS),
        )
