from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'ordering': ['-updated_at']},
        ),
        migrations.AddField(
            model_name='company',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='address',
            field=models.CharField(blank=True, help_text='Физический адрес организации', max_length=200),
        ),
        migrations.AlterField(
            model_name='company',
            name='authorized_capital',
            field=models.PositiveIntegerField(blank=True, help_text='Уставный капитал', null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='cbrn',
            field=models.CharField(help_text='Регистрационный номер ЦБ', max_length=4),
        ),
        migrations.AlterField(
            model_name='company',
            name='contacts',
            field=models.TextField(blank=True, help_text='Контакты из реестра'),
        ),
        migrations.AlterField(
            model_name='company',
            name='director',
            field=models.CharField(blank=True, help_text='Имя директора', max_length=200),
        ),
        migrations.AlterField(
            model_name='company',
            name='director_date',
            field=models.DateTimeField(blank=True, help_text='Дата информации на основании которой указан директор', null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='federal_subject',
            field=models.CharField(blank=True, help_text='Федеральный субъект', max_length=200),
        ),
        migrations.AlterField(
            model_name='company',
            name='inn',
            field=models.CharField(blank=True, help_text='ИНН', max_length=10),
        ),
        migrations.AlterField(
            model_name='company',
            name='licenses',
            field=models.JSONField(blank=True, help_text='Лицензии компании', null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.URLField(blank=True, help_text='Ссылка на логотип c банки.ру'),
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(blank=True, help_text='Название из реестра ЦБ', max_length=200),
        ),
        migrations.AlterField(
            model_name='company',
            name='net_profit',
            field=models.PositiveIntegerField(blank=True, help_text='Чистая прибыль', null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='ogrn',
            field=models.CharField(blank=True, help_text='ОГРН', max_length=13),
        ),
        migrations.AlterField(
            model_name='company',
            name='payouts',
            field=models.PositiveIntegerField(blank=True, help_text='Объем выплат', null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='premiums',
            field=models.PositiveIntegerField(blank=True, help_text='Объем премий', null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='trademark',
            field=models.CharField(blank=True, help_text='"Красивое" название как на банки.ру', max_length=200),
        ),
    ]
