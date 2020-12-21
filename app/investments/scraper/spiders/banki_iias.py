import scrapy
from common.scraper.items import BaseLoader
from common.scraper.utils import normalize_space
from investments.scraper.items import IIAItem
from scrapy.loader.processors import MapCompose, Identity


class Loader(BaseLoader):
    default_item_class = IIAItem

    investment_min_in = MapCompose(
        BaseLoader.default_input_processor,
        lambda x: x.replace(' ', ''),
        int,
    )
    yield_value_in = MapCompose(
        BaseLoader.default_input_processor,
        lambda x: x.replace(',', '.'),
        float,
    )
    fees_out = Identity()


class Spider(scrapy.Spider):
    name = 'banki_iias'
    allowed_domains = ['banki.ru']
    start_urls = ['https://www.banki.ru/investment/iia_products/']

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, self.parse_sections)

    def parse_sections(self, response):
        for link in response.css('.switcher__button::attr(href)').getall():
            yield response.follow(link, self.parse_links)

    def parse_links(self, response):
        filter_ = response.css('.switcher__button--active::text').get()
        for item_sel in response.css('.specials__item'):
            logo = item_sel.css('.item__header img::attr(data-src)').get()
            link = item_sel.css('.item__footer [data-test=more] a::attr(href)').get()
            yield response.follow(
                link,
                self.parse_items,
                cb_kwargs={
                    'filter_': filter_,
                    'logo': logo,
                },
            )

    def parse_items(self, response, filter_, logo):
        loader = Loader(response=response)
        loader.add_css('name', '.bread-crumbs__item:last-child span::text')
        loader.add_css('company', '.bread-crumbs__item:nth-last-child(3) span::text')
        loader.add_value('logo', logo)
        loader.add_value('filter', filter_)
        loader.add_xpath('investment_min', '//*[starts-with(normalize-space(text()), "Минимальная сумма")]/following-sibling::*[has-class("header-h2")]/text()', re=r'[\d\s]+')
        loader.add_css('yield_type', '[data-test=info] .flexbox__item .font-size-medium::text')
        loader.add_css('yield_value', '[data-test=info] .flexbox__item .header-h2::text', re=r'[\d\,]+')
        loader.add_value('yield_block', self.extract_yield_block(response))
        loader.add_xpath('fees', '//*[starts-with(normalize-space(text()), "Комиссии")]/following-sibling::ul/li/text()')
        loader.add_value('docs', self.extract_docs(response))
        yield loader.load_item()

    @staticmethod
    def extract_yield_block(response):
        ret = {}
        for header_sel in response.xpath('//*[has-class("ui-columns__column")][1]//div[normalize-space(text())]'):
            key = header_sel.xpath('./text()').get()
            if 'доходность' not in key.lower():
                continue
            values = header_sel.xpath('./following-sibling::ul[1]/li/text()').getall()
            values = [(normalize_space(v) or '') for v in values]
            ret[key] = values
        return ret

    @staticmethod
    def extract_docs(response):
        ret = {}
        for a_sel in response.xpath('//a[.//*[@data-test="pdf-link"]]'):
            value = a_sel.xpath('./@href').get()
            key = a_sel.xpath('.//*[@data-test="pdf-link"]/text()').get()
            ret[key] = value
        return ret
