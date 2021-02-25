import scrapy
from banks.scraper.items import BankItem
from common.scraper.items import BaseLoader


class Loader(BaseLoader):
    default_item_class = BankItem


class Spider(scrapy.Spider):
    name = 'bank_banki'
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
        loader = Loader(response=response)
        loader.add_value('url_self_banki', response.url)
        loader.add_css('name', '[data-test=bankpage-header-bankname]::text')
        loader.add_css('reg_number', '[data-test=bankpage-header-banklicense]::text', re=r'(\d+(-\w+)?)')
        loader.add_css('ogrn', '[data-test=bankpage-header-ogrn]::text', re=r'\d{5,}')
        yield loader.load_item()
