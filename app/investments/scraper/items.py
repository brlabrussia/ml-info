from investments.models import Bond, Share
from scrapy_djangoitem import DjangoItem


class ShareItem(DjangoItem):
    django_model = Share


class BondItem(DjangoItem):
    django_model = Bond
