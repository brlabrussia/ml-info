import json
import os
from typing import List

import requests

from core.celery import app
from tables.models import Table

SCRAPYD_PROJECT = 'tables'
SCRAPYD_URL = os.getenv('SCRAPYD_URL')
SCRAPYD_LOGIN = os.getenv('SCRAPYD_LOGIN')
SCRAPYD_PASS = os.getenv('SCRAPYD_PASS')

VIRTUAL_HOST = (
    VIRTUAL_HOST
    if 'localhost' not in (VIRTUAL_HOST := os.getenv('VIRTUAL_HOST'))
    else 'nginx'
)
WEBHOOK_ENDPOINT = f'http://{VIRTUAL_HOST}/tables/scrapers/'


@app.task(ignore_result=True)
def schedule_scraper(spider: str, pk: int, url: str, driver_args: List[str]):
    spider = spider
    args = [pk, url, *driver_args]
    data = [
        ('project', SCRAPYD_PROJECT),
        ('spider', spider),
        ('request_args', json.dumps(args)),
        ('setting', f'WEBHOOK_ENDPOINT={WEBHOOK_ENDPOINT}'),
    ]
    requests.post(
        f'{SCRAPYD_URL}/schedule.json',
        data=data,
        auth=(SCRAPYD_LOGIN, SCRAPYD_PASS),
    )


@app.task(ignore_result=True)
def schedule_scrapers():
    tables = Table.objects.filter(driver__isnull=False)
    for table in tables:
        schedule_scraper.delay(
            table.driver.scraper,
            table.pk,
            table.url,
            table.driver_args,
        )
