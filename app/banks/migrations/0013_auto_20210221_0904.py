import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('banks', '0012_auto_20210221_0512'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='debitcard',
            options={'ordering': ['-updated_at']},
        ),
        migrations.RenameField(
            model_name='debitcard',
            old_name='banki_bank_url',
            new_name='url_bank_banki',
        ),
        migrations.RenameField(
            model_name='debitcard',
            old_name='banki_url',
            new_name='url_self_banki',
        ),
        migrations.AddField(
            model_name='debitcard',
            name='banki_updated_at',
            field=models.DateTimeField(blank=True, help_text='Дата актуализации банки.ру', null=True),
        ),
        migrations.AddField(
            model_name='debitcard',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='debitcard',
            name='additional_information',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), blank=True, help_text='Дополнительная информация', null=True, size=None),
        ),
        migrations.AlterField(
            model_name='debitcard',
            name='bank',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='banks.bank'),
        ),
        migrations.AlterField(
            model_name='debitcard',
            name='borrower_age',
            field=models.TextField(blank=True, help_text='Возраст'),
        ),
        migrations.AlterField(
            model_name='debitcard',
            name='borrower_registration',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), blank=True, help_text='Регистрация', null=True, size=None),
        ),
        migrations.AlterField(
            model_name='debitcard',
            name='cash_pickup_point',
            field=models.TextField(blank=True, help_text='Снятие наличных в ПВН банка'),
        ),
        migrations.AlterField(
            model_name='debitcard',
            name='cash_withdrawal',
            field=models.TextField(blank=True, help_text='Снятие наличных в банкоматах банка'),
        ),
        migrations.AlterField(
            model_name='debitcard',
            name='debit_bonuses',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), blank=True, help_text='Бонусы', null=True, size=None),
        ),
        migrations.AlterField(
            model_name='debitcard',
            name='debit_cashback',
            field=models.TextField(blank=True, help_text='Cash Back'),
        ),
        migrations.AlterField(
            model_name='debitcard',
            name='debit_type',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), blank=True, help_text='Тип карты', null=True, size=None),
        ),
        migrations.AlterField(
            model_name='debitcard',
            name='expert_negative',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), blank=True, help_text='Минусы', null=True, size=None),
        ),
        migrations.AlterField(
            model_name='debitcard',
            name='expert_positive',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), blank=True, help_text='Плюсы', null=True, size=None),
        ),
        migrations.AlterField(
            model_name='debitcard',
            name='expert_restrictions',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), blank=True, help_text='Особые ограничения', null=True, size=None),
        ),
        migrations.AlterField(
            model_name='debitcard',
            name='foreign_cash_pickup_point',
            field=models.JSONField(blank=True, default=dict, help_text='Снятие наличных в ПВН других банков'),
        ),
        migrations.AlterField(
            model_name='debitcard',
            name='foreign_cash_withdrawal',
            field=models.JSONField(blank=True, default=dict, help_text='Снятие наличных в банкоматах других банков'),
        ),
        migrations.AlterField(
            model_name='debitcard',
            name='interest_accrual',
            field=models.JSONField(blank=True, default=dict, help_text='Начисление процентов на остаток средств на счете'),
        ),
        migrations.AlterField(
            model_name='debitcard',
            name='operations_limit',
            field=models.JSONField(blank=True, default=dict, help_text='Лимиты по операциям'),
        ),
        migrations.AlterField(
            model_name='debitcard',
            name='service_cost',
            field=models.JSONField(blank=True, default=dict, help_text='Выпуск и годовое обслуживание'),
        ),
        migrations.AlterField(
            model_name='debitcard',
            name='summary',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), blank=True, help_text='Основные характеристики', null=True, size=None),
        ),
        migrations.AlterField(
            model_name='debitcard',
            name='technological_features',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), blank=True, help_text='Технологические особенности', null=True, size=None),
        ),
        migrations.AlterField(
            model_name='debitcard',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
