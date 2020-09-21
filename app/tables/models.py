from django.contrib.postgres.fields import ArrayField, JSONField
from django.db import models


class Driver(models.Model):
    name = models.TextField()
    description = models.TextField(blank=True)
    scraper = models.TextField()

    def __str__(self):
        return self.name


class Table(models.Model):
    category = models.TextField()
    name = models.TextField()
    url = models.URLField()
    description = models.TextField(blank=True)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name='tables', blank=True, null=True)
    driver_args = ArrayField(models.TextField(), blank=True, null=True)
    result = JSONField(blank=True, null=True)

    def __str__(self):
        return self.name
