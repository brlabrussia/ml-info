import json

from django.db.models import Q

from ..models import (
    AutoCredit,
    Bank,
    BankAgency,
    BankCard,
    BankSubsidiary,
    ConsumerCredit,
    CreditCard,
    DebitCard,
    Deposit,
)

INPUT_PATH = 'banks/utils/setup_input/{}.json'


def main():
    banks()
    debit_cards()
    credit_cards()
    auto_credits()
    consumer_credits()
    deposits()


def banks():
    for model in [Bank, BankCard, BankSubsidiary, BankAgency]:
        model.objects.all().delete()

    with open(INPUT_PATH.format('banks_cbr')) as f:
        for item in json.load(f):
            custom = {
                'cards': BankCard,
                'subsidiaries': BankSubsidiary,
                'agencies': BankAgency,
            }

            bank = Bank.objects.create(**{
                key: value
                for key, value in item.items()
                if key not in custom
            })

            for key in custom:
                if key in item:
                    for custom_item in item[key]:
                        custom[key].objects.create(bank=bank, **custom_item)

    with open(INPUT_PATH.format('banks_banki')) as f:
        for item in json.load(f):
            reg_number = item.get('reg_number')
            ogrn = item.get('ogrn')
            qs = Bank.objects.filter(
                Q(reg_number__isnull=False, reg_number=reg_number)
                | Q(ogrn__isnull=False, ogrn=ogrn),
            )
            if qs.exists():
                bank = qs.first()
                bank.banki_url = item.get('banki_url')
                bank.save()


def debit_cards():
    DebitCard.objects.all().delete()

    with open(INPUT_PATH.format('banki_debit_cards')) as f:
        for item in json.load(f):
            banki_bank_url = item.get('banki_bank_url')
            qs = Bank.objects.filter(banki_url__isnull=False, banki_url=banki_bank_url)
            if qs.exists():
                DebitCard.objects.create(**item, bank=qs.first())


def credit_cards():
    CreditCard.objects.all().delete()

    with open(INPUT_PATH.format('banki_credit_cards')) as f:
        for item in json.load(f):
            banki_bank_url = item.get('banki_bank_url')
            qs = Bank.objects.filter(banki_url__isnull=False, banki_url=banki_bank_url)
            if qs.exists():
                CreditCard.objects.create(**item, bank=qs.first())


def auto_credits():
    AutoCredit.objects.all().delete()

    with open(INPUT_PATH.format('banki_auto_credits')) as f:
        for item in json.load(f):
            banki_bank_url = item.get('banki_bank_url')
            qs = Bank.objects.filter(banki_url__isnull=False, banki_url=banki_bank_url)
            if qs.exists():
                AutoCredit.objects.create(**item, bank=qs.first())


def consumer_credits():
    ConsumerCredit.objects.all().delete()

    with open(INPUT_PATH.format('banki_consumer_credits')) as f:
        for item in json.load(f):
            banki_bank_url = item.get('banki_bank_url')
            qs = Bank.objects.filter(banki_url__isnull=False, banki_url=banki_bank_url)
            if qs.exists():
                ConsumerCredit.objects.create(**item, bank=qs.first())


def deposits():
    Deposit.objects.all().delete()

    with open(INPUT_PATH.format('banki_deposits')) as f:
        for item in json.load(f):
            banki_bank_url = item.get('banki_bank_url')
            qs = Bank.objects.filter(banki_url__isnull=False, banki_url=banki_bank_url)
            if qs.exists():
                Deposit.objects.create(**item, bank=qs.first())


if __name__ == '__main__':
    main()
