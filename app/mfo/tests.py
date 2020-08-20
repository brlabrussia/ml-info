import json

from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from .models import Lender


class CbrTestCase(APITestCase):
    endpoint = '/mfo/scrapers/cbr/'
    sample_list = [
        {
            'scraped_from': [
                'https://www.cbr.ru/vfs/finmarkets/files/supervision/list_MFO.xlsx',
            ],
            'cbrn': '1904012009226',
            'cbr_created_at': '2019-04-17T00:00:00+03:00',
            'type': 'Микрокредитная компания',
            'ogrn': '1173025007902',
            'inn': '3015111990',
            'name_full': 'Общество с ограниченной ответственностью Микрокредитная Компания «Ламэль»',
            'name_short': 'ООО МКК «Ламэль»',
            'address': '414004, Астраханская область, г. Астрахань, ул. Валерии Барсовой, д. 2, кв. 7',
            'website': 'http://www.astfin.ru',
            'email': 'ssg-buh@mail.ru',
        },
        {
            'scraped_from': [
                'https://www.cbr.ru/vfs/finmarkets/files/supervision/list_MFO.xlsx',
            ],
            'cbrn': '1903111009224',
            'cbr_created_at': '2019-04-17T00:00:00+03:00',
            'type': 'Микрокредитная компания',
            'ogrn': '1192901002678',
            'inn': '2903012586',
            'name_full': 'Общество с ограниченной ответственностью «Микрокредитная компания «Еврик»',
            'name_short': 'ООО «МКК «Еврик»',
            'address': '164901, Архангельская область, г. Новодвинск, ул. 3-й Пятилетки, д. 21, кв. 2',
            'email': 'ooomkkevrik@yandex.ru',
        },
    ]

    def test_create_item(self):
        """
        Ensure we can create single Lender object from valid data.
        """
        item = self.sample_list[0].copy()
        response = self.client.post(self.endpoint, item)
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        self.assertEqual(Lender.objects.get().ogrn, item['ogrn'])

    def test_update_item(self):
        """
        Ensure we:
            don't create duplicates when sending same item multiple times;
            override fields correctly.
        """
        initial_item = self.sample_list[0].copy()
        for _ in range(5):
            response = self.client.post(self.endpoint, initial_item)
            self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
            self.assertEqual(Lender.objects.count(), 1)
            initial_instance = Lender.objects.get()
            self.assertEqual(initial_instance.ogrn, initial_item['ogrn'])

        changed_item = initial_item.copy()
        changed_item['scraped_from'] = ['http://test.com']
        changed_item['type'] = 'different type'
        response = self.client.post(self.endpoint, changed_item)
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        # didn't create duplicates
        self.assertEqual(Lender.objects.count(), 1)
        changed_instance = Lender.objects.get()
        # `scraped_from` shouldn't be overriden
        self.assertEqual(changed_instance.scraped_from, initial_instance.scraped_from)
        # `type` should be overriden
        self.assertNotEqual(changed_instance.type, initial_instance.type)
        # and become `'different type'`
        self.assertEqual(changed_instance.type, changed_item['type'])
        # `updated_at` should refreshed
        self.assertNotEqual(changed_instance.updated_at, initial_instance.updated_at)

    def test_create_item_error(self):
        """
        Ensure we cannot create single Lender object from invalid data.
        """
        item = self.sample_list[0].copy()
        item['website'] = 'invalid website'
        response = self.client.post(self.endpoint, item)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_list_sample(self):
        """
        Ensure we can create multiple Lender objects from sample list.
        """
        response = self.client.post(self.endpoint, self.sample_list)
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        self.assertEqual(Lender.objects.count(), len(self.sample_list))

    def test_update_list_sample(self):
        """
        Ensure we don't create duplicates by sending same sample multiple times.
        """
        for _ in range(4):
            response = self.client.post(self.endpoint, self.sample_list)
            self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
            self.assertEqual(Lender.objects.count(), len(self.sample_list))

    def test_create_list_scraper(self):
        """
        Ensure we can create multiple Lender objects from sample scraper output.
        """
        with open('mfo/utils/imitate_scrapers_input/cbr.json') as json_file:
            json_data = json.load(json_file)
        response = self.client.post(self.endpoint, json_data)
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        self.assertEqual(Lender.objects.count(), len(json_data))

    def test_update_list_scraper(self):
        """
        Ensure we don't create duplicates by sending same sample multiple times.
        """
        with open('mfo/utils/imitate_scrapers_input/cbr.json') as json_file:
            json_data = json.load(json_file)
        for _ in range(2):
            response = self.client.post(self.endpoint, json_data)
            self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
            self.assertEqual(Lender.objects.count(), len(json_data))
