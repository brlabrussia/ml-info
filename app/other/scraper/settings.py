from common.scraper.settings import *

BOT_NAME = 'other'
SPIDER_MODULES = ['other.scraper.spiders']
NEWSPIDER_MODULE = 'other.scraper.spiders'

ITEM_PIPELINES.update({
    'other.scraper.pipelines.DjangoWriterPipeline': 800,
})
