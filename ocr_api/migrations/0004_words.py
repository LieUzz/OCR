# Generated by Django 2.1.7 on 2019-04-23 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ocr_api', '0003_auto_20190419_0439'),
    ]

    operations = [
        migrations.CreateModel(
            name='Words',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zi', models.CharField(max_length=16)),
                ('pinyin', models.CharField(default='', max_length=64)),
                ('bihua', models.CharField(default='', max_length=16)),
                ('pianpang', models.CharField(default='', max_length=16)),
                ('yisi1', models.CharField(default='', max_length=512)),
                ('yisi2', models.CharField(default='', max_length=512)),
                ('yisi3', models.CharField(default='', max_length=512)),
            ],
        ),
    ]
