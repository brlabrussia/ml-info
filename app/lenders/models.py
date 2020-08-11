from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.core.validators import RegexValidator


class Lender(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    scraped_from = ArrayField(models.URLField())

    trademark = models.TextField(blank=True, help_text='Торговая марка')
    name = models.TextField(blank=True, help_text='Сокращенное наименование')
    full_name = models.TextField(blank=True, help_text='Полное наименование')
    logo = models.URLField(blank=True, help_text='Логотип')
    # documents = ArrayField(JSONField(), blank=True, null=True, help_text='Документы')

    is_legal = models.BooleanField(default=False, help_text='Легальная МФО (есть в реестре ЦБ)')
    cbr_created_at = models.DateTimeField(blank=True, null=True, help_text='Дата внесения в реестр ЦБ')
    type = models.TextField(blank=True, help_text='Вид МФО')
    cbrn = models.CharField(
        max_length=13,
        validators=(RegexValidator(r'\d{13}$'),),
        unique=True,
        blank=True,
        help_text='Регномер в ЦБ',
    )
    ogrn = models.CharField(
        max_length=13,
        validators=(RegexValidator(r'\d{13}$'),),
        unique=True,
        blank=True,
        null=True,
        help_text='ОГРН',
    )
    inn = models.CharField(
        max_length=10,
        validators=(RegexValidator(r'\d{10}$'),),
        unique=True,
        blank=True,
        null=True,
        help_text='ИНН',
    )

    website = models.URLField(blank=True, help_text='Вебсайт')
    email = models.EmailField(blank=True, help_text='Электронная почта')
    socials = ArrayField(models.URLField(), blank=True, null=True, help_text='Соцсети')
    address = models.TextField(blank=True, help_text='Адрес')
    head_name = models.TextField(blank=True, help_text='Руководитель')

    decision_speed = models.TextField(blank=True, help_text='Скорость рассмотрения заявки')
    payment_speed = models.TextField(blank=True, help_text='Скорость выплаты')
    amount_min = models.PositiveIntegerField(blank=True, null=True, help_text='Минимальная сумма займа')
    amount_max = models.PositiveIntegerField(blank=True, null=True, help_text='Максимальная сумма займа')
    overpayment_day = models.PositiveIntegerField(blank=True, null=True, help_text='Переплата за день')
    overpayment_full = models.PositiveIntegerField(blank=True, null=True, help_text='Переплата за весь срок')
    decline_reasons = ArrayField(models.TextField(), blank=True, null=True, help_text='Причины отказа')

    def __str__(self):
        return self.trademark or self.name


class Document(models.Model):
    lender = models.ForeignKey(Lender, on_delete=models.CASCADE, related_name='documents')
    name = models.TextField()
    url = models.URLField()


class Loan(models.Model):
    lender = models.ForeignKey(Lender, on_delete=models.CASCADE, related_name='loans')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # * О займе
    # https://www.banki.ru/microloans/products/2/
    name = models.TextField(help_text='Название займа')
    banki_url = models.URLField(unique=True, help_text='Ссылка на Банки.ру')
    banki_updated_at = models.DateTimeField(blank=True, null=True, help_text='Дата актуализации на Банки.ру')
    # ** Условия и ставки
    purposes = ArrayField(models.TextField(), blank=True, null=True, help_text='Цель займа')
    amount_min = models.PositiveIntegerField(blank=True, null=True, help_text='Минимальная сумма займа')
    amount_max = models.PositiveIntegerField(blank=True, null=True, help_text='Максимальная сумма займа')
    amount_note = models.TextField(blank=True, help_text='Допинфа по сумме займа')
    rate = models.TextField(blank=True, help_text='Ставка')
    period_min = models.PositiveIntegerField(blank=True, null=True, help_text='Минимальный срок займа')
    period_max = models.PositiveIntegerField(blank=True, null=True, help_text='Максимальный срок займа')
    period_note = models.TextField(blank=True, help_text='Допинфа по срокам')
    collateral = ArrayField(models.TextField(), blank=True, null=True, help_text='Обеспечение')
    # ** Требования и документы
    borrower_categories = ArrayField(models.TextField(), blank=True, null=True, help_text='Категории заемщиков')
    borrower_age = models.TextField(blank=True, help_text='Возраст заемщика')
    borrower_registration = ArrayField(models.TextField(), blank=True, null=True, help_text='Регистрация заемщика')
    borrower_documents = ArrayField(models.TextField(), blank=True, null=True, help_text='Документы заемщика')
    # ** Выдача
    application_process = ArrayField(models.TextField(), blank=True, null=True, help_text='Оформление займа')
    payment_speed = models.TextField(blank=True, help_text='Срок выдачи')
    payment_forms = ArrayField(models.TextField(), blank=True, null=True, help_text='Форма выдачи')
    payment_forms_note = models.TextField(blank=True, help_text='Допинфа по форме выдачи')
    # ** Погашение
    repayment_process = ArrayField(models.TextField(), blank=True, null=True, help_text='Порядок погашения')
    repayment_process_note = models.TextField(blank=True, help_text='Допинфа по порядку погашения')
    repayment_forms = ArrayField(models.TextField(), blank=True, null=True, help_text='Способ оплаты')

    # * Об организации
    # We merge based on scraped data, which can be outdated so we keep it for future debugging
    lender_logo = models.URLField(blank=True, help_text='Логотип организации')
    lender_trademark = models.TextField(blank=True, help_text='Торговая марка')
    lender_address = models.TextField(blank=True, help_text='Адрес')
    lender_head_name = models.TextField(blank=True, help_text='Руководитель')
    lender_cbrn = models.CharField(
        max_length=13,
        validators=(RegexValidator(r'\d{13}$'),),
        unique=True,
        blank=True,
        help_text='Регномер в ЦБ',
    )
    lender_ogrn = models.CharField(
        max_length=13,
        validators=(RegexValidator(r'^\d{13}$'),),
        unique=True,
        blank=True,
        null=True,
        help_text='ОГРН',
    )

    def __str__(self):
        return self.name
