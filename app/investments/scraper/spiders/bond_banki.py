import json
from html import unescape

import scrapy
from common.scraper.items import BaseLoader
from investments.scraper.items import BondItem


class Loader(BaseLoader):
    default_item_class = BondItem


class Spider(scrapy.Spider):
    name = 'bond_banki'
    allowed_domains = ['banki.ru']
    start_urls = ['https://www.banki.ru/investment/search/']

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, self.parse_links)

    def parse_links(self, response):
        bundle_sel = response.css('div[data-module*="/InvestmentBundle/ui-2018/investment"]')
        if not bundle_sel:
            self.logger.error(f'bundle_sel not found on {response.url}')
            return
        bundle_options = bundle_sel.css('::attr(data-module-options)').get()
        bundle_options = json.loads(unescape(bundle_options))
        for bond in bundle_options['pageInfo']['bonds']:
            loader = Loader(response=response)
            loader.add_value('isin', bond['isin'])
            loader.add_value('name', bond['name'])
            loader.add_value('issuer', bond['issuer']['name'])
            loader.add_value('logo', bond['logo'])
            loader.add_value('price', bond['price_current'])
            loader.add_value('risk', bond['risk'])
            loader.add_value('maturity_yield', bond['yield_maturity'])
            loader.add_value('maturity_date', bond['end_mty_date'])
            loader.add_value('offer_yield', bond['yield_offer'])
            loader.add_value('offer_date', bond['offer_date'])
            loader.add_value('coupon_yield', bond['coupon_rate'])
            loader.add_value('coupon_date', bond['coupon_date'])
            yield loader.load_item()

        current_page = bundle_options['pageInfo']['pagination']['currentPageNumber']
        current_page = int(current_page)
        total_bonds = bundle_options['pageInfo']['pagination']['totalCount']
        total_bonds = int(total_bonds)
        if current_page < int(total_bonds / 10):
            next_page = current_page + 1
            url = response.url.split('?')[0] + f'?page={next_page}'
            yield response.follow(url, self.parse_links)
