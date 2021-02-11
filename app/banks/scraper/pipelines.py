from banks.models import Bank


class DjangoWriterPipeline:
    def process_item(self, item, spider):
        custom_method = getattr(self, spider.name, None)
        if custom_method is None:
            spider.logger.error(f'Cannot find custom process_item method for {spider.name}')
            return item
        return custom_method(item, spider)

    def banki_rating(self, item, spider):
        qs = Bank.objects.filter(banki_url=item['url_bank_banki'])
        if not qs.exists():
            spider.logger.error(f'Bank not found\n{item}')
            return item
        bank = qs.first()
        if len(item.errors) == 1 and 'bank' in item.errors:
            item.django_model.objects.update_or_create(
                url_self_banki=item['url_self_banki'],
                defaults={'bank': bank, **item},
            )
        else:
            spider.logger.error(f'Invalid item\n{item.errors}')
        return item

    def banki_person(self, item, spider):
        qs = Bank.objects.filter(banki_url=item['url_bank_banki'])
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
