from django.contrib.postgres.fields import ArrayField
from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-updated_at']


class Bank(BaseModel):
    url_self_cbr = models.URLField(blank=True)
    url_self_banki = models.URLField(blank=True)

    full_name = models.TextField(blank=True, help_text='Полное фирменное наименование')
    name = models.TextField(blank=True, help_text='Сокращённое фирменное наименование')
    reg_number = models.TextField(blank=True, help_text='Регистрационный номер')
    registration_date = models.DateTimeField(blank=True, null=True, help_text='Дата регистрации Банком России')
    ogrn = models.TextField(blank=True, help_text='Основной государственный регистрационный номер')
    ogrn_date = models.DateTimeField(blank=True, null=True)
    bik = models.TextField(blank=True, help_text='БИК')
    statutory_address = models.TextField(blank=True, help_text='Адрес из устава')
    actual_address = models.TextField(blank=True, help_text='Адрес фактический')
    tel_number = ArrayField(models.TextField(), blank=True, null=True, help_text='Телефон')
    statutory_update = models.DateTimeField(blank=True, null=True)
    authorized_capital = models.BigIntegerField(blank=True, null=True, help_text='Уставный капитал')
    authorized_capital_date = models.DateTimeField(blank=True, null=True)
    license_info = ArrayField(models.TextField(), blank=True, null=True, help_text='Лицензия (дата выдачи/последней замены)')
    license_info_file = models.URLField(blank=True, help_text='Лицензия файлом')
    deposit_insurance_system = models.BooleanField(blank=True, null=True, help_text='Участие в системе страхования вкладов')
    english_name = models.TextField(blank=True, help_text='Фирменное наименование на английском языке')

    bank_subsidiaries = models.TextField(blank=True, help_text='Филиалы, инфа о кол-ве')
    bank_agencies = models.BigIntegerField(blank=True, null=True, help_text='Представительства, количество')
    additional_offices = models.BigIntegerField(blank=True, null=True, help_text='Дополнительные офисы, количество')
    operating_cash_desks = models.BigIntegerField(blank=True, null=True, help_text='Операционные кассы вне кассового узла, количество')
    operating_offices = models.BigIntegerField(blank=True, null=True, help_text='Операционные офисы, количество')
    mobile_cash_desks = models.BigIntegerField(blank=True, null=True, help_text='Передвижные пункты кассовых операций, количество')

    info_sites = ArrayField(models.URLField(), blank=True, null=True, help_text='Информационные сайты и страницы организации в социальных сетях')
    cards = models.JSONField(blank=True, null=True, help_text='Сведения об эмиссии и эквайринге банковских карт')
    subsidiaries = models.JSONField(blank=True, null=True, help_text='Филиалы')
    agencies = models.JSONField(blank=True, null=True, help_text='Представительства')

    def __str__(self):
        return self.name


class DebitCard(BaseModel):
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)

    url_self_banki = models.URLField(blank=True)
    url_bank_banki = models.URLField(blank=True)

    name = models.TextField(blank=True)
    images = models.JSONField(blank=True, default=dict)
    summary = ArrayField(models.TextField(), blank=True, null=True, help_text='Основные характеристики')

    borrower_age = models.TextField(blank=True, help_text='Возраст')
    borrower_registration = ArrayField(models.TextField(), blank=True, null=True, help_text='Регистрация')
    expert_positive = ArrayField(models.TextField(), blank=True, null=True, help_text='Плюсы')
    expert_negative = ArrayField(models.TextField(), blank=True, null=True, help_text='Минусы')
    expert_restrictions = ArrayField(models.TextField(), blank=True, null=True, help_text='Особые ограничения')

    debit_type = ArrayField(models.TextField(), blank=True, null=True, help_text='Тип карты')
    technological_features = ArrayField(models.TextField(), blank=True, null=True, help_text='Технологические особенности')
    debit_cashback = models.TextField(blank=True, help_text='Cash Back')
    debit_cashback_description = models.TextField(blank=True)
    debit_bonuses = ArrayField(models.TextField(), blank=True, null=True, help_text='Бонусы')
    interest_accrual = models.JSONField(blank=True, default=dict, help_text='Начисление процентов на остаток средств на счете')
    service_cost = models.JSONField(blank=True, default=dict, help_text='Выпуск и годовое обслуживание')
    cash_withdrawal = models.TextField(blank=True, help_text='Снятие наличных в банкоматах банка')
    cash_pickup_point = models.TextField(blank=True, help_text='Снятие наличных в ПВН банка')
    foreign_cash_withdrawal = models.JSONField(blank=True, default=dict, help_text='Снятие наличных в банкоматах других банков')
    foreign_cash_pickup_point = models.JSONField(blank=True, default=dict, help_text='Снятие наличных в ПВН других банков')
    operations_limit = models.JSONField(blank=True, default=dict, help_text='Лимиты по операциям')
    additional_information = ArrayField(models.TextField(), blank=True, null=True, help_text='Дополнительная информация')
    banki_updated_at = models.DateTimeField(blank=True, null=True, help_text='Дата актуализации банки.ру')

    def __str__(self):
        return self.name


class CreditCard(BaseModel):
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)

    url_self_banki = models.URLField(blank=True)
    url_bank_banki = models.URLField(blank=True)

    name = models.TextField(blank=True)
    images = models.JSONField(blank=True, default=dict)
    summary = ArrayField(models.TextField(), blank=True, null=True, help_text='Основные характеристики')

    borrower_age = models.TextField(blank=True, help_text='Возраст')
    borrower_registration = ArrayField(models.TextField(), blank=True, null=True, help_text='Регистрация')
    borrower_income = ArrayField(models.TextField(), blank=True, null=True, help_text='Подтверждение дохода')
    borrower_experience = models.TextField(blank=True, help_text='Стаж работы')
    expert_positive = ArrayField(models.TextField(), blank=True, null=True, help_text='Плюсы')
    expert_negative = ArrayField(models.TextField(), blank=True, null=True, help_text='Минусы')
    expert_restrictions = ArrayField(models.TextField(), blank=True, null=True, help_text='Особые ограничения')

    credit_limit = models.TextField(blank=True, help_text='Размер кредитного лимита')
    credit_limit_description = models.TextField(blank=True)
    credit_period = models.TextField(blank=True, help_text='Срок кредита')
    grace_period = models.TextField(blank=True, help_text='Льготный период')
    percentage_grace = models.TextField(blank=True, help_text='Проценты в течение льготного периода')
    percentage_grace_description = models.TextField(blank=True)
    percentage_credit = models.TextField(blank=True, help_text='Проценты за кредит')
    percentage_credit_description = models.TextField(blank=True)
    repayment = models.TextField(blank=True, help_text='Погашение кредита')
    repayment_description = models.TextField(blank=True)

    credit_type = ArrayField(models.TextField(), blank=True, null=True, help_text='Тип карты')
    technological_features = ArrayField(models.TextField(), blank=True, null=True, help_text='Технологические особенности')
    credit_cashback = models.TextField(blank=True, help_text='Cash Back')
    credit_cashback_description = models.TextField(blank=True)
    credit_bonuses = ArrayField(models.TextField(), blank=True, null=True, help_text='Бонусы')
    interest_accrual = models.JSONField(blank=True, default=dict, help_text='Начисление процентов на остаток средств на счете')
    service_cost = models.JSONField(blank=True, default=dict, help_text='Выпуск и годовое обслуживание')
    cash_withdrawal = models.TextField(blank=True, help_text='Снятие наличных в банкоматах банка')
    cash_pickup_point = models.TextField(blank=True, help_text='Снятие наличных в ПВН банка')
    foreign_cash_withdrawal = models.JSONField(blank=True, default=dict, help_text='Снятие наличных в банкоматах других банков')
    foreign_cash_pickup_point = models.JSONField(blank=True, default=dict, help_text='Снятие наличных в ПВН других банков')
    operations_limit = models.JSONField(blank=True, default=dict, help_text='Лимиты по операциям')
    additional_information = ArrayField(models.TextField(), blank=True, null=True, help_text='Дополнительная информация')
    banki_updated_at = models.DateTimeField(blank=True, null=True, help_text='Дата актуализации банки.ру')

    own_funds = models.BooleanField(blank=True, null=True, help_text='Использование собственных средств')

    def __str__(self):
        return self.name


class AutoCredit(BaseModel):
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)

    url_self_banki = models.URLField(blank=True)
    url_bank_banki = models.URLField(blank=True)

    name = models.TextField(blank=True)
    auto_seller = ArrayField(models.TextField(), blank=True, null=True, help_text='Продавец')
    auto_kind = ArrayField(models.TextField(), blank=True, null=True, help_text='Вид транспортного средства')
    auto_type = ArrayField(models.TextField(), blank=True, null=True, help_text='Тип транспортного средства')
    auto_age = ArrayField(models.TextField(), blank=True, null=True, help_text='Возраст транспортного средства')
    autocredit_min_time = models.TextField(blank=True, help_text='Срок кредита')
    autocredit_max_time = models.TextField(blank=True, help_text='Срок кредита')
    autocredit_currency = models.TextField(blank=True, help_text='Валюта')
    autocredit_amount_min = models.TextField(blank=True, help_text='Сумма кредита')
    autocredit_amount_max = models.TextField(blank=True, help_text='Сумма кредита')
    autocredit_amount_description = models.TextField(blank=True)
    min_down_payment = models.FloatField(blank=True, null=True, help_text='Минимальный первоначальный взнос')
    loan_rate_min = models.FloatField(blank=True, null=True, help_text='Cтавка по кредиту')
    loan_rate_max = models.FloatField(blank=True, null=True, help_text='Cтавка по кредиту')
    loan_rate_description = models.TextField(blank=True)
    autocredit_comission = models.TextField(blank=True, help_text='Комиссии при рассмотрении')
    early_moratorium_repayment = models.TextField(blank=True, help_text='Мораторий на досрочное погашение')
    prepayment_penalty = models.TextField(blank=True, help_text='Штраф за досрочное погашение')
    insurance_necessity = models.BooleanField(blank=True, null=True, help_text='Необходимость страхования')
    borrowers_age = models.TextField(blank=True, help_text='Возраст заёмщика')
    borrowers_age_description = models.TextField(blank=True)
    income_proof = ArrayField(models.TextField(), blank=True, null=True, help_text='Подтверждение дохода')
    registration_requirements = ArrayField(models.TextField(), blank=True, null=True, help_text='Регистрация по месту получения кредита')
    last_work_experience = models.TextField(blank=True, help_text='Стаж работы на последнем месте')
    full_work_experience = models.TextField(blank=True, help_text='Стаж работы общий')
    additional_conditions = models.TextField(blank=True, help_text='Особые условия')
    banki_updated_at = models.DateTimeField(blank=True, null=True, help_text='Дата актуализации банки.ру')
    has_repurchase = models.BooleanField(default=False, help_text='Возможность обратного выкупа')

    def __str__(self):
        return self.name


class ConsumerCredit(BaseModel):
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)

    url_self_banki = models.URLField(blank=True)
    url_bank_banki = models.URLField(blank=True)

    name_base = models.TextField(blank=True)
    name_full = models.TextField(blank=True)

    account_currency = models.TextField(blank=True, help_text='Валюта счета')
    loan_purpose = models.TextField(blank=True, help_text='Цель кредита')
    loan_purpose_description = models.TextField(blank=True)
    credit_fee = models.JSONField(blank=True, default=dict, help_text='Комиссии')
    credit_fee_description = models.JSONField(blank=True, default=dict)
    loan_security = models.JSONField(blank=True, default=dict, help_text='Обеспечение')
    loan_security_description = models.TextField(blank=True)
    credit_insurance = models.JSONField(blank=True, default=dict, help_text='Страхование')
    credit_insurance_description = models.TextField(blank=True)
    additional_information = models.TextField(blank=True, help_text='Дополнительная информация')
    rates_table = models.JSONField(blank=True, default=dict, help_text='Таблица ставок')
    borrowers_category = ArrayField(models.TextField(), blank=True, null=True, help_text='Категория заемщиков')
    borrowers_age_men = models.TextField(blank=True, help_text='Возраст заемщика')
    borrowers_age_women = models.TextField(blank=True, help_text='Возраст заемщика')
    work_experience = models.TextField(blank=True, help_text='Стаж работы')
    work_experience_description = models.TextField(blank=True)
    borrowers_registration = ArrayField(models.TextField(), blank=True, null=True, help_text='Регистрация')
    borrowers_income_description = models.TextField(blank=True, help_text='Доход')
    borrowers_income_tip = models.TextField(blank=True, help_text='Доход')
    borrowers_income_documents = models.JSONField(blank=True, default=dict, help_text='Доход')
    borrowers_documents = models.JSONField(blank=True, default=dict, help_text='Документы')
    borrowers_documents_description = models.TextField(blank=True)
    application_consider_time = models.TextField(blank=True, help_text='Срок рассмотрения заявки')
    application_consider_time_description = models.TextField(blank=True)
    credit_decision_time = models.TextField(blank=True, help_text='Максимальный срок действия кредитного решения')
    loan_processing_terms = ArrayField(models.TextField(), blank=True, null=True, help_text='Оформление кредита')
    loan_delivery_order = ArrayField(models.TextField(), blank=True, null=True, help_text='Режим выдачи')
    loan_delivery_order_description = models.TextField(blank=True)
    loan_delivery_type = ArrayField(models.TextField(), blank=True, null=True, help_text='Форма выдачи')
    loan_delivery_type_description = models.TextField(blank=True)
    repayment_procedure = ArrayField(models.TextField(), blank=True, null=True, help_text='Порядок погашения')
    repayment_procedure_description = models.TextField(blank=True)
    early_repayment_full = ArrayField(models.TextField(), blank=True, null=True, help_text='Досрочное погашение полное')
    early_repayment_partial = ArrayField(models.TextField(), blank=True, null=True, help_text='Досрочное погашение частичное')
    obligations_violation = models.TextField(blank=True, help_text='Нарушение обязательств по кредиту')
    payment_method = ArrayField(models.TextField(), blank=True, null=True, help_text='Способ оплаты')
    banki_updated_at = models.DateTimeField(blank=True, null=True, help_text='Дата актуализации банки.ру')

    def __str__(self):
        return self.name_full


class Deposit(BaseModel):
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)

    url_self_banki = models.URLField(blank=True)
    url_bank_banki = models.URLField(blank=True)

    name_base = models.TextField(blank=True)
    name_full = models.TextField(blank=True)

    deposit_amount = models.TextField(blank=True)
    deposit_currency = models.TextField(blank=True)
    deposit_term = models.TextField(blank=True)

    interest_payment = models.TextField(blank=True, help_text='Выплата процентов')
    interest_payment_description = models.TextField(blank=True)
    capitalization = models.TextField(blank=True, help_text='Капитализация')
    special_contribution = models.TextField(blank=True, help_text='Специальный вклад')
    special_contribution_description = models.TextField(blank=True)
    is_staircase_contribution = models.BooleanField(default=False, help_text='Лестничный вклад')
    special_conditions = ArrayField(models.TextField(), blank=True, null=True, help_text='Особые условия')
    replenishment_ability = models.IntegerField(blank=True, null=True, help_text='Пополнение')
    replenishment_description = models.TextField(blank=True)
    min_irreducible_balance = models.TextField(blank=True, help_text='Минимальный неснижаемый остаток')
    early_dissolution = models.TextField(blank=True, help_text='Досрочное расторжение')
    early_dissolution_description = models.TextField(blank=True)
    auto_prolongation = models.IntegerField(blank=True, null=True, help_text='Автопролонгация')
    auto_prolongation_description = models.TextField(blank=True)
    rates_table = models.JSONField(blank=True, default=dict, help_text='Таблица ставок')
    rates_comments = ArrayField(models.TextField(), blank=True, null=True, help_text='Комментарии к таблице ставок')
    online_opening = models.TextField(blank=True, help_text='Открытие вклада online')
    partial_withdrawal = models.TextField(blank=True, help_text='Частичное снятие')
    partial_withdrawal_description = models.TextField(blank=True)
    banki_updated_at = models.DateTimeField(blank=True, null=True, help_text='Дата актуализации банки.ру')

    def __str__(self):
        return self.name_full


class Branch(BaseModel):
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)

    id_self_banki = models.CharField(max_length=200, blank=True)
    url_bank_banki = models.URLField(blank=True)

    latitude = models.CharField(max_length=200, blank=True)
    longitude = models.CharField(max_length=200, blank=True)
    name = models.CharField(max_length=200, blank=True)
    address = models.CharField(max_length=200, blank=True)
    type = models.CharField(max_length=200, blank=True)
    bank_name = models.CharField(max_length=200, blank=True)
    metro = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=200, blank=True)
    schedule = models.JSONField(blank=True, null=True)

    region_name = models.CharField(max_length=200, blank=True)
    region_name_full = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name


class Rating(BaseModel):
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)

    url_self_banki = models.URLField(blank=True)
    url_bank_banki = models.URLField(blank=True)

    net_assets = models.JSONField(
        blank=True,
        null=True,
        help_text='Активы нетто',
    )
    net_profit = models.JSONField(
        blank=True,
        null=True,
        help_text='Чистая прибыль',
    )
    equity = models.JSONField(
        blank=True,
        null=True,
        help_text='Капитал (по форме 123)',
    )
    credit_portfolio = models.JSONField(
        blank=True,
        null=True,
        help_text='Кредитный портфель',
    )
    npls = models.JSONField(
        blank=True,
        null=True,
        help_text='Просроченная задолженность в кредитном портфеле',
    )
    private_deposits = models.JSONField(
        blank=True,
        null=True,
        help_text='Вклады физических лиц',
    )
    investment_in_securities = models.JSONField(
        blank=True,
        null=True,
        help_text='Вложения в ценные бумаги',
    )
    household_credits = models.JSONField(
        blank=True,
        null=True,
        help_text='Кредиты физическим лицам',
    )
    loans_extended_to_businesses_and_institutions = models.JSONField(
        blank=True,
        null=True,
        help_text='Кредиты предприятиям и организациям',
    )
    funds_held_by_businesses_and_institutions = models.JSONField(
        blank=True,
        null=True,
        help_text='Средства предприятий и организаций',
    )
    interbank_loans_raised = models.JSONField(
        blank=True,
        null=True,
        help_text='Привлеченные МБК',
    )
    promissory_notes_and_bonds_issued = models.JSONField(
        blank=True,
        null=True,
        help_text='Выпущенные облигации и векселя',
    )
    loro_accounts = models.JSONField(
        blank=True,
        null=True,
        help_text='ЛОРО-счета',
    )
    return_on_assets = models.JSONField(
        blank=True,
        null=True,
        help_text='Рентабельность активов-нетто',
    )
    return_on_equity = models.JSONField(
        blank=True,
        null=True,
        help_text='Рентабельность капитала',
    )
    overdue_debts_to_loans_portfolio = models.JSONField(
        blank=True,
        null=True,
        help_text='Уровень просроченной задолженности по кредитному портфелю',
    )
    level_of_provisioning_loan_portfolio = models.JSONField(
        blank=True,
        null=True,
        help_text='Уровень резервирования по кредитному портфелю',
    )
    level_of_ensuring_loan_portfolio_by_pledge_of_property = models.JSONField(
        blank=True,
        null=True,
        help_text='Уровень обеспечения кредитного портфеля залогом имущества',
    )
    n1 = models.JSONField(
        blank=True,
        null=True,
        help_text='Н1',
    )
    n2 = models.JSONField(
        blank=True,
        null=True,
        help_text='Н2',
    )
    n3 = models.JSONField(
        blank=True,
        null=True,
        help_text='Н3',
    )

    def __str__(self):
        return str(self.bank)
