# Generated by Django 3.1.4 on 2020-12-02 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banks', '0003_auto_20201202_0623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consumercredit',
            name='rates_table',
            field=models.JSONField(blank=True, default=dict),
        ),
        migrations.AlterField(
            model_name='creditcard',
            name='foreign_cash_pickup_point',
            field=models.JSONField(blank=True, default=dict),
        ),
        migrations.AlterField(
            model_name='creditcard',
            name='foreign_cash_withdrawal',
            field=models.JSONField(blank=True, default=dict),
        ),
        migrations.AlterField(
            model_name='creditcard',
            name='images',
            field=models.JSONField(blank=True, default=dict),
        ),
        migrations.AlterField(
            model_name='creditcard',
            name='interest_accrual',
            field=models.JSONField(blank=True, default=dict),
        ),
        migrations.AlterField(
            model_name='creditcard',
            name='operations_limit',
            field=models.JSONField(blank=True, default=dict),
        ),
        migrations.AlterField(
            model_name='creditcard',
            name='service_cost',
            field=models.JSONField(blank=True, default=dict),
        ),
        migrations.AlterField(
            model_name='debitcard',
            name='foreign_cash_pickup_point',
            field=models.JSONField(blank=True, default=dict),
        ),
        migrations.AlterField(
            model_name='debitcard',
            name='foreign_cash_withdrawal',
            field=models.JSONField(blank=True, default=dict),
        ),
        migrations.AlterField(
            model_name='debitcard',
            name='images',
            field=models.JSONField(blank=True, default=dict),
        ),
        migrations.AlterField(
            model_name='debitcard',
            name='interest_accrual',
            field=models.JSONField(blank=True, default=dict),
        ),
        migrations.AlterField(
            model_name='debitcard',
            name='operations_limit',
            field=models.JSONField(blank=True, default=dict),
        ),
        migrations.AlterField(
            model_name='debitcard',
            name='service_cost',
            field=models.JSONField(blank=True, default=dict),
        ),
        migrations.AlterField(
            model_name='deposit',
            name='rates_table',
            field=models.JSONField(blank=True, default=dict),
        ),
    ]
