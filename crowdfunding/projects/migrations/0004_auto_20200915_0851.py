# Generated by Django 3.0.8 on 2020-09-15 08:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20200911_2341'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='date_updated',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 15, 8, 51, 17, 547170, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='project',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]