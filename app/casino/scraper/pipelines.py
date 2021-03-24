class DjangoWriterPipeline:
    def process_item(self, item, spider):
        custom_method = getattr(self, spider.name, None)
        if custom_method is None:
            spider.logger.error(f'Cannot find custom process_item method for {spider.name}')
            return item
        return custom_method(item, spider)

    def casino_casinoguru(self, item, spider):
        if item.is_valid():
            item.django_model.objects.update_or_create(
                url_self_casinoguru=item['url_self_casinoguru'],
                defaults=item,
            )
        else:
            spider.logger.error(f'Invalid item\n{item.errors}')
        return item

    def slot_casinoguru(self, item, spider):
        if item.is_valid():
            item.django_model.objects.update_or_create(
                url_self_casinoguru=item['url_self_casinoguru'],
                defaults=item,
            )
        else:
            spider.logger.error(f'Invalid item\n{item.errors}')
        return item
