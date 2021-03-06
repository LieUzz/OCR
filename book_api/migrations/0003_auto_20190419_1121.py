# Generated by Django 2.1.7 on 2019-04-19 11:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book_api', '0002_favoritebook'),
    ]

    operations = [
        migrations.AddField(
            model_name='favoritebook',
            name='author',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.AddField(
            model_name='favoritebook',
            name='limage',
            field=models.CharField(default='', max_length=128),
        ),
        migrations.AddField(
            model_name='favoritebook',
            name='mimage',
            field=models.CharField(default='', max_length=128),
        ),
        migrations.AddField(
            model_name='favoritebook',
            name='publisher',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.AddField(
            model_name='favoritebook',
            name='simage',
            field=models.CharField(default='', max_length=128),
        ),
        migrations.AddField(
            model_name='favoritebook',
            name='summary',
            field=models.CharField(default='', max_length=1280),
        ),
        migrations.AddField(
            model_name='favoritebook',
            name='title',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='favoritebook',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='usr_api.UserInfo'),
        ),
    ]
