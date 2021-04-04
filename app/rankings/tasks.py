from celery import shared_task
from common.tasks import schedule_spider

from rankings.models import Ranking

PROJECT = 'rankings'


@shared_task
def schedule_project():
    for ranking in Ranking.objects.exclude(spider__exact=''):
        spider_kwargs = ranking.spider_kwargs
        spider_kwargs['ranking_pk'] = ranking.pk
        spider_kwargs['ranking_url'] = ranking.url
        schedule_spider.delay(PROJECT, ranking.spider, spider_kwargs)
