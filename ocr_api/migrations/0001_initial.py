# Generated by Django 2.1.7 on 2019-04-19 04:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usr_api', '0004_auto_20190417_1352'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserWordHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=16)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='usr_api.UserInfo')),
            ],
        ),
    ]
