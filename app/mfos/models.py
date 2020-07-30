from django.contrib.postgres.fields import ArrayField
from django.db import models


class Lender(models.Model):
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    scraped_from = ArrayField(models.URLField())

    trademark = models.TextField('Торговая марка', blank=True)
    name = models.TextField(blank=True)
    full_name = models.TextField(blank=True)
    # logo = models.ImageField()  # TODO upload_to='images/', add pillow

    is_legal = models.BooleanField(default=False)
    type = models.TextField(blank=True)
    regdate = models.DateTimeField('date entry added to cbr register', blank=True, null=True)
    regnum = models.IntegerField('number in cbr register', unique=True, null=True)
    ogrn = models.IntegerField(unique=True, null=True)
    inn = models.IntegerField(unique=True, null=True)

    website = models.URLField(blank=True)  # both blank and null?
    email = models.EmailField(blank=True)
    socials = ArrayField(models.URLField(), null=True)
    address = models.TextField('Адрес', blank=True)
    head_name = models.TextField('Руководитель', blank=True)

    amount_min = models.IntegerField()
    amount_max = models.IntegerField()
    overpayment_day = models.IntegerField()
    overpayment_full = models.IntegerField()
    refusal_reasons = ArrayField(models.TextField())


class Document(models.Model):
    lender = models.ForeignKey(Lender, on_delete=models.CASCADE)
    name = models.TextField()
    file = models.FileField()


class Loan(models.Model):
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    scraped_from = models.URLField(unique=True)

    # О займе
    name = models.TextField('Название займа')
    last_modified = models.DateTimeField('Дата актуализации')
    # Условия и ставки
    purpose = ArrayField(models.TextField('Цель займа'))
    amount_max = models.TextField('Максимальная сумма займа')
    amount_note = models.TextField('Допинфа по сумме займа')  # first_loan_condition
    interest_rate = models.TextField('Ставка')  # rate
    period_min = models.IntegerField('Минимальный срок займа')  # dates_from
    period_max = models.IntegerField('Максимальный срок займа')  # dates_to
    period_note = models.TextField('Допинфа по срокам')  # loan_time_terms
    collateral = ArrayField(models.TextField('Обеспечение'))  # providing
    # Требования и документы
    borrowers_categories = ArrayField(models.TextField('Категория заемщиков'))
    borrowers_age = models.TextField('Возраст заемщика')
    borrowers_registration = ArrayField(models.TextField('Регистрация'))
    borrowers_documents = ArrayField(models.TextField('Документы'))
    # Выдача
    issuance = models.TextField('Срок выдачи')
    loan_processing = ArrayField(models.TextField('Оформление займа'))
    loan_form = ArrayField(models.TextField('Форма выдачи'))
    loan_form_note = models.TextField('Допинфа по форме выдачи')  # loan_form_description
    # Погашение
    repayment_order = ArrayField(models.TextField('Порядок погашения'))
    repayment_order_note = models.TextField('Допинфа по порядку погашения')  # repayment_order_description
    payment_methods = ArrayField(models.TextField('Способ оплаты'))

    # Об организации
    # Мерджим по этим данным каждый займ, но они могут быть устаревшими,
    # поэтому для порядка сохраняем
    lender = models.ForeignKey(Lender, on_delete=models.CASCADE)
    logo = models.URLField()
    trademark = models.TextField('Торговая марка')
    address = models.TextField('Адрес')
    head_name = models.TextField('Руководитель')
    regnum = models.IntegerField()
    ogrn = models.IntegerField()
