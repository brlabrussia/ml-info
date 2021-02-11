import csv

import dateparser
import scrapy
from banks.scraper.items import RatingItem
from common.scraper.items import BaseLoader
from common.scraper.utils import format_url
from scrapy.loader.processors import Compose, MapCompose


class Loader(BaseLoader):
    default_item_class = RatingItem
    _ = \
        url_self_banki_in = \
        url_bank_banki_in = \
        MapCompose(
            BaseLoader.default_input_processor,
            format_url,
        )


class Spider(scrapy.Spider):
    name = 'banki_rating'
    allowed_domains = ['banki.ru']
    start_urls = ['https://www.banki.ru/banks/']

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, self.parse_links)

    def parse_links(self, response):
        pattern = r'/banks/bank/[^/]+/'
        for link in response.css('a::attr(href)').re(pattern):
            yield response.follow(link, self.parse_id)
        next_page = response.css('.icon-arrow-right-16::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse_links)

    def parse_id(self, response):
        bank_id = response.css('script').re_first(r"var currentBankId = '(\d+?)';")
        if not bank_id:
            return
        url = f'https://www.banki.ru/banks/ratings/export.php?LANG=ru&BANK_ID={bank_id}'
        yield response.follow(
            url,
            self.parse_items,
            cb_kwargs={'url_bank_banki': response.url},
        )

    def parse_items(self, response, url_bank_banki):
        loader = Loader(response=response)
        loader.add_value(
            'url_self_banki',
            response.url.replace('export.php?LANG=ru&', '?'),
        )
        loader.add_value('url_bank_banki', url_bank_banki)
        dates = (
            str(dateparser.parse('1 month ago').strftime('%Y-%m-01')),
            str(dateparser.parse('2 month ago').strftime('%Y-%m-01')),
        )
        proc = Compose(
            lambda x: x.replace(',', '.'),
            lambda x: x.replace(' ', ''),
            lambda x: x.replace('−', '-'),
            lambda x: float(x) if x not in ('н/д', '-') else None,
        )
        response_processed = {
            row[4]: {
                dates[0]: proc(row[5]),
                dates[1]: proc(row[6]),
            }
            for row in csv.reader(response.text.splitlines(), delimiter=';')
            if len(row) >= 7 and row[4]
        }
        for field in RatingItem.django_model._meta.fields:
            if field.help_text:
                loader.add_value(
                    field.name,
                    response_processed.get(field.help_text, None),
                )
        yield loader.load_item()
