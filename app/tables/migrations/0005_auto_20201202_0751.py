# Generated by Django 3.1.4 on 2020-12-02 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0004_auto_20201130_0004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='result',
            field=models.JSONField(blank=True, default=dict),
        ),
        migrations.AlterField(
            model_name='table',
            name='spider_kwargs',
            field=models.JSONField(blank=True, default=dict),
        ),
    ]
