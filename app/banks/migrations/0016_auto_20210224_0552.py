import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('banks', '0015_auto_20210221_1342'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='consumercredit',
            options={'ordering': ['-updated_at']},
        ),
        migrations.RenameField(
            model_name='consumercredit',
            old_name='banki_bank_url',
            new_name='url_bank_banki',
        ),
        migrations.RenameField(
            model_name='consumercredit',
            old_name='banki_url',
            new_name='url_self_banki',
        ),
        migrations.AddField(
            model_name='consumercredit',
            name='banki_updated_at',
            field=models.DateTimeField(blank=True, help_text='Дата актуализации банки.ру', null=True),
        ),
        migrations.AddField(
            model_name='consumercredit',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='consumercredit',
            name='account_currency',
            field=models.TextField(blank=True, help_text='Валюта счета'),
        ),
        migrations.AlterField(
            model_name='consumercredit',
            name='additional_information',
            field=models.TextField(blank=True, help_text='Дополнительная информация'),
        ),
        migrations.AlterField(
            model_name='consumercredit',
            name='application_consider_time',
            field=models.TextField(blank=True, help_text='Срок рассмотрения заявки'),
        ),
        migrations.AlterField(
            model_name='consumercredit',
            name='bank',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='banks.bank'),
        ),
        migrations.AlterField(
            model_name='consumercredit',
            name='borrowers_age_men',
            field=models.TextField(blank=True, help_text='Возраст заемщика'),
        ),
        migrations.AlterField(
            model_name='consumercredit',
            name='borrowers_age_women',
            field=models.TextField(blank=True, help_text='Возраст заемщика'),
        ),
        migrations.AlterField(
            model_name='consumercredit',
            name='borrowers_category',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), blank=True, help_text='Категория заемщиков', null=True, size=None),
        ),
        migrations.AlterField(
            model_name='consumercredit',
            name='borrowers_documents',
            field=models.JSONField(blank=True, default=dict, help_text='Документы'),
        ),
        migrations.AlterField(
            model_name='consumercredit',
            name='borrowers_income_description',
            field=models.TextField(blank=True, help_text='Доход'),
        ),
        migrations.AlterField(
            model_name='consumercredit',
            name='borrowers_income_documents',
            field=models.JSONField(blank=True, default=dict, help_text='Доход'),
        ),
        migrations.AlterField(
            model_name='consumercredit',
            name='borrowers_income_tip',
            field=models.TextField(blank=True, help_text='Доход'),
        ),
        migrations.AlterField(
            model_name='consumercredit',
            name='borrowers_registration',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), blank=True, help_text='Регистрация', null=True, size=None),
        ),
        migrations.AlterField(
            model_name='consumercredit',
            name='credit_decision_time',
            field=models.TextField(blank=True, help_text='Максимальный срок действия кредитного решения'),
        ),
        migrations.AlterField(
            model_name='consumercredit',
            name='credit_fee',
            field=models.JSONField(blank=True, default=dict, help_text='Комиссии'),
        ),
        migrations.AlterField(
            model_name='consumercredit',
            name='credit_insurance',
            field=models.JSONField(blank=True, default=dict, help_text='Страхование'),
        ),
        migrations.AlterField(
            model_name='consumercredit',
            name='early_repayment_full',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), blank=True, help_text='Досрочное погашение полное', null=True, size=None),
        ),
        migrations.AlterField(
            model_name='consumercredit',
            name='early_repayment_partial',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), blank=True, help_text='Досрочное погашение частичное', null=True, size=None),
        ),
        migrations.AlterField(
            model_name='consumercredit',
            name='loan_delivery_order',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), blank=True, help_text='Режим выдачи', null=True, size=None),
        ),
        migrations.AlterField(
            model_name='consumercredit',
            name='loan_delivery_type',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), blank=True, help_text='Форма выдачи', null=True, size=None),
        ),
        migrations.AlterField(
            model_name='consumercredit',
            name='loan_processing_terms',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), blank=True, help_text='Оформление кредита', null=True, size=None),
        ),
        migrations.AlterField(
            model_name='consumercredit',
            name='loan_purpose',
            field=models.TextField(blank=True, help_text='Цель кредита'),
        ),
        migrations.AlterField(
            model_name='consumercredit',
            name='loan_security',
            field=models.JSONField(blank=True, default=dict, help_text='Обеспечение'),
        ),
        migrations.AlterField(
            model_name='consumercredit',
            name='obligations_violation',
            field=models.TextField(blank=True, help_text='Нарушение обязательств по кредиту'),
        ),
        migrations.AlterField(
            model_name='consumercredit',
            name='payment_method',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), blank=True, help_text='Способ оплаты', null=True, size=None),
        ),
        migrations.AlterField(
            model_name='consumercredit',
            name='rates_table',
            field=models.JSONField(blank=True, default=dict, help_text='Таблица ставок'),
        ),
        migrations.AlterField(
            model_name='consumercredit',
            name='repayment_procedure',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), blank=True, help_text='Порядок погашения', null=True, size=None),
        ),
        migrations.AlterField(
            model_name='consumercredit',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='consumercredit',
            name='work_experience',
            field=models.TextField(blank=True, help_text='Стаж работы'),
        ),
    ]
