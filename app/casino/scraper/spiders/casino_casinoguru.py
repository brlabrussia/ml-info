import scrapy
from casino.scraper.items import CasinoItem
from common.scraper.items import BaseLoader
from common.scraper.utils import format_url
from scrapy.loader.processors import MapCompose


class Loader(BaseLoader):
    default_item_class = CasinoItem

    _ = \
        url_self_casinoguru_in = \
        images_logo_in = \
        MapCompose(
            BaseLoader.default_input_processor,
            format_url,
        )


class Spider(scrapy.Spider):
    name = 'casino_casinoguru'
    allowed_domains = ['casino.guru']
    custom_settings = {
        'CONCURRENT_REQUESTS': 1,
        'DOWNLOAD_DELAY': 0.5,
        'AUTOTHROTTLE_ENABLED': True,
        'AUTOTHROTTLE_START_DELAY': 5,
        'AUTOTHROTTLE_MAX_DELAY': 60,
        'AUTOTHROTTLE_TARGET_CONCURRENCY': 1.0,
    }

    def start_requests(self):
        yield scrapy.Request(
            'https://casino.guru/top-online-casinos',
            self.parse_items,
            cookies={'casinoTab': 'ALL'},
        )

    def parse_items(self, response):
        casino_items = response.css('.casino-card')
        for ci in casino_items:
            loader = Loader(response=response, selector=ci)
            loader.add_css('url_self_casinoguru', '.casino-card-heading a::attr(href)')
            loader.add_css('name', '.casino-card-heading a::text')
            loader.add_css('images_logo', '.casino-card-logo img.logo-wide::attr(src)')
            yield loader.load_item()
        next_page = response.css('.paging-right::attr(href)').get()
        if next_page:
            next_page = response.urljoin(next_page)
            yield response.request.replace(url=next_page)
