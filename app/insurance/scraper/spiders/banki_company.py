import scrapy
from common.scraper.items import BaseLoader
from common.scraper.utils import format_date, format_url, normalize_space
from insurance.scraper.items import CompanyItem
from scrapy.loader.processors import Identity, MapCompose


class Loader(BaseLoader):
    default_item_class = CompanyItem

    logo_in = MapCompose(format_url)
    licenses_out = Identity()
    director_date_in = MapCompose(format_date)

    _ = \
        authorized_capital_in = \
        net_profit_in = \
        premiums_in = \
        payouts_in = \
        MapCompose(
            lambda x: x.replace(' ', ''),
            int,
        )


class Spider(scrapy.Spider):
    name = 'banki_company'
    allowed_domains = ['banki.ru']
    start_urls = ['https://www.banki.ru/insurance/companies/']

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, self.parse_links)

    def parse_links(self, response):
        for link in response.css('[data-test=company-name]::attr(href)'):
            yield response.follow(link, self.parse_items)

        pagination_sel = response.css('[data-module$=pagination]::attr(data-options)')
        current_page = int(pagination_sel.re_first(r'currentPageNumber: (\d+);'))
        items_per_page = int(pagination_sel.re_first(r'itemsPerPage: (\d+);'))
        total_items = int(pagination_sel.re_first(r'totalItems: (\d+);'))
        if (current_page * items_per_page) < total_items:
            next_page = current_page + 1
            url = response.url.split('?')[0] + f'?page={next_page}'
            yield response.follow(url, self.parse_links)

    def parse_items(self, response):
        loader = Loader(response=response)
        loader.add_css('cbrn', '[data-test=reference-information]', re=r'лицензия.*№\s*(\d+)')
        loader.add_css('cbrn', '[data-test=company-licenses]', re=r'№\s*(\d+)\s*от')
        loader.add_css('trademark', '.bread-crumbs__item:last-child span::text')
        loader.add_css('logo', '[data-test=company-header-logo]::attr(style)', re=r'url\((.+)\)')
        loader.add_value('licenses', self.extract_licenses(response))
        xp = (
            '//*[has-class("company-properties--title")]'
            '[starts-with(normalize-space(text()), "{}")]'
            '/following-sibling::*[has-class("company-properties--amount")]'
            '/text()'
        )
        loader.add_xpath('authorized_capital', xp.format('Уставный капитал'), re=r'[\d\s]+')
        loader.add_xpath('net_profit', xp.format('Чистая прибыль'), re=r'[\d\s]+')
        loader.add_xpath('premiums', xp.format('Объем премий'), re=r'[\d\s]+')
        loader.add_xpath('payouts', xp.format('Объем выплат'), re=r'[\d\s]+')
        xp = '//dl[has-class("definition-list")]/dt[text()="{}"]/following-sibling::dd[1]{}'
        loader.add_xpath('director', xp.format('Руководитель', '/text()'))
        loader.add_xpath('director_date', xp.format('Руководитель', '/div/text()'), re=r'по информации на\s*(.+ г\.)')
        yield loader.load_item()

    @staticmethod
    def extract_licenses(response):
        ret = []
        table_sel = response.css('[data-test=company-licenses] table')
        for row_sel in table_sel.css('tbody tr'):
            ret.append({
                'number': row_sel.re_first(r'\w+\s*№\s*\d+'),
                'date': row_sel.re_first(r'от (\d{2}\.\d{2}\.\d{4})'),
                'status': row_sel.css('td:nth-child(2) span::text').re_first(r'\w+'),
                'type': None,
                'subtypes': None,
                'comment': row_sel.css('td:nth-child(3) p::text').get(),
            })
        return ret
