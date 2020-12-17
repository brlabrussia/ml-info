from investments.models import Share
from scrapy_djangoitem import DjangoItem


class ShareItem(DjangoItem):
    django_model = Share
