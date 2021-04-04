from django.db import migrations, models


def populate_from_tables(apps, schema_editor):
    copylist = (
        'category',
        'name',
        'url',
        'description',
        'spider',
        'spider_kwargs',
    )
    Ranking = apps.get_model('rankings', 'Ranking')
    Table = apps.get_model('tables', 'Table')
    rankings = []
    for table_dict in Table.objects.values():
        rankings.append(Ranking(**{
            k: v
            for k, v in table_dict.items()
            if k in copylist
        }))
    Ranking.objects.bulk_create(rankings)


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('tables', '0005_auto_20201202_0751'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ranking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.TextField()),
                ('name', models.TextField()),
                ('url', models.URLField()),
                ('description', models.TextField(blank=True)),
                ('spider', models.TextField(blank=True)),
                ('spider_kwargs', models.JSONField(blank=True, default=dict)),
                ('result', models.JSONField(blank=True, null=True)),
            ],
            options={
                'ordering': ['-category'],
            },
        ),
        migrations.RunPython(populate_from_tables, migrations.RunPython.noop),
    ]
