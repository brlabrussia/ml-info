import os

from common.scraper.settings import *

BOT_NAME = 'finance'
SPIDER_MODULES = ['finance.scraper.spiders']
NEWSPIDER_MODULE = 'finance.scraper.spiders'

ITEM_PIPELINES.update({
    'finance.scraper.pipelines.DjangoWriterPipeline': 800,
})
