import os

from common.scraper.settings import *

BOT_NAME = 'insurance'
SPIDER_MODULES = ['insurance.scraper.spiders']
NEWSPIDER_MODULE = 'insurance.scraper.spiders'

ITEM_PIPELINES.update({
    'insurance.scraper.pipelines.DjangoWriterPipeline': 800,
})
