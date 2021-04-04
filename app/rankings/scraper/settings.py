import os

from common.scraper.settings import *

BOT_NAME = 'rankings'
SPIDER_MODULES = ['rankings.scraper.spiders']
NEWSPIDER_MODULE = 'rankings.scraper.spiders'

ITEM_PIPELINES.update({
    'rankings.scraper.pipelines.DjangoWriterPipeline': 800,
})
