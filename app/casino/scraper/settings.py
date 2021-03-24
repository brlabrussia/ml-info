import os

from common.scraper.settings import *

BOT_NAME = 'casino'
SPIDER_MODULES = ['casino.scraper.spiders']
NEWSPIDER_MODULE = 'casino.scraper.spiders'

ITEM_PIPELINES.update({
    'casino.scraper.pipelines.DjangoWriterPipeline': 800,
})
