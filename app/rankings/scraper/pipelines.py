from rankings.models import Ranking


class DjangoWriterPipeline:
    def process_item(self, item, spider):
        custom_method = getattr(self, spider.name, None)
        if custom_method is None:
            spider.logger.error(f'Cannot find custom process_item method for {spider.name}')
            return item
        return custom_method(item, spider)

    def fifa(self, item, spider):
        ranking = Ranking.objects.get(pk=spider.ranking_pk)
        ranking.result = item['result']
        ranking.save()
        return item

    def fivb(self, item, spider):
        ranking = Ranking.objects.get(pk=spider.ranking_pk)
        ranking.result = item['result']
        ranking.save()
        return item

    def ufc(self, item, spider):
        ranking = Ranking.objects.get(pk=spider.ranking_pk)
        ranking.result = item['result']
        ranking.save()
        return item
