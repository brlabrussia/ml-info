from django.db import models


class Company(models.Model):
    cbrn = models.CharField(max_length=4)
    ogrn = models.CharField(max_length=13, blank=True)
    inn = models.CharField(max_length=10, blank=True)
    trademark = models.CharField(max_length=200, blank=True)
    name = models.CharField(max_length=200, blank=True)
    logo = models.URLField(blank=True)
    address = models.CharField(max_length=200, blank=True)
    federal_subject = models.CharField(max_length=200, blank=True)
    contacts = models.TextField(blank=True)
    licenses = models.JSONField(blank=True, null=True)
    authorized_capital = models.PositiveIntegerField(blank=True, null=True)
    net_profit = models.PositiveIntegerField(blank=True, null=True)
    premiums = models.PositiveIntegerField(blank=True, null=True)
    payouts = models.PositiveIntegerField(blank=True, null=True)
    director = models.CharField(max_length=200, blank=True)
    director_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.trademark or self.name
