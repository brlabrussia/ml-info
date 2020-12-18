from urllib.parse import urljoin

import requests
from core.celery import app

SCRAPY_URL = 'http://scrapy:6800/'
SCRAPY_PROJECT = 'investments'


@app.task(ignore_result=True)
def schedule_spider(spider: str):
    requests.post(
        urljoin(SCRAPY_URL, 'schedule.json'),
        data={
            'project': SCRAPY_PROJECT,
            'spider': spider,
        },
    )


@app.task(ignore_result=True)
def schedule_spiders():
    response = requests.get(
        urljoin(SCRAPY_URL, 'listspiders.json'),
        params={
            'project': SCRAPY_PROJECT,
        },
    )
    for spider in response.json()['spiders']:
        schedule_spider.delay(spider)
