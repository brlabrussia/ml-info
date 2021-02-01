from django.db import models


class ItunesApp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    url = models.URLField(blank=True)
    name = models.CharField(max_length=200, blank=True)
    subtitle = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    logo = models.URLField(max_length=500, blank=True)
    screenshots = models.JSONField(blank=True, null=True)
    version_history = models.JSONField(blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)

    provider = models.CharField(max_length=200, blank=True)
    size = models.IntegerField(blank=True, null=True)
    category = models.CharField(max_length=200, blank=True)
    compatibility = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-updated_at']
