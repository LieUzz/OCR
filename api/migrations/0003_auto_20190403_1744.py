# Generated by Django 2.1.7 on 2019-04-03 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_userinfo_mail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='phone',
            field=models.IntegerField(default=0, max_length=64),
        ),
    ]
