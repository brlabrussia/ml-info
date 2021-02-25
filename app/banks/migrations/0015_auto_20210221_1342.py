import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('banks', '0014_auto_20210221_0940'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='autocredit',
            options={'ordering': ['-updated_at']},
        ),
        migrations.RenameField(
            model_name='autocredit',
            old_name='banki_bank_url',
            new_name='url_bank_banki',
        ),
        migrations.RenameField(
            model_name='autocredit',
            old_name='banki_url',
            new_name='url_self_banki',
        ),
        migrations.AddField(
            model_name='autocredit',
            name='banki_updated_at',
            field=models.DateTimeField(blank=True, help_text='Дата актуализации банки.ру', null=True),
        ),
        migrations.AddField(
            model_name='autocredit',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='autocredit',
            name='additional_conditions',
            field=models.TextField(blank=True, help_text='Особые условия'),
        ),
        migrations.AlterField(
            model_name='autocredit',
            name='auto_age',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), blank=True, help_text='Возраст транспортного средства', null=True, size=None),
        ),
        migrations.AlterField(
            model_name='autocredit',
            name='auto_kind',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), blank=True, help_text='Вид транспортного средства', null=True, size=None),
        ),
        migrations.AlterField(
            model_name='autocredit',
            name='auto_seller',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), blank=True, help_text='Продавец', null=True, size=None),
        ),
        migrations.AlterField(
            model_name='autocredit',
            name='auto_type',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), blank=True, help_text='Тип транспортного средства', null=True, size=None),
        ),
        migrations.AlterField(
            model_name='autocredit',
            name='autocredit_amount_max',
            field=models.TextField(blank=True, help_text='Сумма кредита'),
        ),
        migrations.AlterField(
            model_name='autocredit',
            name='autocredit_amount_min',
            field=models.TextField(blank=True, help_text='Сумма кредита'),
        ),
        migrations.AlterField(
            model_name='autocredit',
            name='autocredit_comission',
            field=models.TextField(blank=True, help_text='Комиссии при рассмотрении'),
        ),
        migrations.AlterField(
            model_name='autocredit',
            name='autocredit_currency',
            field=models.TextField(blank=True, help_text='Валюта'),
        ),
        migrations.AlterField(
            model_name='autocredit',
            name='autocredit_max_time',
            field=models.TextField(blank=True, help_text='Срок кредита'),
        ),
        migrations.AlterField(
            model_name='autocredit',
            name='autocredit_min_time',
            field=models.TextField(blank=True, help_text='Срок кредита'),
        ),
        migrations.AlterField(
            model_name='autocredit',
            name='bank',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='banks.bank'),
        ),
        migrations.AlterField(
            model_name='autocredit',
            name='borrowers_age',
            field=models.TextField(blank=True, help_text='Возраст заёмщика'),
        ),
        migrations.AlterField(
            model_name='autocredit',
            name='early_moratorium_repayment',
            field=models.TextField(blank=True, help_text='Мораторий на досрочное погашение'),
        ),
        migrations.AlterField(
            model_name='autocredit',
            name='full_work_experience',
            field=models.TextField(blank=True, help_text='Стаж работы общий'),
        ),
        migrations.AlterField(
            model_name='autocredit',
            name='has_repurchase',
            field=models.BooleanField(default=False, help_text='Возможность обратного выкупа'),
        ),
        migrations.AlterField(
            model_name='autocredit',
            name='income_proof',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), blank=True, help_text='Подтверждение дохода', null=True, size=None),
        ),
        migrations.AlterField(
            model_name='autocredit',
            name='insurance_necessity',
            field=models.BooleanField(blank=True, help_text='Необходимость страхования', null=True),
        ),
        migrations.AlterField(
            model_name='autocredit',
            name='last_work_experience',
            field=models.TextField(blank=True, help_text='Стаж работы на последнем месте'),
        ),
        migrations.AlterField(
            model_name='autocredit',
            name='loan_rate_max',
            field=models.FloatField(blank=True, help_text='Cтавка по кредиту', null=True),
        ),
        migrations.AlterField(
            model_name='autocredit',
            name='loan_rate_min',
            field=models.FloatField(blank=True, help_text='Cтавка по кредиту', null=True),
        ),
        migrations.AlterField(
            model_name='autocredit',
            name='min_down_payment',
            field=models.FloatField(blank=True, help_text='Минимальный первоначальный взнос', null=True),
        ),
        migrations.AlterField(
            model_name='autocredit',
            name='prepayment_penalty',
            field=models.TextField(blank=True, help_text='Штраф за досрочное погашение'),
        ),
        migrations.AlterField(
            model_name='autocredit',
            name='registration_requirements',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), blank=True, help_text='Регистрация по месту получения кредита', null=True, size=None),
        ),
        migrations.AlterField(
            model_name='autocredit',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
