import scrapy


class Spider(scrapy.Spider):
    name = 'ufc'
    allowed_domains = ['bsrussia.com']

    ranking_pk = None
    ranking_url = 'https://ru.ufc.com/rankings'
    table_name = 'Женский наилегчайший вес'

    def start_requests(self):
        yield scrapy.Request(self.ranking_url)

    def parse(self, response):
        xp = f'//*[@class="info"]/h4[normalize-space(text())="{self.table_name}"]/ancestor::table'
        table_sel = response.xpath(xp)
        result = []
        for row_sel in table_sel.css('tbody tr'):
            rank_elem = row_sel.css('td:nth-child(3)').get()
            if 'rank-increase' in rank_elem:
                rank = 1
            elif 'rank-decrease' in rank_elem:
                rank = -1
            else:
                rank = 0
            result.append({
                'position': row_sel.css('td:nth-child(1) *::text').get().strip(),
                'rank': rank,
                'name': row_sel.css('td:nth-child(2) a::text').get(),
            })
        yield {'result': result}
