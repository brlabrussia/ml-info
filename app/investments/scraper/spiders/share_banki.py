import json
from html import unescape

import scrapy
from common.scraper.items import BaseLoader
from common.scraper.utils import normalize_space
from investments.scraper.items import ShareItem
from scrapy.loader.processors import Identity, MapCompose


class Loader(BaseLoader):
    default_item_class = ShareItem
    seo_quote_in = MapCompose(
        lambda x: x if '%' in x else None,
    )
    seo_quote_out = Identity()


class Spider(scrapy.Spider):
    name = 'share_banki'
    allowed_domains = ['banki.ru']
    start_urls = ['https://www.banki.ru/investment/search/share/?page=1']

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(
                url,
                self.parse_links,
                dont_filter=True,
            )

    def parse_links(self, response):
        bundle_sel = response.css('div[data-module*="/InvestmentBundle/ui-2018/investment"]')
        if not bundle_sel:
            self.logger.error(f'bundle_sel not found on {response.url}')
            return
        bundle_options = bundle_sel.css('::attr(data-module-options)').get()
        bundle_options = json.loads(unescape(bundle_options))
        for share in bundle_options['pageInfo']['shares']:
            yield response.follow(
                share['card_url'],
                self.parse_items,
                cb_kwargs={'share': share},
            )

        current_page = bundle_options['pageInfo']['pagination']['currentPageNumber']
        current_page = int(current_page)
        total_shares = bundle_options['pageInfo']['pagination']['totalCount']
        total_shares = int(total_shares)
        if current_page < int(total_shares / 10):
            next_page = current_page + 1
            url = response.url.split('?')[0] + f'?page={next_page}'
            yield response.follow(url, self.parse_links)

    def parse_items(self, response, share):
        loader = Loader(response=response)
        loader.add_value('isin', share['isin'])
        loader.add_value('name', share['name'])
        loader.add_value('logo', share['logo'])
        loader.add_value('price', share['price_current'])
        loader.add_value('price_dynamic', self.extract_price_dynamic(response))
        loader.add_value('dividend_history', self.extract_dividend_history(response))
        loader.add_xpath('seo_quote', '//*[@data-test="seo-block-title"][starts-with(normalize-space(text()), "Котировки акций")]/..//p/text()')
        yield loader.load_item()

    @staticmethod
    def extract_price_dynamic(response):
        ret = {}
        for row_sel in response.css('.dynamics-of-shares__changes tr'):
            tds = row_sel.css('td::text').getall()
            tds = [normalize_space(td) for td in tds]
            ret[tds[0]] = tds[1:]
        return ret

    @staticmethod
    def extract_dividend_history(response):
        rex = r'(?s)/components/share/dividend-history.*Chart\((.*?)\);'
        try:
            return {
                item['year']: (
                    str(item['dividend']) + '%'
                    if item['dividend']
                    else None
                )
                for item in json.loads(response.css('script').re_first(rex))
            }
        except Exception:
            return None
