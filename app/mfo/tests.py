import json

from rest_framework import status
from rest_framework.test import APITestCase

from .models import Lender, Loan


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


class ZaymovTestCase(APITestCase):
    endpoint = '/mfo/scrapers/zaymov/'
    sample_list = [
        {
            'scraped_from': [
                'https://zaymov.net/mfo/zaymer',
            ],
            'trademark': 'Займер',
            'logo': 'https://zaymov.net/wp-content/themes/zaymovnet/images/mfo/zaymer.png',
            'cbrn': '1303532004088',
            'ogrn': '1134205019189',
            'cbr_created_at': '2013-11-10T00:00:00+04:00',
            'address': '650000, Кемеровская обл., г. Кемерово, Советский пр-т, д. 2/7',
        },
        {
            'scraped_from': [
                'https://zaymov.net/mfo/vkarmane',
            ],
            'trademark': 'Вкармане',
            'logo': 'https://zaymov.net/wp-content/themes/zaymovnet/images/mfo/vkarmane.png',
            'cbrn': '1403550005450',
            'ogrn': '1145476064711',
            'cbr_created_at': '2014-07-28T00:00:00+04:00',
            'address': '630004 г. Новосибирск, ул. Дмитрия Шамшурина д. 1, офис 1',
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
        changed_item['cbrn'] = '0123456789012'
        changed_item['address'] = 'different address'
        response = self.client.post(self.endpoint, changed_item)
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        # didn't create duplicates
        self.assertEqual(Lender.objects.count(), 1)
        changed_instance = Lender.objects.get()
        # `cbrn` shouldn't be overriden
        self.assertEqual(changed_instance.cbrn, initial_instance.cbrn)
        # `address` should be overriden
        self.assertNotEqual(changed_instance.address, initial_instance.address)
        # and become `'different address'`
        self.assertEqual(changed_instance.address, changed_item['address'])
        # `updated_at` should refreshed
        self.assertNotEqual(changed_instance.updated_at, initial_instance.updated_at)

    def test_create_item_error(self):
        """
        Ensure we cannot create single Lender object from invalid data.
        """
        item = self.sample_list[0].copy()
        del item['scraped_from']  # `scraped_from` is required
        response = self.client.post(self.endpoint, item)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_list_sample(self):
        """
        Ensure we can create multiple Lender objects from sample list.
        """
        response = self.client.post(self.endpoint, self.sample_list)
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        self.assertLessEqual(Lender.objects.count(), len(self.sample_list))

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
        with open('mfo/utils/imitate_scrapers_input/zaymov.json') as json_file:
            json_data = json.load(json_file)
        response = self.client.post(self.endpoint, json_data)
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        self.assertLessEqual(Lender.objects.count(), len(json_data))

    def test_update_list_scraper(self):
        """
        Ensure we don't create duplicates by sending same sample multiple times.
        """
        with open('mfo/utils/imitate_scrapers_input/zaymov.json') as json_file:
            json_data = json.load(json_file)
        for _ in range(2):
            response = self.client.post(self.endpoint, json_data)
            self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
            self.assertLessEqual(Lender.objects.count(), len(json_data))


class VsezaimyonlineTestCase(APITestCase):
    endpoint = '/mfo/scrapers/vsezaimyonline/'
    sample_list = [
        {
            'scraped_from': [
                'https://vsezaimyonline.ru/mobifinans',
            ],
            'trademark': 'Мобифинанс',
            'logo': 'https://vsezaimyonline.ru/images/zajm/mobifinans.png',
            'ogrn': '5157746003366',
            'inn': '7718282033',
            'decline_reasons': [
                'Заемщику нет 18 лет',
                'Заемщик имеет незакрытые долги перед компанией',
                'Заемщик не является гражданином Российской Федерации',
                'У заемщика отсутствует мобильный телефон (или номер указан неверно)',
            ],
            'documents': [
                {
                    'name': 'Правила предоставления займов',
                    'url': 'https://vsezaimyonline.ru/files/new/mobifinans1.pdf',
                },
            ],
            'decision_speed': '1 минута',
            'payment_speed': 'Моментально',
        },
        {
            'scraped_from': [
                'https://vsezaimyonline.ru/chestnii-zaim',
            ],
            'trademark': 'Честный займ',
            'logo': 'https://vsezaimyonline.ru/images/zajm/chestnii-zaim.png',
            'ogrn': '1152901002330',
            'inn': '2901256280',
            'decline_reasons': [
                'Несоответствие возрасту',
                'Несоответствие поданных данных реальным',
                'Неправильно заполненная заявка',
            ],
            'documents': [
                {
                    'name': 'Свидетельство о внесении в реестр МФО',
                    'url': 'https://vsezaimyonline.ru/files/chestnii-zaim-1.pdf',
                },
                {
                    'name': 'Свидетельство о членстве в СРО',
                    'url': 'https://vsezaimyonline.ru/files/chestnii-zaim-2.pdf',
                },
            ],
            'decision_speed': 'От 10 минут',
            'payment_speed': 'В течение дня',
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
        changed_item['ogrn'] = '0123456789012'
        changed_item['payment_speed'] = 'different payment_speed'
        response = self.client.post(self.endpoint, changed_item)
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        # didn't create duplicates
        self.assertEqual(Lender.objects.count(), 1)
        changed_instance = Lender.objects.get()
        # `ogrn` shouldn't be overriden
        self.assertEqual(changed_instance.cbrn, initial_instance.cbrn)
        # `payment_speed` should be overriden
        self.assertNotEqual(changed_instance.payment_speed, initial_instance.payment_speed)
        # and become `'different payment_speed'`
        self.assertEqual(changed_instance.payment_speed, changed_item['payment_speed'])
        # `updated_at` should refreshed
        self.assertNotEqual(changed_instance.updated_at, initial_instance.updated_at)

    def test_create_item_error(self):
        """
        Ensure we cannot create single Lender object from invalid data.
        """
        item = self.sample_list[0].copy()
        del item['scraped_from']  # `scraped_from` is required
        response = self.client.post(self.endpoint, item)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_list_sample(self):
        """
        Ensure we can create multiple Lender objects from sample list.
        """
        response = self.client.post(self.endpoint, self.sample_list)
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        self.assertLessEqual(Lender.objects.count(), len(self.sample_list))

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
        with open('mfo/utils/imitate_scrapers_input/vsezaimyonline.json') as json_file:
            json_data = json.load(json_file)
        response = self.client.post(self.endpoint, json_data)
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        self.assertLessEqual(Lender.objects.count(), len(json_data))

    def test_update_list_scraper(self):
        """
        Ensure we don't create duplicates by sending same sample multiple times.
        """
        with open('mfo/utils/imitate_scrapers_input/vsezaimyonline.json') as json_file:
            json_data = json.load(json_file)
        for _ in range(2):
            response = self.client.post(self.endpoint, json_data)
            self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
            self.assertLessEqual(Lender.objects.count(), len(json_data))
class ZaymovTestCase(APITestCase):
    endpoint = '/mfo/scrapers/zaymov/'
    sample_list = [
        {
            'scraped_from': [
                'https://zaymov.net/mfo/zaymer',
            ],
            'trademark': 'Займер',
            'logo': 'https://zaymov.net/wp-content/themes/zaymovnet/images/mfo/zaymer.png',
            'cbrn': '1303532004088',
            'ogrn': '1134205019189',
            'cbr_created_at': '2013-11-10T00:00:00+04:00',
            'address': '650000, Кемеровская обл., г. Кемерово, Советский пр-т, д. 2/7',
        },
        {
            'scraped_from': [
                'https://zaymov.net/mfo/vkarmane',
            ],
            'trademark': 'Вкармане',
            'logo': 'https://zaymov.net/wp-content/themes/zaymovnet/images/mfo/vkarmane.png',
            'cbrn': '1403550005450',
            'ogrn': '1145476064711',
            'cbr_created_at': '2014-07-28T00:00:00+04:00',
            'address': '630004 г. Новосибирск, ул. Дмитрия Шамшурина д. 1, офис 1',
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
        changed_item['cbrn'] = '0123456789012'
        changed_item['address'] = 'different address'
        response = self.client.post(self.endpoint, changed_item)
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        # didn't create duplicates
        self.assertEqual(Lender.objects.count(), 1)
        changed_instance = Lender.objects.get()
        # `cbrn` shouldn't be overriden
        self.assertEqual(changed_instance.cbrn, initial_instance.cbrn)
        # `address` should be overriden
        self.assertNotEqual(changed_instance.address, initial_instance.address)
        # and become `'different address'`
        self.assertEqual(changed_instance.address, changed_item['address'])
        # `updated_at` should refreshed
        self.assertNotEqual(changed_instance.updated_at, initial_instance.updated_at)

    def test_create_item_error(self):
        """
        Ensure we cannot create single Lender object from invalid data.
        """
        item = self.sample_list[0].copy()
        del item['scraped_from']  # `scraped_from` is required
        response = self.client.post(self.endpoint, item)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_list_sample(self):
        """
        Ensure we can create multiple Lender objects from sample list.
        """
        response = self.client.post(self.endpoint, self.sample_list)
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        self.assertLessEqual(Lender.objects.count(), len(self.sample_list))

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
        with open('mfo/utils/imitate_scrapers_input/zaymov.json') as json_file:
            json_data = json.load(json_file)
        response = self.client.post(self.endpoint, json_data)
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        self.assertLessEqual(Lender.objects.count(), len(json_data))

    def test_update_list_scraper(self):
        """
        Ensure we don't create duplicates by sending same sample multiple times.
        """
        with open('mfo/utils/imitate_scrapers_input/zaymov.json') as json_file:
            json_data = json.load(json_file)
        for _ in range(2):
            response = self.client.post(self.endpoint, json_data)
            self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
            self.assertLessEqual(Lender.objects.count(), len(json_data))


class BankiTestCase(APITestCase):
    endpoint = '/mfo/scrapers/banki/'

    def test_create_list_scraper(self):
        """
        Ensure we can create multiple Loan objects from sample scraper output.
        """
        with open('mfo/utils/imitate_scrapers_input/banki.json') as json_file:
            json_data = json.load(json_file)
        response = self.client.post(self.endpoint, json_data)
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        self.assertEqual(Loan.objects.count(), len(json_data))

    def test_update_list_scraper(self):
        """
        Ensure we don't create duplicates by sending same sample multiple times.
        """
        with open('mfo/utils/imitate_scrapers_input/banki.json') as json_file:
            json_data = json.load(json_file)
        for _ in range(2):
            response = self.client.post(self.endpoint, json_data)
            self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
            self.assertEqual(Loan.objects.count(), len(json_data))
