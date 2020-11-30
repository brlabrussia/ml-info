import os

import requests
from django.urls import reverse

from core.celery import app
from tables.models import Table

SCRAPY_PROJECT = 'tables'
SCRAPY_HOST = os.getenv('SCRAPY_HOST_TABLES')
SCRAPY_ENDPOINT = 'https://' + SCRAPY_HOST + '/schedule.json'
SCRAPY_LOGIN = os.getenv('SCRAPY_LOGIN_TABLES')
SCRAPY_PASS = os.getenv('SCRAPY_PASS_TABLES')

VIRTUAL_HOST = os.getenv('VIRTUAL_HOST')
if SCRAPY_HOST == 'scrapy:6800':
    VIRTUAL_HOST = 'nginx'


@app.task(ignore_result=True)
def schedule_spider(pk: int, spider: str, spider_kwargs: dict):
    path = reverse('table-detail', args=[pk])
    webhook_endpoint = 'https://' + VIRTUAL_HOST + path
    data = [
        ('project', SCRAPY_PROJECT),
        ('setting', f'WEBHOOK_ENDPOINT={webhook_endpoint}'),
        ('spider', spider),
    ]
    if spider_kwargs is not None:
        data.extend([*spider_kwargs.items()])
    requests.post(
        SCRAPY_ENDPOINT,
        auth=(SCRAPY_LOGIN, SCRAPY_PASS),
        data=data,
    )


@app.task(ignore_result=True)
def schedule_spiders():
    tables = Table.objects.filter(spider__isnull=False)
    for table in tables:
        schedule_spider.delay(
            table.pk,
            table.spider,
            table.spider_kwargs,
        )
