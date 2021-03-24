from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casino', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slot',
            name='images_content',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='slot',
            name='videos',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
