import re
from urllib.parse import unquote
import json

import scrapy
from common.scraper.items import BaseLoader
from furl import furl
from other.scraper.items import ItunesAppItem
from scrapy.loader.processors import Identity, MapCompose


class Loader(BaseLoader):
    default_item_class = ItunesAppItem
    url_in = MapCompose(unquote)
    _ = \
        screenshots_out = \
        version_history_out = \
        Identity()


class Spider(scrapy.Spider):
    name = 'apple_itunesapp'
    allowed_domains = ['apps.apple.com']
    custom_settings = {'DOWNLOAD_DELAY': 4}
    auth_token = None
    start_urls = [
        'https://apps.apple.com/ru/app/id1166619854',
        'https://apps.apple.com/ru/app/id1065803457',
        'https://apps.apple.com/ru/app/id1177395683',
        'https://apps.apple.com/ru/app/id1392323505',
        'https://apps.apple.com/ru/app/id1127251682',
        'https://apps.apple.com/ru/app/id1491142951',
        'https://apps.apple.com/ru/app/id1259203065',
        'https://apps.apple.com/ru/app/id1378876484',
        'https://apps.apple.com/ru/app/id1296163413',
        'https://apps.apple.com/ru/app/id1492307356',
        'https://apps.apple.com/ru/app/id1485980763',
        'https://apps.apple.com/ru/app/id1294769808',
        'https://apps.apple.com/ru/app/id1310600465',
        'https://apps.apple.com/ru/app/id1469527336',
        'https://apps.apple.com/ru/app/id1455333246',
        'https://apps.apple.com/ru/app/id1475084805',
        'https://apps.apple.com/ru/app/id1525533461',
        'https://apps.apple.com/ru/app/id1531690217',
        'https://apps.apple.com/ru/app/id1121573745',
        'https://apps.apple.com/ru/app/id579961527',
        'https://apps.apple.com/ru/app/id1523615263',
        'https://apps.apple.com/kz/app/id1460134358',
        'https://apps.apple.com/kz/app/id1496975315',
        'https://apps.apple.com/by/app/id731960907',
        'https://apps.apple.com/gb/app/id805599513',
        'https://apps.apple.com/gb/app/id465712788',
        'https://apps.apple.com/gb/app/id519684662',
    ]
    start_keywords = [
        'ставки',
        'букмекер',
        'бет',
    ]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, self.parse_links)
        for keyword in self.start_keywords:
            yield scrapy.Request(
                f'https://www.apple.com/ru/search/{keyword}?src=serp',
                self.parse_search_results,
            )

    def parse_search_results(self, response):
        for a in response.css('.as-links-name.more::attr(href)'):
            yield response.follow(a, self.parse_links)

    def parse_links(self, response):
        if self.auth_token is None:
            self.auth_token = self.get_auth_token(response)
        if not self.auth_token:
            return
        url = response.request.url
        xhr_url = self.get_xhr_url(url)
        if not xhr_url:
            return
        yield response.follow(
            url=xhr_url,
            headers={'authorization': f'Bearer {self.auth_token}'},
            callback=self.parse_items,
        )

    def parse_items(self, response):
        response_json = json.loads(response.body)
        attrs = response_json['data'][0]['attributes']
        attrs_ios = attrs['platformAttributes']['ios']
        loader = Loader()
        loader.add_value('url', attrs.get('url'))
        loader.add_value('name', attrs.get('name'))
        loader.add_value('subtitle', attrs_ios.get('subtitle'))
        loader.add_value('description', attrs_ios['description']['standard'])
        loader.add_value('logo', self.get_image_url(attrs_ios.get('artwork')))
        loader.add_value('screenshots', self.extract_screenshots(attrs_ios.get('screenshotsByType', {})))
        loader.add_value('version_history', self.extract_version_history(attrs_ios.get('versionHistory', [])))
        loader.add_value('rating', attrs['userRating']['value'])
        loader.add_value('provider', attrs_ios.get('seller'))
        loader.add_value('size', attrs['fileSizeByDevice']['universal'])
        loader.add_value('category', attrs.get('genreDisplayName'))
        loader.add_value('compatibility', attrs_ios.get('requirementsString'))
        yield loader.load_item()

    def extract_screenshots(self, obj):
        api_screenshots = obj.get('ipadPro') or list(obj.values())[0] or []
        return [self.get_image_url(o) for o in api_screenshots]

    def extract_version_history(self, obj):
        return [self.get_version(o) for o in obj]

    @staticmethod
    def get_image_url(obj):
        if obj is None:
            return None
        return obj['url'] \
            .replace('{w}', str(obj['width'])) \
            .replace('{h}', str(obj['height'])) \
            .replace('{c}.{f}', '.png')

    @staticmethod
    def get_version(obj):
        return {
            'version': obj['versionDisplay'],
            'date': obj['releaseDate'],
            'notes': obj['releaseNotes'] or '',
        }

    @staticmethod
    def get_auth_token(response):
        css = 'meta[name="web-experience-app/config/environment"]::attr(content)'
        meta = response.css(css).get()
        try:
            meta = json.loads(unquote(meta))
            auth_token = meta['MEDIA_API']['token']
            return auth_token
        except (TypeError, KeyError):
            return False

    @staticmethod
    def get_xhr_url(url):
        try:
            lang = re.search(r'apple\.com/(\w+)/', url).group(1)
            app_id = re.search(r'/id(\d+)/?$', url).group(1)
        except AttributeError:
            return False
        f = furl(
            url=f'https://amp-api.apps.apple.com/v1/catalog/{lang}/apps/{app_id}',
            query={
                'platform': 'web',
                'additionalPlatforms': 'appletv,ipad,iphone,mac',
                'extend': (
                    'description,developerInfo,distributionKind,editorialVideo,fileSizeByDevice'
                    ',messagesScreenshots,privacy,privacyPolicyUrl,privacyPolicyText,promotionalText'
                    ',screenshotsByType,supportURLForLanguage,versionHistory,videoPreviewsByType,websiteUrl'
                ),
            },
        )
        return f.url
