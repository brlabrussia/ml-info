# Generated by Django 3.1.4 on 2020-12-21 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investments', '0005_mutual'),
    ]

    operations = [
        migrations.AddField(
            model_name='iia',
            name='docs',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
