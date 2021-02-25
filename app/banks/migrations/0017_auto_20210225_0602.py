import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('banks', '0016_auto_20210224_0552'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='deposit',
            options={'ordering': ['-updated_at']},
        ),
        migrations.RenameField(
            model_name='deposit',
            old_name='banki_bank_url',
            new_name='url_bank_banki',
        ),
        migrations.RenameField(
            model_name='deposit',
            old_name='banki_url',
            new_name='url_self_banki',
        ),
        migrations.AddField(
            model_name='deposit',
            name='banki_updated_at',
            field=models.DateTimeField(blank=True, help_text='Дата актуализации банки.ру', null=True),
        ),
        migrations.AddField(
            model_name='deposit',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='deposit',
            name='auto_prolongation',
            field=models.IntegerField(blank=True, help_text='Автопролонгация', null=True),
        ),
        migrations.AlterField(
            model_name='deposit',
            name='bank',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='banks.bank'),
        ),
        migrations.AlterField(
            model_name='deposit',
            name='capitalization',
            field=models.TextField(blank=True, help_text='Капитализация'),
        ),
        migrations.AlterField(
            model_name='deposit',
            name='early_dissolution',
            field=models.TextField(blank=True, help_text='Досрочное расторжение'),
        ),
        migrations.AlterField(
            model_name='deposit',
            name='interest_payment',
            field=models.TextField(blank=True, help_text='Выплата процентов'),
        ),
        migrations.AlterField(
            model_name='deposit',
            name='is_staircase_contribution',
            field=models.BooleanField(default=False, help_text='Лестничный вклад'),
        ),
        migrations.AlterField(
            model_name='deposit',
            name='min_irreducible_balance',
            field=models.TextField(blank=True, help_text='Минимальный неснижаемый остаток'),
        ),
        migrations.AlterField(
            model_name='deposit',
            name='online_opening',
            field=models.TextField(blank=True, help_text='Открытие вклада online'),
        ),
        migrations.AlterField(
            model_name='deposit',
            name='partial_withdrawal',
            field=models.TextField(blank=True, help_text='Частичное снятие'),
        ),
        migrations.AlterField(
            model_name='deposit',
            name='rates_comments',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), blank=True, help_text='Комментарии к таблице ставок', null=True, size=None),
        ),
        migrations.AlterField(
            model_name='deposit',
            name='rates_table',
            field=models.JSONField(blank=True, default=dict, help_text='Таблица ставок'),
        ),
        migrations.AlterField(
            model_name='deposit',
            name='replenishment_ability',
            field=models.IntegerField(blank=True, help_text='Пополнение', null=True),
        ),
        migrations.AlterField(
            model_name='deposit',
            name='special_conditions',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), blank=True, help_text='Особые условия', null=True, size=None),
        ),
        migrations.AlterField(
            model_name='deposit',
            name='special_contribution',
            field=models.TextField(blank=True, help_text='Специальный вклад'),
        ),
        migrations.AlterField(
            model_name='deposit',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
