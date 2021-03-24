from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Casino',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('url_self_casinoguru', models.URLField(blank=True)),
                ('name', models.CharField(blank=True, max_length=200)),
                ('images_logo', models.URLField(blank=True)),
            ],
            options={
                'ordering': ['-updated_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('url_self_casinoguru', models.URLField(blank=True)),
                ('name', models.CharField(blank=True, max_length=200)),
                ('iframe_original', models.URLField(blank=True)),
                ('iframe_fallback', models.URLField(blank=True)),
                ('images_logo', models.URLField(blank=True)),
                ('images_content', models.TextField(blank=True)),
                ('videos', models.TextField(blank=True)),
            ],
            options={
                'ordering': ['-updated_at'],
                'abstract': False,
            },
        ),
    ]
