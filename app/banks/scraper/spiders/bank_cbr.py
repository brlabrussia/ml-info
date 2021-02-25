from urllib.parse import unquote

import scrapy
from banks.scraper.items import BankItem
from common.scraper.items import BaseLoader
from common.scraper.utils import format_date
from scrapy.loader.processors import Identity, Join, MapCompose


class Loader(BaseLoader):
    default_item_class = BankItem

    registration_date_in = MapCompose(format_date)
    ogrn_date_in = MapCompose(format_date)
    tel_number_in = MapCompose(
        BaseLoader.default_input_processor,
        lambda x: x.split(', '),
    )
    tel_number_out = Identity()
    statutory_update_in = MapCompose(format_date)
    authorized_capital_in = MapCompose(
        BaseLoader.default_input_processor,
        lambda x: x if not x else int(x.replace(' ', '')),
    )
    authorized_capital_date_in = MapCompose(format_date)
    license_info_in = MapCompose(
        BaseLoader.default_input_processor,
        lambda x: x if x else None,
    )
    license_info_out = Identity()
    license_info_file_in = MapCompose(
        BaseLoader.default_input_processor,
        lambda x: ('http://cbr.ru' + x) if x.startswith('/') else x,
    )
    deposit_insurance_system_in = MapCompose(
        BaseLoader.default_input_processor,
        lambda x: True if x == 'Да' else (False if x == 'Нет' else None),
    )

    bank_subsidiaries_out = Join(', ')
    bank_agencies_in = MapCompose(int)
    additional_offices_in = MapCompose(int)
    operating_cash_desks_in = MapCompose(int)
    operating_offices_in = MapCompose(int)
    mobile_cash_desks_in = MapCompose(int)

    info_sites_in = MapCompose(unquote)
    info_sites_out = Identity()
    cards_in = cards_out = Identity()
    subsidiaries_in = subsidiaries_out = Identity()
    agencies_in = agencies_out = Identity()


class Spider(scrapy.Spider):
    name = 'bank_cbr'
    allowed_domains = ['cbr.ru']

    def start_requests(self):
        url = 'http://cbr.ru/banking_sector/credit/FullCoList/'
        yield scrapy.Request(url, self.parse_links)

    def parse_links(self, response):
        for link in response.css('td a::attr(href)'):
            yield response.follow(link, self.parse_items)

    def parse_items(self, response):
        loader = Loader(response=response)

        xp = '//*[has-class("coinfo_item_title")][starts-with(normalize-space(text()), "{}")]/following-sibling::div[has-class("coinfo_item_text")][1]/text()'
        loader.add_value('url_self_cbr', response.url)
        loader.add_xpath('full_name', xp.format('Полное фирменное наименование'))
        loader.add_xpath('name', xp.format('Сокращённое фирменное наименование'))
        loader.add_xpath('reg_number', xp.format('Регистрационный номер'))
        loader.add_xpath('registration_date', xp.format('Дата регистрации Банком России'))
        loader.add_xpath('ogrn', xp.format('Основной государственный регистрационный номер'), re=r'\d{5,}')
        loader.add_xpath('ogrn_date', xp.format('Основной государственный регистрационный номер'), re=r'\d{2}\.\d{2}\.\d{4}')
        loader.add_xpath('bik', xp.format('БИК'))
        loader.add_xpath('statutory_address', xp.format('Адрес из устава'))
        loader.add_xpath('actual_address', xp.format('Адрес фактический'))
        loader.add_xpath('tel_number', xp.format('Телефон'))
        loader.add_xpath('statutory_update', xp.format('Устав'), re=r'\d{2}\.\d{2}\.\d{4}')
        loader.add_xpath('authorized_capital', xp.format('Уставный капитал'), re=r'^[\d\s]*')
        loader.add_xpath('authorized_capital_date', xp.format('Уставный капитал'), re=r'\d{2}\.\d{2}\.\d{4}')
        loader.add_xpath('license_info', xp.format('Лицензия (дата выдачи/последней замены)'))
        loader.add_xpath('license_info', xp.format('Лицензия (дата выдачи/последней замены)').replace('/text()', '/*/text()'))
        loader.add_xpath('license_info_file', xp.format('Лицензия (дата выдачи/последней замены)').replace('/text()', '/p/a/@href'))
        loader.add_xpath('deposit_insurance_system', xp.format('Участие в системе страхования вкладов'))
        loader.add_xpath('english_name', xp.format('Фирменное наименование на английском языке'))

        xp = '//h4[starts-with(normalize-space(text()), "Подразделения кредитной организации")]/following-sibling::div[1]//td[starts-with(normalize-space(text()), "{}")]/following-sibling::td[1]/text()'
        loader.add_xpath('bank_subsidiaries', xp.format('Филиалы'))
        loader.add_xpath('bank_agencies', xp.format('Представительства'), re=r'\d+')
        loader.add_xpath('additional_offices', xp.format('Дополнительные офисы'), re=r'\d+')
        loader.add_xpath('operating_cash_desks', xp.format('Операционные кассы вне кассового узла'), re=r'\d+')
        loader.add_xpath('operating_offices', xp.format('Операционные офисы'), re=r'\d+')
        loader.add_xpath('mobile_cash_desks', xp.format('Передвижные пункты кассовых операций'), re=r'\d+')

        loader.add_css('info_sites', '.org_info ._links a::attr(href)')
        loader.add_value('cards', self.extract_cards(response))
        loader.add_value('subsidiaries', self.extract_subsidiaries(response))
        loader.add_value('agencies', self.extract_agencies(response))

        yield loader.load_item()

    @staticmethod
    def extract_cards(response):
        ret = []
        for row_sel in response.css('.cards table tr'):
            data_sels = row_sel.css('td')
            if len(data_sels) != 3:
                continue
            ret.append({
                'pay_system': data_sels[0].css('::text').get(),
                'emission': True if 'black_dot' in data_sels[1].get() else False,
                'acquiring': True if 'black_dot' in data_sels[2].get() else False,
            })
        return ret

    @staticmethod
    def extract_subsidiaries(response):
        ret = []
        table_sel = response.xpath('//h2[starts-with(normalize-space(text()), "Филиалы")]/following-sibling::div[1]//table')
        for row_sel in table_sel.css('tr'):
            data_sels = row_sel.css('td')
            if len(data_sels) != 4:
                continue
            ret.append({
                'reg_number': data_sels[0].css('::text').get(),
                'name': data_sels[1].css('::text').get(),
                'reg_date': format_date(data_sels[2].css('::text').get()),
                'address': data_sels[3].css('::text').get(),
            })
        return ret

    @staticmethod
    def extract_agencies(response):
        ret = []
        table_sel = response.xpath('//h2[starts-with(normalize-space(text()), "Представительства")]/following-sibling::div[1]//table')
        for row_sel in table_sel.css('tr'):
            data_sels = row_sel.css('td')
            if len(data_sels) != 4:
                continue
            ret.append({
                'name': data_sels[1].css('::text').get(),
                'foundation_date': format_date(data_sels[2].css('::text').get()),
                'address': data_sels[3].css('::text').get(),
            })
        return ret
