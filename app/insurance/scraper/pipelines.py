class DjangoWriterPipeline:
    def process_item(self, item, spider):
        custom_method = getattr(self, spider.name, None)
        if custom_method is None:
            spider.logger.error(f'Cannot find custom process_item method for {spider.name}')
            return item
        return custom_method(item, spider)

    def banki_company(self, item, spider):
        if not item.is_valid():
            spider.logger.error(f'Invalid item {item}')
            return item
        try:
            qs = item.django_model.objects.filter(cbrn=item['cbrn'])
            if qs.count() > 1:
                qs = qs.filter(trademark=item['trademark']).exclude(trademark__exact='')
            obj = qs.get()
            if obj.trademark and (obj.trademark != item['trademark']):
                raise item.django_model.DoesNotExist
            licenses = item.pop('licenses')
            if not obj.licenses:
                obj.licenses = licenses
            for key, value in item.items():
                setattr(obj, key, value)
            obj.save()
        except item.django_model.DoesNotExist:
            item.save()
        return item

    def cbr_company(self, item, spider):
        if not item.is_valid():
            spider.logger.error(f'Invalid item {item}')
            return item
        qs = item.django_model.objects.filter(cbrn=item['cbrn'])
        if qs.exists():
            qs.update(**item)
        else:
            item.save()
        return item
