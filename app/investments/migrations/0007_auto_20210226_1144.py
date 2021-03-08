import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('investments', '0006_iia_docs'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bond',
            options={'ordering': ['-updated_at']},
        ),
        migrations.AlterModelOptions(
            name='iia',
            options={'ordering': ['-updated_at']},
        ),
        migrations.AlterModelOptions(
            name='mutual',
            options={'ordering': ['-updated_at']},
        ),
        migrations.AlterModelOptions(
            name='share',
            options={'ordering': ['-updated_at']},
        ),
        migrations.AddField(
            model_name='bond',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bond',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='iia',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='iia',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='mutual',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mutual',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='share',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='share',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='bond',
            name='coupon_date',
            field=models.DateTimeField(blank=True, help_text='Ближайшая выплата купона', null=True),
        ),
        migrations.AlterField(
            model_name='bond',
            name='coupon_yield',
            field=models.FloatField(blank=True, help_text='Купон', null=True),
        ),
        migrations.AlterField(
            model_name='bond',
            name='isin',
            field=models.CharField(help_text='ИСИН', max_length=12, unique=True, validators=[django.core.validators.RegexValidator('^\\w{12}$')]),
        ),
        migrations.AlterField(
            model_name='bond',
            name='issuer',
            field=models.CharField(blank=True, help_text='Наименование эмитента', max_length=200),
        ),
        migrations.AlterField(
            model_name='bond',
            name='logo',
            field=models.URLField(blank=True, help_text='Логотип компании'),
        ),
        migrations.AlterField(
            model_name='bond',
            name='maturity_date',
            field=models.DateTimeField(blank=True, help_text='Срок до погашения', null=True),
        ),
        migrations.AlterField(
            model_name='bond',
            name='maturity_yield',
            field=models.FloatField(blank=True, help_text='Доходность к погашению', null=True),
        ),
        migrations.AlterField(
            model_name='bond',
            name='name',
            field=models.CharField(blank=True, help_text='Наименование облигации', max_length=200),
        ),
        migrations.AlterField(
            model_name='bond',
            name='offer_date',
            field=models.DateTimeField(blank=True, help_text='Ближайшая оферта', null=True),
        ),
        migrations.AlterField(
            model_name='bond',
            name='offer_yield',
            field=models.FloatField(blank=True, help_text='Доходность к оферте', null=True),
        ),
        migrations.AlterField(
            model_name='bond',
            name='price',
            field=models.FloatField(blank=True, help_text='Цена за 1 облигацию', null=True),
        ),
        migrations.AlterField(
            model_name='bond',
            name='risk',
            field=models.PositiveSmallIntegerField(blank=True, help_text='Индикатор риска при покупке облигации', null=True),
        ),
        migrations.AlterField(
            model_name='iia',
            name='company',
            field=models.CharField(blank=True, help_text='Наименование компании', max_length=200),
        ),
        migrations.AlterField(
            model_name='iia',
            name='docs',
            field=models.JSONField(blank=True, help_text='Документы', null=True),
        ),
        migrations.AlterField(
            model_name='iia',
            name='fees',
            field=models.JSONField(blank=True, help_text='Комиссии', null=True),
        ),
        migrations.AlterField(
            model_name='iia',
            name='filter',
            field=models.CharField(blank=True, help_text='Фильтр, по которому выводит данный ИИС (высокий риск, низкий риск и тп)', max_length=200),
        ),
        migrations.AlterField(
            model_name='iia',
            name='investment_min',
            field=models.PositiveIntegerField(blank=True, help_text='Мин. инвестиция', null=True),
        ),
        migrations.AlterField(
            model_name='iia',
            name='logo',
            field=models.URLField(blank=True, help_text='Логотип компании'),
        ),
        migrations.AlterField(
            model_name='iia',
            name='name',
            field=models.CharField(blank=True, help_text='Наименование ИИС', max_length=200),
        ),
        migrations.AlterField(
            model_name='iia',
            name='yield_block',
            field=models.JSONField(blank=True, help_text='Блок с доходностями с банки.ру', null=True),
        ),
        migrations.AlterField(
            model_name='iia',
            name='yield_type',
            field=models.CharField(blank=True, help_text='Тип доходности из шапки/списка', max_length=200),
        ),
        migrations.AlterField(
            model_name='iia',
            name='yield_value',
            field=models.FloatField(blank=True, help_text='Значение доходности из шапки/списка', null=True),
        ),
        migrations.AlterField(
            model_name='mutual',
            name='company',
            field=models.CharField(blank=True, help_text='Наименование компании', max_length=200),
        ),
        migrations.AlterField(
            model_name='mutual',
            name='docs',
            field=models.JSONField(blank=True, help_text='Документы', null=True),
        ),
        migrations.AlterField(
            model_name='mutual',
            name='fees',
            field=models.JSONField(blank=True, help_text='Комиссии', null=True),
        ),
        migrations.AlterField(
            model_name='mutual',
            name='filter',
            field=models.CharField(blank=True, help_text='Фильтр, по которому выводит данный ПИФ (в тч ETF)', max_length=200),
        ),
        migrations.AlterField(
            model_name='mutual',
            name='investment_min',
            field=models.PositiveIntegerField(blank=True, help_text='Мин. инвестиция', null=True),
        ),
        migrations.AlterField(
            model_name='mutual',
            name='logo',
            field=models.URLField(blank=True, help_text='Логотип компании'),
        ),
        migrations.AlterField(
            model_name='mutual',
            name='name',
            field=models.CharField(blank=True, help_text='Наименование ПИФ', max_length=200),
        ),
        migrations.AlterField(
            model_name='mutual',
            name='yield_block',
            field=models.JSONField(blank=True, help_text='Блок с доходностями с банки.ру', null=True),
        ),
        migrations.AlterField(
            model_name='mutual',
            name='yield_type',
            field=models.CharField(blank=True, help_text='Тип доходности из шапки/списка', max_length=200),
        ),
        migrations.AlterField(
            model_name='mutual',
            name='yield_value',
            field=models.FloatField(blank=True, help_text='Значение доходности из шапки/списка', null=True),
        ),
        migrations.AlterField(
            model_name='share',
            name='dividend_history',
            field=models.JSONField(blank=True, help_text='История дивидендной доходности', null=True),
        ),
        migrations.AlterField(
            model_name='share',
            name='isin',
            field=models.CharField(help_text='ИСИН', max_length=12, unique=True, validators=[django.core.validators.RegexValidator('^\\w{12}$')]),
        ),
        migrations.AlterField(
            model_name='share',
            name='logo',
            field=models.URLField(blank=True, help_text='Логотип компании'),
        ),
        migrations.AlterField(
            model_name='share',
            name='name',
            field=models.CharField(blank=True, help_text='Название акции', max_length=200),
        ),
        migrations.AlterField(
            model_name='share',
            name='price',
            field=models.FloatField(blank=True, help_text='Текущая цена', null=True),
        ),
        migrations.AlterField(
            model_name='share',
            name='price_dynamic',
            field=models.JSONField(blank=True, help_text='Динамика изменения акций', null=True),
        ),
        migrations.AlterField(
            model_name='share',
            name='seo_quote',
            field=models.JSONField(blank=True, help_text='Сеошный текст по котировкам', null=True),
        ),
    ]
