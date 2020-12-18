from common.scraper.utils import drop_falsy, normalize_space
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst


class BaseLoader(ItemLoader):
    default_input_processor = MapCompose(
        normalize_space,
        drop_falsy,
    )
    default_output_processor = TakeFirst()
