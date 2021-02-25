from banks import models
from scrapy_djangoitem import DjangoItem


class BankItem(DjangoItem):
    django_model = models.Bank


class DebitCardItem(DjangoItem):
    django_model = models.DebitCard


class CreditCardItem(DjangoItem):
    django_model = models.CreditCard


class AutoCreditItem(DjangoItem):
    django_model = models.AutoCredit


class ConsumerCreditItem(DjangoItem):
    django_model = models.ConsumerCredit


class DepositItem(DjangoItem):
    django_model = models.Deposit


class BranchItem(DjangoItem):
    django_model = models.Branch


class RatingItem(DjangoItem):
    django_model = models.Rating
