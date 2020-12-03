import json
import os

import requests

from core.celery import app
from django.urls import reverse
from tables.models import Table

SCRAPY_PROJECT = 'tables'
SCRAPY_HOST = os.getenv('SCRAPY_HOST_TABLES')
SCRAPY_ENDPOINT = 'http://' + SCRAPY_HOST + '/schedule.json'
SCRAPY_LOGIN = os.getenv('SCRAPY_LOGIN_TABLES')
SCRAPY_PASS = os.getenv('SCRAPY_PASS_TABLES')

VIRTUAL_HOST = os.getenv('VIRTUAL_HOST')
if SCRAPY_HOST == 'scrapy:6800':
    VIRTUAL_HOST = 'nginx'


@app.task(ignore_result=True)
def schedule_spider(pk: int, url: str, spider: str, spider_kwargs: dict):
    path = reverse('table-detail', args=[pk])
    webhook_endpoint = 'http://' + VIRTUAL_HOST + path
    data = [
        ('project', SCRAPY_PROJECT),
        ('setting', f'WEBHOOK_ENDPOINT={webhook_endpoint}'),
        ('spider', spider),
        ('start_urls', json.dumps([url])),
        *spider_kwargs.items(),
    ]
    requests.post(
        SCRAPY_ENDPOINT,
        auth=(SCRAPY_LOGIN, SCRAPY_PASS),
        data=data,
    )


@app.task(ignore_result=True)
def schedule_spiders():
    tables = Table.objects.exclude(spider__exact='')
    for table in tables:
        schedule_spider.delay(
            table.pk,
            table.url,
            table.spider,
            table.spider_kwargs,
        )
