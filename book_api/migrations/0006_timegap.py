# Generated by Django 2.1.7 on 2019-04-20 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usr_api', '0004_auto_20190417_1352'),
        ('book_api', '0005_auto_20190420_1447'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeGap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lasttime', models.IntegerField(default=0, max_length=16)),
                ('one', models.IntegerField(default=0, max_length=16)),
                ('two', models.IntegerField(default=0, max_length=16)),
                ('three', models.IntegerField(default=0, max_length=16)),
                ('four', models.IntegerField(default=0, max_length=16)),
                ('five', models.IntegerField(default=0, max_length=16)),
                ('six', models.IntegerField(default=0, max_length=16)),
                ('seven', models.IntegerField(default=0, max_length=16)),
                ('eight', models.IntegerField(default=0, max_length=16)),
                ('nine', models.IntegerField(default=0, max_length=16)),
                ('ten', models.IntegerField(default=0, max_length=16)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='usr_api.UserInfo')),
            ],
        ),
    ]