import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banks', '0011_auto_20210211_0525'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bankcard',
            name='bank',
        ),
        migrations.RemoveField(
            model_name='banksubsidiary',
            name='bank',
        ),
        migrations.AlterModelOptions(
            name='bank',
            options={'ordering': ['-updated_at']},
        ),
        migrations.RenameField(
            model_name='bank',
            old_name='banki_url',
            new_name='url_self_banki',
        ),
        migrations.RenameField(
            model_name='bank',
            old_name='cbr_url',
            new_name='url_self_cbr',
        ),
        migrations.AddField(
            model_name='bank',
            name='agencies',
            field=models.JSONField(blank=True, help_text='Представительства', null=True),
        ),
        migrations.AddField(
            model_name='bank',
            name='cards',
            field=models.JSONField(blank=True, help_text='Сведения об эмиссии и эквайринге банковских карт', null=True),
        ),
        migrations.AddField(
            model_name='bank',
            name='subsidiaries',
            field=models.JSONField(blank=True, help_text='Филиалы', null=True),
        ),
        migrations.AlterField(
            model_name='bank',
            name='actual_address',
            field=models.TextField(blank=True, help_text='Адрес фактический'),
        ),
        migrations.AlterField(
            model_name='bank',
            name='additional_offices',
            field=models.BigIntegerField(blank=True, help_text='Дополнительные офисы, количество', null=True),
        ),
        migrations.AlterField(
            model_name='bank',
            name='authorized_capital',
            field=models.BigIntegerField(blank=True, help_text='Уставный капитал', null=True),
        ),
        migrations.AlterField(
            model_name='bank',
            name='bank_agencies',
            field=models.BigIntegerField(blank=True, help_text='Представительства, количество', null=True),
        ),
        migrations.AlterField(
            model_name='bank',
            name='bank_subsidiaries',
            field=models.TextField(blank=True, help_text='Филиалы, инфа о кол-ве'),
        ),
        migrations.AlterField(
            model_name='bank',
            name='bik',
            field=models.TextField(blank=True, help_text='БИК'),
        ),
        migrations.AlterField(
            model_name='bank',
            name='deposit_insurance_system',
            field=models.BooleanField(blank=True, help_text='Участие в системе страхования вкладов', null=True),
        ),
        migrations.AlterField(
            model_name='bank',
            name='english_name',
            field=models.TextField(blank=True, help_text='Фирменное наименование на английском языке'),
        ),
        migrations.AlterField(
            model_name='bank',
            name='full_name',
            field=models.TextField(blank=True, help_text='Полное фирменное наименование'),
        ),
        migrations.AlterField(
            model_name='bank',
            name='info_sites',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.URLField(), blank=True, help_text='Информационные сайты и страницы организации в социальных сетях', null=True, size=None),
        ),
        migrations.AlterField(
            model_name='bank',
            name='license_info',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), blank=True, help_text='Лицензия (дата выдачи/последней замены)', null=True, size=None),
        ),
        migrations.AlterField(
            model_name='bank',
            name='license_info_file',
            field=models.URLField(blank=True, help_text='Лицензия файлом'),
        ),
        migrations.AlterField(
            model_name='bank',
            name='mobile_cash_desks',
            field=models.BigIntegerField(blank=True, help_text='Передвижные пункты кассовых операций, количество', null=True),
        ),
        migrations.AlterField(
            model_name='bank',
            name='name',
            field=models.TextField(blank=True, help_text='Сокращённое фирменное наименование'),
        ),
        migrations.AlterField(
            model_name='bank',
            name='ogrn',
            field=models.TextField(blank=True, help_text='Основной государственный регистрационный номер'),
        ),
        migrations.AlterField(
            model_name='bank',
            name='operating_cash_desks',
            field=models.BigIntegerField(blank=True, help_text='Операционные кассы вне кассового узла, количество', null=True),
        ),
        migrations.AlterField(
            model_name='bank',
            name='operating_offices',
            field=models.BigIntegerField(blank=True, help_text='Операционные офисы, количество', null=True),
        ),
        migrations.AlterField(
            model_name='bank',
            name='reg_number',
            field=models.TextField(blank=True, help_text='Регистрационный номер'),
        ),
        migrations.AlterField(
            model_name='bank',
            name='registration_date',
            field=models.DateTimeField(blank=True, help_text='Дата регистрации Банком России', null=True),
        ),
        migrations.AlterField(
            model_name='bank',
            name='statutory_address',
            field=models.TextField(blank=True, help_text='Адрес из устава'),
        ),
        migrations.AlterField(
            model_name='bank',
            name='tel_number',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), blank=True, help_text='Телефон', null=True, size=None),
        ),
        migrations.DeleteModel(
            name='BankAgency',
        ),
        migrations.DeleteModel(
            name='BankCard',
        ),
        migrations.DeleteModel(
            name='BankSubsidiary',
        ),
    ]
