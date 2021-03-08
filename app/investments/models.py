from django.core.validators import RegexValidator
from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-updated_at']


class Share(BaseModel):
    isin = models.CharField(
        max_length=12,
        validators=[RegexValidator(r'^\w{12}$')],
        unique=True,
        help_text='ИСИН',
    )
    name = models.CharField(max_length=200, blank=True, help_text='Название акции')
    logo = models.URLField(blank=True, help_text='Логотип компании')
    price = models.FloatField(blank=True, null=True, help_text='Текущая цена')
    price_dynamic = models.JSONField(blank=True, null=True, help_text='Динамика изменения акций')
    dividend_history = models.JSONField(blank=True, null=True, help_text='История дивидендной доходности')
    seo_quote = models.JSONField(blank=True, null=True, help_text='Сеошный текст по котировкам')

    def __str__(self):
        return self.name


class Bond(BaseModel):
    isin = models.CharField(
        max_length=12,
        validators=[RegexValidator(r'^\w{12}$')],
        unique=True,
        help_text='ИСИН',
    )
    name = models.CharField(max_length=200, blank=True, help_text='Наименование облигации')
    issuer = models.CharField(max_length=200, blank=True, help_text='Наименование эмитента')
    logo = models.URLField(blank=True, help_text='Логотип компании')
    price = models.FloatField(blank=True, null=True, help_text='Цена за 1 облигацию')
    risk = models.PositiveSmallIntegerField(blank=True, null=True, help_text='Индикатор риска при покупке облигации')
    maturity_yield = models.FloatField(blank=True, null=True, help_text='Доходность к погашению')
    maturity_date = models.DateTimeField(blank=True, null=True, help_text='Срок до погашения')
    offer_yield = models.FloatField(blank=True, null=True, help_text='Доходность к оферте')
    offer_date = models.DateTimeField(blank=True, null=True, help_text='Ближайшая оферта')
    coupon_yield = models.FloatField(blank=True, null=True, help_text='Купон')
    coupon_date = models.DateTimeField(blank=True, null=True, help_text='Ближайшая выплата купона')

    def __str__(self):
        return self.name


class IIA(BaseModel):
    name = models.CharField(max_length=200, blank=True, help_text='Наименование ИИС')
    company = models.CharField(max_length=200, blank=True, help_text='Наименование компании')
    logo = models.URLField(blank=True, help_text='Логотип компании')
    filter = models.CharField(max_length=200, blank=True, help_text='Фильтр, по которому выводит данный ИИС (высокий риск, низкий риск и тп)')
    investment_min = models.PositiveIntegerField(blank=True, null=True, help_text='Мин. инвестиция')
    yield_type = models.CharField(max_length=200, blank=True, help_text='Тип доходности из шапки/списка')
    yield_value = models.FloatField(blank=True, null=True, help_text='Значение доходности из шапки/списка')
    yield_block = models.JSONField(blank=True, null=True, help_text='Блок с доходностями с банки.ру')
    fees = models.JSONField(blank=True, null=True, help_text='Комиссии')
    docs = models.JSONField(blank=True, null=True, help_text='Документы')

    def __str__(self):
        return self.name


class Mutual(BaseModel):
    name = models.CharField(max_length=200, blank=True, help_text='Наименование ПИФ')
    company = models.CharField(max_length=200, blank=True, help_text='Наименование компании')
    logo = models.URLField(blank=True, help_text='Логотип компании')
    filter = models.CharField(max_length=200, blank=True, help_text='Фильтр, по которому выводит данный ПИФ (в тч ETF)')
    investment_min = models.PositiveIntegerField(blank=True, null=True, help_text='Мин. инвестиция')
    yield_type = models.CharField(max_length=200, blank=True, help_text='Тип доходности из шапки/списка')
    yield_value = models.FloatField(blank=True, null=True, help_text='Значение доходности из шапки/списка')
    yield_block = models.JSONField(blank=True, null=True, help_text='Блок с доходностями с банки.ру')
    fees = models.JSONField(blank=True, null=True, help_text='Комиссии')
    docs = models.JSONField(blank=True, null=True, help_text='Документы')

    def __str__(self):
        return self.name
