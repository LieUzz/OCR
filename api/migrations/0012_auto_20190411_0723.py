# Generated by Django 2.1.7 on 2019-04-11 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_recommendbook'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='age',
            field=models.CharField(default='', max_length=32),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='sex',
            field=models.CharField(default='', max_length=32),
        ),
    ]
