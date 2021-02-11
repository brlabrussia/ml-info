from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-updated_at']


class Person(BaseModel):
    bank = models.ForeignKey('banks.Bank', on_delete=models.SET_NULL, blank=True, null=True)

    url_self_finparty = models.URLField(blank=True)
    url_bank_banki = models.URLField(blank=True)

    name = models.CharField(max_length=200, blank=True)
    photo = models.URLField(blank=True)
    position = models.CharField(max_length=255, blank=True)
    birthday = models.DateTimeField(blank=True, null=True)
    about = models.TextField(blank=True)

    def __str__(self):
        return self.name
