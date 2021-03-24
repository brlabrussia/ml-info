from casino import models
from scrapy_djangoitem import DjangoItem


class CasinoItem(DjangoItem):
    django_model = models.Casino


class SlotItem(DjangoItem):
    django_model = models.Slot
