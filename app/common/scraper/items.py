from common.scraper.utils import drop_blank, normalize_space
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst


class BaseLoader(ItemLoader):
    default_input_processor = MapCompose(
        normalize_space,
        drop_blank,
    )
    default_output_processor = TakeFirst()
