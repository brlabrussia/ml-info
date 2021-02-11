from finance import models
from scrapy_djangoitem import DjangoItem


class PersonItem(DjangoItem):
    django_model = models.Person
