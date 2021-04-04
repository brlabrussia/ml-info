import requests
from celery import shared_task
from django.core.management import call_command

SCRAPY_URL = 'http://scrapy:6800'


@shared_task
def backup():
    call_command('dbbackup', '--clean')
    call_command('mediabackup', '--clean')


@shared_task
def schedule_spider(project, spider, spider_kwargs=None):
    if spider_kwargs is None:
        spider_kwargs = {}

    url = SCRAPY_URL + '/schedule.json'
    data = {
        'project': project,
        'spider': spider,
        **spider_kwargs,
    }
    requests.post(url, data=data)


@shared_task
def schedule_project(project, exclude_spiders=None, countdown_step=0):
    if exclude_spiders is None:
        exclude_spiders = []

    url = SCRAPY_URL + '/listspiders.json'
    params = {
        'project': project,
    }
    response = requests.get(url, params=params)

    countdown = 0
    for spider in response.json()['spiders']:
        if spider in exclude_spiders:
            continue
        schedule_spider.apply_async(
            (project, spider),
            countdown=countdown,
        )
        countdown += countdown_step
