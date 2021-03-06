# Generated by Django 2.1.7 on 2019-04-19 11:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0031_auto_20190415_0625'),
    ]

    operations = [
        migrations.CreateModel(
            name='FavoriteBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=64)),
                ('author', models.CharField(default='', max_length=64)),
                ('publisher', models.CharField(default='', max_length=64)),
                ('isbn', models.CharField(default='', max_length=64)),
                ('summary', models.CharField(default='', max_length=1280)),
                ('simage', models.CharField(default='', max_length=128)),
                ('mimage', models.CharField(default='', max_length=128)),
                ('limage', models.CharField(default='', max_length=128)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.UserInfo')),
            ],
        ),
    ]
