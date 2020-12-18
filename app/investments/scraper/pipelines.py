class DjangoWriterPipeline:
    def process_item(self, item, spider):
        custom_method = getattr(self, spider.name, None)
        if custom_method is None:
            spider.logger.error(f'Cannot find custom process_item method for {spider.name}')
            return item
        return custom_method(item, spider)

    def banki_shares(self, item, spider):
        if item.is_valid():
            item.django_model.objects.update_or_create(
                isin=item['isin'],
                defaults=item,
            )
        else:
            spider.logger.error(f'Invalid item {item}')
        return item

    def banki_bonds(self, item, spider):
        if item.is_valid():
            item.django_model.objects.update_or_create(
                isin=item['isin'],
                defaults=item,
            )
        else:
            spider.logger.error(f'Invalid item {item}')
        return item
