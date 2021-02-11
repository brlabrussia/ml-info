from banks import models
from scrapy_djangoitem import DjangoItem


class RatingItem(DjangoItem):
    django_model = models.Rating
