import scrapy
from casino.scraper.items import SlotItem
from common.scraper.items import BaseLoader
from common.scraper.utils import format_url
from scrapy.loader.processors import Identity, MapCompose


class Loader(BaseLoader):
    default_item_class = SlotItem

    _ = \
        url_self_casinoguru_in = \
        iframe_original_in = \
        iframe_fallback_in = \
        images_logo_in = \
        MapCompose(
            BaseLoader.default_input_processor,
            format_url,
        )

    _ = \
        images_content_out = \
        videos_out = \
        Identity()


class Spider(scrapy.Spider):
    name = 'slot_casinoguru'
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
        url = 'https://casino.guru/free-casino-games/new'
        yield scrapy.Request(url, self.parse_links)

    def parse_links(self, response):
        slot_items = response.css('.game-item')
        for si in slot_items:
            url = si.css('a.game-item-img::attr(href)').get()
            yield scrapy.Request(url, self.parse_items)
        next_page = response.css('.paging-right::attr(href)').get()
        if next_page:
            next_page = response.urljoin(next_page)
            yield response.request.replace(url=next_page)

    def parse_items(self, response):
        loader = Loader(response=response)
        loader.add_value('url_self_casinoguru', response.url)
        loader.add_css('name', '.game-detail-main-overview h2::text')
        loader.add_css('iframe_original', '#game_link::attr(data-url)')
        loader.add_css('iframe_fallback', '#game_link::attr(data-fallback-url)')
        loader.add_css('images_logo', '.game-detail-main-info img::attr(data-src)')
        loader.add_css('images_content', '.section-game-review .games-content-image img::attr(data-src)')
        loader.add_css('videos', '.video-wrapper iframe::attr(data-src)')
        yield loader.load_item()
