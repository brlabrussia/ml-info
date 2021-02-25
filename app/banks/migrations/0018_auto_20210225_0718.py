from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('banks', '0017_auto_20210225_0602'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='branch',
            options={'ordering': ['-updated_at']},
        ),
        migrations.RenameField(
            model_name='branch',
            old_name='banki_id',
            new_name='id_self_banki',
        ),
        migrations.RenameField(
            model_name='branch',
            old_name='bank_url',
            new_name='url_bank_banki',
        ),
        migrations.AddField(
            model_name='branch',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='branch',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='branch',
            name='bank',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='banks.bank'),
        ),
    ]
