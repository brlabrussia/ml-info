from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-updated_at']


class Casino(BaseModel):
    url_self_casinoguru = models.URLField(blank=True)

    name = models.CharField(max_length=200, blank=True)
    images_logo = models.URLField(blank=True)

    def __str__(self):
        return self.name


class Slot(BaseModel):
    url_self_casinoguru = models.URLField(blank=True)

    name = models.CharField(max_length=200, blank=True)
    iframe_original = models.URLField(blank=True)
    iframe_fallback = models.URLField(blank=True)
    images_logo = models.URLField(blank=True)
    images_content = models.TextField(blank=True)
    videos = models.TextField(blank=True)

    def __str__(self):
        return self.name
