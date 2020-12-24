from insurance.models import Company
from scrapy_djangoitem import DjangoItem


class CompanyItem(DjangoItem):
    django_model = Company
