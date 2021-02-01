from other.models import ItunesApp
from scrapy_djangoitem import DjangoItem


class ItunesAppItem(DjangoItem):
    django_model = ItunesApp
