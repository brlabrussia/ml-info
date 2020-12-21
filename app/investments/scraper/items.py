from investments.models import IIA, Bond, Mutual, Share
from scrapy_djangoitem import DjangoItem


class ShareItem(DjangoItem):
    django_model = Share


class BondItem(DjangoItem):
    django_model = Bond


class IIAItem(DjangoItem):
    django_model = IIA


class MutualItem(DjangoItem):
    django_model = Mutual
