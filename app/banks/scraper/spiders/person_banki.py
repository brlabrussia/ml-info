import scrapy
from common.scraper.items import BaseLoader
from common.scraper.utils import format_url
from finance.scraper.items import PersonItem
from scrapy.loader.processors import MapCompose


class Loader(BaseLoader):
    default_item_class = PersonItem
    _ = \
        url_self_finparty_in = \
        url_bank_banki = \
        MapCompose(
            BaseLoader.default_input_processor,
            format_url,
        )


class Spider(scrapy.Spider):
    name = 'person_banki'
    allowed_domains = ['banki.ru']
    start_urls = ['https://www.banki.ru/banks/']

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, self.parse_links)

    def parse_links(self, response):
        pattern = r'/banks/bank/[^/]+/'
        for link in response.css('a::attr(href)').re(pattern):
            yield response.follow(link, self.parse_items)
        next_page = response.css('.icon-arrow-right-16::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse_links)

    def parse_items(self, response):
        urls = response.css('html').re(r'support__name[^>]+href="([^"]+)"')
        for url in urls:
            loader = Loader(response=response)
            loader.add_value('url_self_finparty', url)
            loader.add_value('url_bank_banki', response.url)
            yield loader.load_item()
