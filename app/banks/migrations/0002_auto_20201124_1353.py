# Generated by Django 3.0.11 on 2020-11-24 10:53

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('banks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='creditcard',
            name='images',
        ),
        migrations.AddField(
            model_name='creditcard',
            name='images',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
        migrations.RemoveField(
            model_name='debitcard',
            name='images',
        ),
        migrations.AddField(
            model_name='debitcard',
            name='images',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
    ]
