import scrapy


class Spider(scrapy.Spider):
    name = 'fifa'
    allowed_domains = ['fifa.com']

    ranking_pk = None
    ranking_url = 'https://www.fifa.com/fifa-world-ranking/ranking-table/men/'
    table_name = None

    def start_requests(self):
        yield scrapy.Request(self.ranking_url)

    def parse(self, response):
        result = []
        for row_sel in response.css('tbody tr'):
            federation = row_sel.css('td:nth-child(7) span::text').get()
            if self.table_name and f'#{self.table_name}#' != federation:
                continue
            rank_elem = row_sel.css('td:nth-child(6)').get()
            if '#icon-equal' in rank_elem:
                rank = 0
            elif '#icon-rise' in rank_elem:
                rank = 1
            elif '#icon-fall' in rank_elem:
                rank = -1
            result.append({
                'position': row_sel.css('td:nth-child(1) *::text').get(),
                'rank': rank,
                'name': row_sel.css('td:nth-child(2) span.fi-t__nText::text').get(),
                'country': row_sel.css('td:nth-child(2) span.fi-t__nText::text').get(),
            })
        yield {'result': result}
