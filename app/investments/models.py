from django.core.validators import RegexValidator
from django.db import models


class Share(models.Model):
    isin = models.CharField(
        max_length=12,
        validators=[RegexValidator(r'^\w{12}$')],
        unique=True,
    )
    name = models.TextField(blank=True)
    logo = models.URLField(blank=True)
    price = models.FloatField(blank=True, null=True)
    price_dynamic = models.JSONField(blank=True, null=True)
    dividend_history = models.JSONField(blank=True, null=True)
    seo_quote = models.JSONField(blank=True, null=True)

    def __str__(self):
        return self.isin
