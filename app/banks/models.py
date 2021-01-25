from django.contrib.postgres.fields import ArrayField
from django.db import models


class Bank(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    cbr_url = models.URLField(blank=True)
    banki_url = models.URLField(blank=True)

    full_name = models.TextField(blank=True)
    name = models.TextField(blank=True)
    reg_number = models.TextField(blank=True)
    registration_date = models.DateTimeField(blank=True, null=True)
    ogrn = models.TextField(blank=True)
    ogrn_date = models.DateTimeField(blank=True, null=True)
    bik = models.TextField(blank=True)
    statutory_address = models.TextField(blank=True)
    actual_address = models.TextField(blank=True)
    tel_number = ArrayField(models.TextField(), blank=True, null=True)
    statutory_update = models.DateTimeField(blank=True, null=True)
    authorized_capital = models.BigIntegerField(blank=True, null=True)
    authorized_capital_date = models.DateTimeField(blank=True, null=True)
    license_info = ArrayField(models.TextField(), blank=True, null=True)
    license_info_file = models.URLField(blank=True)
    deposit_insurance_system = models.BooleanField(blank=True, null=True)
    english_name = models.TextField(blank=True)

    bank_subsidiaries = models.TextField(blank=True)
    bank_agencies = models.BigIntegerField(blank=True, null=True)
    additional_offices = models.BigIntegerField(blank=True, null=True)
    operating_cash_desks = models.BigIntegerField(blank=True, null=True)
    operating_offices = models.BigIntegerField(blank=True, null=True)
    mobile_cash_desks = models.BigIntegerField(blank=True, null=True)

    info_sites = ArrayField(models.URLField(), blank=True, null=True)
    # cards = models.JSONField(blank=True, default=dict)
    # subsidiaries = models.JSONField(blank=True, default=dict)
    # agencies = models.JSONField(blank=True, default=dict)

    def __str__(self):
        return self.name


class BankCard(models.Model):
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, related_name='cards')
    pay_system = models.TextField(blank=True)
    emission = models.BooleanField(blank=True, null=True)
    acquiring = models.BooleanField(blank=True, null=True)


class BankSubsidiary(models.Model):
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, related_name='subsidiaries')
    reg_number = models.TextField(blank=True)
    name = models.TextField(blank=True)
    reg_date = models.DateTimeField(blank=True, null=True)
    address = models.TextField(blank=True)


class BankAgency(models.Model):
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, related_name='agencies')
    name = models.TextField(blank=True)
    foundation_date = models.DateTimeField(blank=True, null=True)
    address = models.TextField(blank=True)


class DebitCard(models.Model):
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, related_name='debit_cards')

    banki_url = models.URLField(blank=True)
    banki_bank_url = models.URLField(blank=True)

    name = models.TextField(blank=True)
    images = models.JSONField(blank=True, default=dict)
    summary = ArrayField(models.TextField(), blank=True, null=True)

    borrower_age = models.TextField(blank=True)
    borrower_registration = ArrayField(models.TextField(), blank=True, null=True)
    expert_positive = ArrayField(models.TextField(), blank=True, null=True)
    expert_negative = ArrayField(models.TextField(), blank=True, null=True)
    expert_restrictions = ArrayField(models.TextField(), blank=True, null=True)

    debit_type = ArrayField(models.TextField(), blank=True, null=True)
    technological_features = ArrayField(models.TextField(), blank=True, null=True)
    debit_cashback = models.TextField(blank=True)
    debit_cashback_description = models.TextField(blank=True)
    debit_bonuses = ArrayField(models.TextField(), blank=True, null=True)
    interest_accrual = models.JSONField(blank=True, default=dict)
    service_cost = models.JSONField(blank=True, default=dict)
    cash_withdrawal = models.TextField(blank=True)
    cash_pickup_point = models.TextField(blank=True)
    foreign_cash_withdrawal = models.JSONField(blank=True, default=dict)
    foreign_cash_pickup_point = models.JSONField(blank=True, default=dict)
    operations_limit = models.JSONField(blank=True, default=dict)
    additional_information = ArrayField(models.TextField(), blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name


class CreditCard(models.Model):
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, related_name='credit_cards')

    banki_url = models.URLField(blank=True)
    banki_bank_url = models.URLField(blank=True)

    name = models.TextField(blank=True)
    images = models.JSONField(blank=True, default=dict)
    summary = ArrayField(models.TextField(), blank=True, null=True)

    borrower_age = models.TextField(blank=True)
    borrower_registration = ArrayField(models.TextField(), blank=True, null=True)
    borrower_income = ArrayField(models.TextField(), blank=True, null=True)
    borrower_experience = models.TextField(blank=True)
    expert_positive = ArrayField(models.TextField(), blank=True, null=True)
    expert_negative = ArrayField(models.TextField(), blank=True, null=True)
    expert_restrictions = ArrayField(models.TextField(), blank=True, null=True)

    credit_limit = models.TextField(blank=True)
    credit_limit_description = models.TextField(blank=True)
    credit_period = models.TextField(blank=True)
    grace_period = models.TextField(blank=True)
    percentage_grace = models.TextField(blank=True)
    percentage_grace_description = models.TextField(blank=True)
    percentage_credit = models.TextField(blank=True)
    percentage_credit_description = models.TextField(blank=True)
    repayment = models.TextField(blank=True)
    repayment_description = models.TextField(blank=True)

    credit_type = ArrayField(models.TextField(), blank=True, null=True)
    technological_features = ArrayField(models.TextField(), blank=True, null=True)
    credit_cashback = models.TextField(blank=True)
    credit_cashback_description = models.TextField(blank=True)
    credit_bonuses = ArrayField(models.TextField(), blank=True, null=True)
    interest_accrual = models.JSONField(blank=True, default=dict)
    service_cost = models.JSONField(blank=True, default=dict)
    cash_withdrawal = models.TextField(blank=True)
    cash_pickup_point = models.TextField(blank=True)
    foreign_cash_withdrawal = models.JSONField(blank=True, default=dict)
    foreign_cash_pickup_point = models.JSONField(blank=True, default=dict)
    operations_limit = models.JSONField(blank=True, default=dict)
    additional_information = ArrayField(models.TextField(), blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    own_funds = models.BooleanField(blank=True, null=True)

    def __str__(self):
        return self.name


class AutoCredit(models.Model):
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, related_name='auto_credits')

    banki_url = models.URLField(blank=True)
    banki_bank_url = models.URLField(blank=True)

    name = models.TextField(blank=True)

    auto_seller = ArrayField(models.TextField(), blank=True, null=True)
    auto_kind = ArrayField(models.TextField(), blank=True, null=True)
    auto_type = ArrayField(models.TextField(), blank=True, null=True)
    auto_age = ArrayField(models.TextField(), blank=True, null=True)
    autocredit_min_time = models.TextField(blank=True)
    autocredit_max_time = models.TextField(blank=True)
    autocredit_currency = models.TextField(blank=True)
    autocredit_amount_min = models.TextField(blank=True)
    autocredit_amount_max = models.TextField(blank=True)
    autocredit_amount_description = models.TextField(blank=True)
    min_down_payment = models.FloatField(blank=True, null=True)
    loan_rate_min = models.FloatField(blank=True, null=True)
    loan_rate_max = models.FloatField(blank=True, null=True)
    loan_rate_description = models.TextField(blank=True)
    autocredit_comission = models.TextField(blank=True)
    early_moratorium_repayment = models.TextField(blank=True)
    prepayment_penalty = models.TextField(blank=True)
    insurance_necessity = models.BooleanField(blank=True, null=True)
    borrowers_age = models.TextField(blank=True)
    borrowers_age_description = models.TextField(blank=True)
    income_proof = ArrayField(models.TextField(), blank=True, null=True)
    registration_requirements = ArrayField(models.TextField(), blank=True, null=True)
    last_work_experience = models.TextField(blank=True)
    full_work_experience = models.TextField(blank=True)
    additional_conditions = models.TextField(blank=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    has_repurchase = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class ConsumerCredit(models.Model):
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, related_name='consumer_credits')

    banki_url = models.URLField(blank=True)
    banki_bank_url = models.URLField(blank=True)

    name_base = models.TextField(blank=True)
    name_full = models.TextField(blank=True)

    account_currency = models.TextField(blank=True)
    loan_purpose = models.TextField(blank=True)
    loan_purpose_description = models.TextField(blank=True)
    credit_fee = models.JSONField(blank=True, default=dict)
    credit_fee_description = models.JSONField(blank=True, default=dict)
    loan_security = models.JSONField(blank=True, default=dict)
    loan_security_description = models.TextField(blank=True)
    credit_insurance = models.JSONField(blank=True, default=dict)
    credit_insurance_description = models.TextField(blank=True)
    additional_information = models.TextField(blank=True)
    rates_table = models.JSONField(blank=True, default=dict)
    borrowers_category = ArrayField(models.TextField(), blank=True, null=True)
    borrowers_age_men = models.TextField(blank=True)
    borrowers_age_women = models.TextField(blank=True)
    work_experience = models.TextField(blank=True)
    work_experience_description = models.TextField(blank=True)
    borrowers_registration = ArrayField(models.TextField(), blank=True, null=True)
    borrowers_income_description = models.TextField(blank=True)
    borrowers_income_tip = models.TextField(blank=True)
    borrowers_income_documents = models.JSONField(blank=True, default=dict)
    borrowers_documents = models.JSONField(blank=True, default=dict)
    borrowers_documents_description = models.TextField(blank=True)
    application_consider_time = models.TextField(blank=True)
    application_consider_time_description = models.TextField(blank=True)
    credit_decision_time = models.TextField(blank=True)
    loan_processing_terms = ArrayField(models.TextField(), blank=True, null=True)
    loan_delivery_order = ArrayField(models.TextField(), blank=True, null=True)
    loan_delivery_order_description = models.TextField(blank=True)
    loan_delivery_type = ArrayField(models.TextField(), blank=True, null=True)
    loan_delivery_type_description = models.TextField(blank=True)
    repayment_procedure = ArrayField(models.TextField(), blank=True, null=True)
    repayment_procedure_description = models.TextField(blank=True)
    early_repayment_full = ArrayField(models.TextField(), blank=True, null=True)
    early_repayment_partial = ArrayField(models.TextField(), blank=True, null=True)
    obligations_violation = models.TextField(blank=True)
    payment_method = ArrayField(models.TextField(), blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name_full


class Deposit(models.Model):
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, related_name='deposits')

    banki_url = models.URLField(blank=True)
    banki_bank_url = models.URLField(blank=True)

    name_base = models.TextField(blank=True)
    name_full = models.TextField(blank=True)

    deposit_amount = models.TextField(blank=True)
    deposit_currency = models.TextField(blank=True)
    deposit_term = models.TextField(blank=True)

    interest_payment = models.TextField(blank=True)
    interest_payment_description = models.TextField(blank=True)
    capitalization = models.TextField(blank=True)
    special_contribution = models.TextField(blank=True)
    special_contribution_description = models.TextField(blank=True)
    is_staircase_contribution = models.BooleanField(default=False)
    special_conditions = ArrayField(models.TextField(), blank=True, null=True)
    replenishment_ability = models.IntegerField(blank=True, null=True)
    replenishment_description = models.TextField(blank=True)
    min_irreducible_balance = models.TextField(blank=True)
    early_dissolution = models.TextField(blank=True)
    early_dissolution_description = models.TextField(blank=True)
    auto_prolongation = models.IntegerField(blank=True, null=True)
    auto_prolongation_description = models.TextField(blank=True)
    rates_table = models.JSONField(blank=True, default=dict)
    rates_comments = ArrayField(models.TextField(), blank=True, null=True)
    online_opening = models.TextField(blank=True)
    partial_withdrawal = models.TextField(blank=True)
    partial_withdrawal_description = models.TextField(blank=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name_full


class Branch(models.Model):
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, related_name='branches')

    banki_id = models.CharField(max_length=200, blank=True)
    latitude = models.CharField(max_length=200, blank=True)
    longitude = models.CharField(max_length=200, blank=True)
    name = models.CharField(max_length=200, blank=True)
    address = models.CharField(max_length=200, blank=True)
    type = models.CharField(max_length=200, blank=True)

    bank_url = models.URLField(blank=True)
    bank_name = models.CharField(max_length=200, blank=True)

    metro = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=200, blank=True)
    schedule = models.JSONField(blank=True, null=True)

    region_name = models.CharField(max_length=200, blank=True)
    region_name_full = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f'{self.name} ({self.bank_name})'


class Rating(models.Model):
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, related_name='ratings')

    banki_url = models.URLField(blank=True)
    banki_bank_url = models.URLField(blank=True)

    net_assets = models.BigIntegerField(null=True)
    net_profit = models.BigIntegerField(null=True)
    equity = models.BigIntegerField(null=True)
    credit_portfolio = models.BigIntegerField(null=True)
    npls = models.BigIntegerField(null=True)
    private_deposits = models.BigIntegerField(null=True)
    investment_in_securities = models.BigIntegerField(null=True)

    def __str__(self):
        return self.banki_url
