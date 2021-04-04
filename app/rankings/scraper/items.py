from rankings import models
from scrapy_djangoitem import DjangoItem


class RankingItem(DjangoItem):
    django_model = models.Ranking
