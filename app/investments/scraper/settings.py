import os

from common.scraper.settings import *

BOT_NAME = 'investments'
SPIDER_MODULES = ['investments.scraper.spiders']
NEWSPIDER_MODULE = 'investments.scraper.spiders'

ITEM_PIPELINES.update({
    'investments.scraper.pipelines.DjangoWriterPipeline': 800,
})

if int(os.getenv('DEBUG', 0)):
    HTTPCACHE_ENABLED = False
