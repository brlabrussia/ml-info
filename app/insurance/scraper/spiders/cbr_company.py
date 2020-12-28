import io

import openpyxl
import scrapy
from common.scraper.items import BaseLoader
from insurance.scraper.items import CompanyItem
from scrapy.loader.processors import Identity


class Loader(BaseLoader):
    default_item_class = CompanyItem

    licenses_out = Identity()


class Spider(scrapy.Spider):
    name = 'cbr_company'
    allowed_domains = ['cbr.ru']
    start_urls = ['https://www.cbr.ru/vfs/finmarkets/files/supervision/list_ssd.xlsx']

    def parse(self, response):
        workbook = openpyxl.load_workbook(io.BytesIO(response.body))
        loader = None
        license_rows = []
        for row in workbook.active.iter_rows(min_row=5, values_only=True):
            if not any(row):
                continue
            elif row[0]:
                if loader:
                    loader.add_value('licenses', self.extract_licenses(license_rows))
                    yield loader.load_item()
                    license_rows.clear()
                loader = Loader()
                loader.add_value('cbrn', row[2])
                loader.add_value('inn', row[7])
                loader.add_value('ogrn', row[8])
                loader.add_value('name', row[3])
                loader.add_value('address', row[4])
                loader.add_value('federal_subject', row[0])
                loader.add_value('contacts', row[6])
            license_rows.append(row[-5:])
        else:
            loader.add_value('licenses', self.extract_licenses(license_rows))
            yield loader.load_item()

    @staticmethod
    def extract_licenses(rows):
        ret = []
        license = None
        for row in rows:
            if not any(row):
                continue
            if row[0]:
                if license:
                    ret.append(license)
                license = {
                    'number': row[0],
                    'date': row[1],
                    'status': row[2],
                    'type': row[3],
                    'subtypes': [row[4]],
                    'comment': None,
                }
            elif row[4]:
                license['subtypes'].append(row[4])
        if license:
            ret.append(license)
        return ret
