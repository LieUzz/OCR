# Generated by Django 2.1.7 on 2019-04-15 06:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0029_auto_20190413_1104'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserWordHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=16)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.UserInfo')),
            ],
        ),
    ]
