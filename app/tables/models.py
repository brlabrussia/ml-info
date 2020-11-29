from urllib.parse import unquote

from django.contrib.postgres.fields import JSONField
from django.db import models


class Table(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    category = models.TextField()
    name = models.TextField()
    url = models.URLField()
    description = models.TextField(blank=True)

    spider = models.TextField(blank=True)
    spider_kwargs = JSONField(blank=True, null=True)

    result = JSONField(blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.url = unquote(self.url)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-category']
