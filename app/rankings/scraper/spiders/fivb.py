import scrapy


class Spider(scrapy.Spider):
    name = 'fivb'
    allowed_domains = ['fivb.com', 'hypercube.nl']

    ranking_pk = None
    ranking_url = 'https://www.fivb.com/en/volleyball/rankings/seniorworldrankingmen'

    def start_requests(self):
        yield scrapy.Request(self.ranking_url)

    def parse(self, response):
        url = response.css('.content-box iframe::attr(src)').get()
        yield response.follow(url, self.parse_)

    def parse_(self, response):
        result = []
        for row_sel in response.css('tbody tr'):
            rank_elem = row_sel.css('td:nth-child(2)').get()
            if 'position"' in rank_elem:
                rank = 0
            elif 'position up' in rank_elem:
                rank = 1
            elif 'position down' in rank_elem:
                rank = -1
            result.append({
                'position': row_sel.css('td:nth-child(1) *::text').get(),
                'rank': rank,
                'name': row_sel.css('td:nth-child(4) *::text').get(),
                'country': row_sel.css('td:nth-child(4) *::text').get(),
            })
        yield {'result': result}
