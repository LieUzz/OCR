# Generated by Django 2.1.7 on 2019-04-19 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ocr_api', '0002_userwordhistory_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userwordhistory',
            name='time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]