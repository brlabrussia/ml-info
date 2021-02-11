import os

from common.scraper.settings import *

BOT_NAME = 'banks'
SPIDER_MODULES = ['banks.scraper.spiders']
NEWSPIDER_MODULE = 'banks.scraper.spiders'

ITEM_PIPELINES.update({
    'banks.scraper.pipelines.DjangoWriterPipeline': 800,
})
