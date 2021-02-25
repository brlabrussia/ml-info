import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('banks', '0013_auto_20210221_0904'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='creditcard',
            options={'ordering': ['-updated_at']},
        ),
        migrations.RenameField(
            model_name='creditcard',
            old_name='banki_bank_url',
            new_name='url_bank_banki',
        ),
        migrations.RenameField(
            model_name='creditcard',
            old_name='banki_url',
            new_name='url_self_banki',
        ),
        migrations.AddField(
            model_name='creditcard',
            name='banki_updated_at',
            field=models.DateTimeField(blank=True, help_text='Дата актуализации банки.ру', null=True),
        ),
        migrations.AddField(
            model_name='creditcard',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='creditcard',
            name='additional_information',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), blank=True, help_text='Дополнительная информация', null=True, size=None),
        ),
        migrations.AlterField(
            model_name='creditcard',
            name='bank',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='banks.bank'),
        ),
        migrations.AlterField(
            model_name='creditcard',
            name='borrower_age',
            field=models.TextField(blank=True, help_text='Возраст'),
        ),
        migrations.AlterField(
            model_name='creditcard',
            name='borrower_experience',
            field=models.TextField(blank=True, help_text='Стаж работы'),
        ),
        migrations.AlterField(
            model_name='creditcard',
            name='borrower_income',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), blank=True, help_text='Подтверждение дохода', null=True, size=None),
        ),
        migrations.AlterField(
            model_name='creditcard',
            name='borrower_registration',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), blank=True, help_text='Регистрация', null=True, size=None),
        ),
        migrations.AlterField(
            model_name='creditcard',
            name='cash_pickup_point',
            field=models.TextField(blank=True, help_text='Снятие наличных в ПВН банка'),
        ),
        migrations.AlterField(
            model_name='creditcard',
            name='cash_withdrawal',
            field=models.TextField(blank=True, help_text='Снятие наличных в банкоматах банка'),
        ),
        migrations.AlterField(
            model_name='creditcard',
            name='credit_bonuses',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), blank=True, help_text='Бонусы', null=True, size=None),
        ),
        migrations.AlterField(
            model_name='creditcard',
            name='credit_cashback',
            field=models.TextField(blank=True, help_text='Cash Back'),
        ),
        migrations.AlterField(
            model_name='creditcard',
            name='credit_limit',
            field=models.TextField(blank=True, help_text='Размер кредитного лимита'),
        ),
        migrations.AlterField(
            model_name='creditcard',
            name='credit_period',
            field=models.TextField(blank=True, help_text='Срок кредита'),
        ),
        migrations.AlterField(
            model_name='creditcard',
            name='credit_type',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), blank=True, help_text='Тип карты', null=True, size=None),
        ),
        migrations.AlterField(
            model_name='creditcard',
            name='expert_negative',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), blank=True, help_text='Минусы', null=True, size=None),
        ),
        migrations.AlterField(
            model_name='creditcard',
            name='expert_positive',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), blank=True, help_text='Плюсы', null=True, size=None),
        ),
        migrations.AlterField(
            model_name='creditcard',
            name='expert_restrictions',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), blank=True, help_text='Особые ограничения', null=True, size=None),
        ),
        migrations.AlterField(
            model_name='creditcard',
            name='foreign_cash_pickup_point',
            field=models.JSONField(blank=True, default=dict, help_text='Снятие наличных в ПВН других банков'),
        ),
        migrations.AlterField(
            model_name='creditcard',
            name='foreign_cash_withdrawal',
            field=models.JSONField(blank=True, default=dict, help_text='Снятие наличных в банкоматах других банков'),
        ),
        migrations.AlterField(
            model_name='creditcard',
            name='grace_period',
            field=models.TextField(blank=True, help_text='Льготный период'),
        ),
        migrations.AlterField(
            model_name='creditcard',
            name='interest_accrual',
            field=models.JSONField(blank=True, default=dict, help_text='Начисление процентов на остаток средств на счете'),
        ),
        migrations.AlterField(
            model_name='creditcard',
            name='operations_limit',
            field=models.JSONField(blank=True, default=dict, help_text='Лимиты по операциям'),
        ),
        migrations.AlterField(
            model_name='creditcard',
            name='own_funds',
            field=models.BooleanField(blank=True, help_text='Использование собственных средств', null=True),
        ),
        migrations.AlterField(
            model_name='creditcard',
            name='percentage_credit',
            field=models.TextField(blank=True, help_text='Проценты за кредит'),
        ),
        migrations.AlterField(
            model_name='creditcard',
            name='percentage_grace',
            field=models.TextField(blank=True, help_text='Проценты в течение льготного периода'),
        ),
        migrations.AlterField(
            model_name='creditcard',
            name='repayment',
            field=models.TextField(blank=True, help_text='Погашение кредита'),
        ),
        migrations.AlterField(
            model_name='creditcard',
            name='service_cost',
            field=models.JSONField(blank=True, default=dict, help_text='Выпуск и годовое обслуживание'),
        ),
        migrations.AlterField(
            model_name='creditcard',
            name='summary',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), blank=True, help_text='Основные характеристики', null=True, size=None),
        ),
        migrations.AlterField(
            model_name='creditcard',
            name='technological_features',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), blank=True, help_text='Технологические особенности', null=True, size=None),
        ),
        migrations.AlterField(
            model_name='creditcard',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
