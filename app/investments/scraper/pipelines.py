class DjangoWriterPipeline:
    def process_item(self, item, spider):
        if item.is_valid():
            item.save()
        return item
