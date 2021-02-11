import re

import scrapy
from common.scraper.items import BaseLoader
from common.scraper.utils import format_date, format_url
from finance.scraper.items import PersonItem
from scrapy.loader.processors import MapCompose


class Loader(BaseLoader):
    default_item_class = PersonItem

    photo_in = MapCompose(
        BaseLoader.default_input_processor,
        format_url,
        lambda x: x.replace('/resize_cache/', '/'),
        lambda x: x.replace('/260_260_1/', '/'),
    )
    position_in = MapCompose(
        lambda x: x.replace('<br>', '; '),
        lambda x: re.sub(r'<.+?>', '', x),
        BaseLoader.default_input_processor,
        lambda x: x.strip('; '),
        lambda x: x.replace(' ; ', '; '),
    )
    birthday_in = MapCompose(
        BaseLoader.default_input_processor,
        format_date,
    )
    about_in = MapCompose(
        BaseLoader.default_input_processor,
        lambda x: x.replace('<br>', '\n'),
        lambda x: re.sub(r'<.+?>', '', x),
        lambda x: x.replace('\n \n ', '\n\n'),
        lambda x: x.strip(),
    )


class Spider(scrapy.Spider):
    name = 'finparty_person'
    allowed_domains = ['finparty.ru']
    start_urls = ['https://finparty.ru/people/person/']

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, self.parse_links)

    def parse_links(self, response):
        pattern = r'/personal/[^/]+/'
        for link in response.css('a::attr(href)').re(pattern):
            yield response.follow(link, self.parse_items)
        next_page = response.css('.button__load-more::attr(data-src)').get()
        if next_page:
            yield response.follow(next_page, self.parse_links)

    def parse_items(self, response):
        loader = Loader(response=response)
        loader.add_value('url_self_finparty', response.url)
        loader.add_css('name', '.user-page h1::text')
        loader.add_css('photo', '.user-page img:first-child::attr(src)')
        loader.add_css('position', '.user-page h1 + p')
        loader.add_css('birthday', '.icon-birthday + span::text')
        loader.add_xpath(
            'about',
            '//h2[starts-with(normalize-space(text()), "Биография")]/following-sibling::div[1]/p/.',
        )
        yield loader.load_item()
