# Generated by Django 2.1.3 on 2018-11-07 18:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_auto_20181107_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='msg_time',
            field=models.TimeField(default=datetime.datetime(2018, 11, 7, 18, 33, 37, 714043, tzinfo=utc)),
        ),
    ]