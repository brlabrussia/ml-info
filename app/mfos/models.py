from django.contrib.postgres.fields import ArrayField
from django.db import models


class MFO(models.Model):
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    scraped_from = ArrayField(models.URLField())

    trademark = models.TextField(blank=True)
    name = models.TextField(blank=True)
    full_name = models.TextField(blank=True)
    # logo = models.ImageField()  # TODO upload_to='images/', add pillow

    is_legal = models.BooleanField(default=False)
    type = models.TextField(blank=True)
    regdate = models.DateTimeField('date entry added to cbr register', blank=True, null=True)
    regnum = models.IntegerField('number in cbr register', unique=True, null=True)
    ogrn = models.IntegerField(unique=True, null=True)
    inn = models.IntegerField(unique=True, null=True)

    website = models.URLField(blank=True)  # both blank and null?
    email = models.EmailField(blank=True)
    socials = ArrayField(models.URLField(), null=True)
    address = models.TextField(blank=True)
    head_name = models.TextField(blank=True)

    money_value_min = models.IntegerField()
    money_value_max = models.IntegerField()
    overpayment_day = models.IntegerField()
    overpayment_full = models.IntegerField()
    refusal_reasons = ArrayField(models.TextField())


class Document(models.Model):
    mfo = models.ForeignKey(MFO, on_delete=models.CASCADE)
    name = models.TextField()
    file = models.FileField()


# WIP
class Loan(models.Model):
    address = models.TextField()
    borrowers_age = models.TextField()
    borrowers_categories = ArrayField(models.TextField())
    borrowers_documents = ArrayField(models.TextField())
    borrowers_registration = ArrayField(models.TextField())
    dates_from = models.IntegerField()
    dates_to = models.IntegerField()
    first_loan_condition = models.TextField()
    head_name = models.TextField()
    issuance = models.TextField()
    loan_form = ArrayField(models.TextField())
    loan_form_description = models.TextField()
    loan_processing = ArrayField(models.TextField())
    loan_providing = ArrayField(models.TextField())
    loan_purpose = ArrayField(models.TextField())
    loan_time_terms = models.TextField()
    # logo = models.ImageField()  # TODO upload_to arg
    max_money_value = models.TextField()
    mfo = models.ForeignKey(MFO, on_delete=models.CASCADE)
    name = models.TextField()
    ogrn = models.TextField()
    payment_methods = ArrayField(models.TextField())
    rate = models.TextField()
    repayment_order = ArrayField(models.TextField())
    repayment_order_description = models.TextField()
    trademark = models.TextField()
    last_modified = models.DateTimeField('last updated on source')
    url = models.URLField('first scraped from', unique=True)
