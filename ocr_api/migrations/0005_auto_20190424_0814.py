# Generated by Django 2.1.7 on 2019-04-24 08:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ocr_api', '0004_words'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userwordhistory',
            name='word',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='tool.Word'),
        ),
    ]