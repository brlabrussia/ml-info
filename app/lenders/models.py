from django.contrib.postgres.fields import ArrayField
from django.db import models


class Lender(models.Model):
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    scraped_from = ArrayField(models.URLField())

    trademark = models.TextField('Торговая марка', blank=True)
    name = models.TextField('Сокращенное наименование', blank=True)
    full_name = models.TextField('Полное наименование', blank=True)
    logo = models.URLField()

    is_legal = models.BooleanField(default=False)
    type = models.TextField('Вид МФО', blank=True)
    regdate = models.DateTimeField('Дата внесения в ЦБ', blank=True, null=True)
    regnum = models.BigIntegerField('Регномер ЦБ', unique=True, blank=True, null=True)
    ogrn = models.BigIntegerField('ОГРН', unique=True, blank=True, null=True)
    inn = models.BigIntegerField('ИНН', unique=True, blank=True, null=True)

    website = models.URLField('Вебсайт', blank=True)
    email = models.EmailField('Электронная почта', blank=True)
    socials = ArrayField(models.URLField(), verbose_name='Соцсети', blank=True, null=True)
    address = models.TextField('Адрес', blank=True)
    head_name = models.TextField('Руководитель', blank=True)

    amount_min = models.IntegerField('Минимальная сумма займа', blank=True, null=True)
    amount_max = models.IntegerField('Максимальная сумма займа', blank=True, null=True)
    overpayment_day = models.IntegerField('Переплата за день', blank=True, null=True)
    overpayment_full = models.IntegerField('Переплата за весь срок', blank=True, null=True)
    refusal_reasons = ArrayField(models.TextField(), verbose_name='Причины отказа', blank=True, null=True)

    def __str__(self):
        return self.trademark or self.name


class Document(models.Model):
    lender = models.ForeignKey(Lender, on_delete=models.CASCADE)
    name = models.TextField()
    url = models.URLField()


class Loan(models.Model):
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    scraped_from = models.URLField(unique=True)

    # * О займе
    # https://www.banki.ru/microloans/products/2/
    name = models.TextField('Название займа')
    last_modified = models.DateTimeField('Дата актуализации')
    # ** Условия и ставки
    purpose = ArrayField(models.TextField(), verbose_name='Цель займа')
    amount_max = models.IntegerField('Максимальная сумма займа')
    amount_note = models.TextField('Допинфа по сумме займа', blank=True)  # first_loan_condition
    rate = models.TextField('Ставка')
    period_min = models.IntegerField('Минимальный срок займа')  # dates_from
    period_max = models.IntegerField('Максимальный срок займа')  # dates_to
    period_note = models.TextField('Допинфа по срокам', blank=True)  # loan_time_terms
    collateral = ArrayField(models.TextField(), verbose_name='Обеспечение')  # providing
    # ** Требования и документы
    borrowers_categories = ArrayField(models.TextField(), verbose_name='Категория заемщиков')
    borrowers_age = models.TextField('Возраст заемщика')
    borrowers_registration = ArrayField(models.TextField(), verbose_name='Регистрация')
    borrowers_documents = ArrayField(models.TextField(), verbose_name='Документы')
    # ** Выдача
    issuance = models.TextField('Срок выдачи')
    loan_processing = ArrayField(models.TextField(), verbose_name='Оформление займа')
    loan_form = ArrayField(models.TextField(), verbose_name='Форма выдачи')
    loan_form_note = models.TextField('Допинфа по форме выдачи', blank=True)  # loan_form_description
    # ** Погашение
    repayment_order = ArrayField(models.TextField(), verbose_name='Порядок погашения')
    repayment_order_note = models.TextField('Допинфа по порядку погашения', blank=True)  # repayment_order_description
    payment_methods = ArrayField(models.TextField(), verbose_name='Способ оплаты')

    # * Об организации
    # We merge based on scraped data, which can be outdated so we keep it for future debugging
    lender = models.ForeignKey(Lender, on_delete=models.CASCADE)
    logo = models.URLField('Логотип организации')
    trademark = models.TextField('Торговая марка')
    address = models.TextField('Адрес')
    head_name = models.TextField('Руководитель')
    regnum = models.BigIntegerField('Регномер ЦБ')
    ogrn = models.BigIntegerField('ОГРН')

    def __str__(self):
        return self.name
