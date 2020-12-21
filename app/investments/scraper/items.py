from investments.models import IIA, Bond, Share
from scrapy_djangoitem import DjangoItem


class ShareItem(DjangoItem):
    django_model = Share


class BondItem(DjangoItem):
    django_model = Bond


class IIAItem(DjangoItem):
    django_model = IIA
