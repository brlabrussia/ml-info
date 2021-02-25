from banks.models import Bank
from django.db.models import Q


class DjangoWriterPipeline:
    def process_item(self, item, spider):
        custom_method = getattr(self, spider.name, None)
        if custom_method is None:
            spider.logger.error(f'Cannot find custom process_item method for {spider.name}')
            return item
        return custom_method(item, spider)

    def bank_cbr(self, item, spider):
        if not item.is_valid():
            spider.logger.error(f'Invalid item\n{item.errors}')
            return item

        try:
            obj = item.django_model.objects.get(url_self_cbr=item['url_self_cbr'])
            for key, value in item.items():
                setattr(obj, key, value)
            obj.save()
        except item.django_model.DoesNotExist:
            spider.logger.error(f'Bank not found\n{item}')

        return item

    def bank_banki(self, item, spider):
        if not item.is_valid():
            spider.logger.error(f'Invalid item\n{item.errors}')
            return item

        reg_number = item.get('reg_number')
        ogrn = item.get('ogrn')
        qs = item.django_model.objects.filter(
            Q(reg_number__isnull=False, reg_number=reg_number)
            | Q(ogrn__isnull=False, ogrn=ogrn),
        )
        if not qs.exists():
            spider.logger.error(f'Bank not found\n{item}')
            return item

        bank = qs.first()
        bank.url_self_banki = item.get('url_self_banki')
        bank.save()

        return item

    def debitcard_banki(self, item, spider):
        if not (len(item.errors) == 1 and 'bank' in item.errors):
            spider.logger.error(f'Invalid item\n{item.errors}')
            return item

        qs = Bank.objects.filter(url_self_banki=item['url_bank_banki'])
        if not qs.exists():
            spider.logger.error(f'Bank not found\n{item}')
            return item

        bank = qs.first()
        item.django_model.objects.update_or_create(
            url_self_banki=item['url_self_banki'],
            defaults={'bank': bank, **item},
        )

        return item

    def creditcard_banki(self, item, spider):
        if not (len(item.errors) == 1 and 'bank' in item.errors):
            spider.logger.error(f'Invalid item\n{item.errors}')
            return item

        qs = Bank.objects.filter(url_self_banki=item['url_bank_banki'])
        if not qs.exists():
            spider.logger.error(f'Bank not found\n{item}')
            return item

        bank = qs.first()
        item.django_model.objects.update_or_create(
            url_self_banki=item['url_self_banki'],
            defaults={'bank': bank, **item},
        )

        return item

    def autocredit_banki(self, item, spider):
        if not (len(item.errors) == 1 and 'bank' in item.errors):
            spider.logger.error(f'Invalid item\n{item.errors}')
            return item

        qs = Bank.objects.filter(url_self_banki=item['url_bank_banki'])
        if not qs.exists():
            spider.logger.error(f'Bank not found\n{item}')
            return item

        bank = qs.first()
        item.django_model.objects.update_or_create(
            url_self_banki=item['url_self_banki'],
            defaults={'bank': bank, **item},
        )

        return item

    def consumercredit_banki(self, item, spider):
        if not (len(item.errors) == 1 and 'bank' in item.errors):
            spider.logger.error(f'Invalid item\n{item.errors}')
            return item

        qs = Bank.objects.filter(url_self_banki=item['url_bank_banki'])
        if not qs.exists():
            spider.logger.error(f'Bank not found\n{item}')
            return item

        bank = qs.first()
        item.django_model.objects.update_or_create(
            url_self_banki=item['url_self_banki'],
            defaults={'bank': bank, **item},
        )

        return item

    def deposit_banki(self, item, spider):
        if not (len(item.errors) == 1 and 'bank' in item.errors):
            spider.logger.error(f'Invalid item\n{item.errors}')
            return item

        qs = Bank.objects.filter(url_self_banki=item['url_bank_banki'])
        if not qs.exists():
            spider.logger.error(f'Bank not found\n{item}')
            return item

        bank = qs.first()
        item.django_model.objects.update_or_create(
            url_self_banki=item['url_self_banki'],
            defaults={'bank': bank, **item},
        )

        return item

    def branch_banki(self, item, spider):
        if not (len(item.errors) == 1 and 'bank' in item.errors):
            spider.logger.error(f'Invalid item\n{item.errors}')
            return item

        qs = Bank.objects.filter(url_self_banki=item['url_bank_banki'])
        if not qs.exists():
            spider.logger.error(f'Bank not found\n{item}')
            return item

        bank = qs.first()
        item.django_model.objects.update_or_create(
            id_self_banki=item['id_self_banki'],
            defaults={'bank': bank, **item},
        )

        return item

    def rating_banki(self, item, spider):
        if not (len(item.errors) == 1 and 'bank' in item.errors):
            spider.logger.error(f'Invalid item\n{item.errors}')
            return item

        qs = Bank.objects.filter(url_self_banki=item['url_bank_banki'])
        if not qs.exists():
            spider.logger.error(f'Bank not found\n{item}')
            return item

        bank = qs.first()
        item.django_model.objects.update_or_create(
            url_self_banki=item['url_self_banki'],
            defaults={'bank': bank, **item},
        )

        return item

    def person_banki(self, item, spider):
        qs = Bank.objects.filter(url_self_banki=item['url_bank_banki'])
        if not qs.exists():
            spider.logger.error(f'Bank not found\n{item}')
            return item
        bank = qs.first()
        if not item.is_valid():
            spider.logger.error(f'Invalid item\n{item.errors}')
        try:
            obj = item.django_model.objects.get(url_self_finparty=item['url_self_finparty'])
            obj.bank = bank
            obj.url_bank_banki = item['url_bank_banki']
            obj.save()
        except item.django_model.DoesNotExist:
            pass
        return item
