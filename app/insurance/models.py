from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-updated_at']


class Company(BaseModel):
    cbrn = models.CharField(max_length=4, help_text='Регистрационный номер ЦБ')
    ogrn = models.CharField(max_length=13, blank=True, help_text='ОГРН')
    inn = models.CharField(max_length=10, blank=True, help_text='ИНН')
    trademark = models.CharField(max_length=200, blank=True, help_text='"Красивое" название как на банки.ру')
    name = models.CharField(max_length=200, blank=True, help_text='Название из реестра ЦБ')
    logo = models.URLField(blank=True, help_text='Ссылка на логотип c банки.ру')
    address = models.CharField(max_length=200, blank=True, help_text='Физический адрес организации')
    federal_subject = models.CharField(max_length=200, blank=True, help_text='Федеральный субъект')
    contacts = models.TextField(blank=True, help_text='Контакты из реестра')
    licenses = models.JSONField(blank=True, null=True, help_text='Лицензии компании')
    authorized_capital = models.PositiveIntegerField(blank=True, null=True, help_text='Уставный капитал')
    net_profit = models.PositiveIntegerField(blank=True, null=True, help_text='Чистая прибыль')
    premiums = models.PositiveIntegerField(blank=True, null=True, help_text='Объем премий')
    payouts = models.PositiveIntegerField(blank=True, null=True, help_text='Объем выплат')
    director = models.CharField(max_length=200, blank=True, help_text='Имя директора')
    director_date = models.DateTimeField(blank=True, null=True, help_text='Дата информации на основании которой указан директор')

    def __str__(self):
        return self.name
