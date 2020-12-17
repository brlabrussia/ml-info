import os

import django

# Django integration
os.environ['DJANGO_SETTINGS_MODULE'] = 'core.settings'
django.setup()

BOT_NAME = 'common'
SPIDER_MODULES = None
NEWSPIDER_MODULE = None

LOG_LEVEL = 'INFO'

FEED_EXPORT_ENCODING = 'utf-8'
TELNETCONSOLE_ENABLED = False

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'

CONCURRENT_REQUESTS = 1
DOWNLOAD_DELAY = 0
DOWNLOAD_TIMEOUT = 30
DOWNLOAD_MAXSIZE = 20 * 1024 * 1024  # 20MB

SPIDER_MIDDLEWARES = {}
DOWNLOADER_MIDDLEWARES = {}
ITEM_PIPELINES = {}
EXTENSIONS = {}

if int(os.getenv('DEBUG', 0)):
    HTTPCACHE_ENABLED = True
    HTTPCACHE_DIR = 'httpcache'
    HTTPCACHE_EXPIRATION_SECS = 100 * 3600
    HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
