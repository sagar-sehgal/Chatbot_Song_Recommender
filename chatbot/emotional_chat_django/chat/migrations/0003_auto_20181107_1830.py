# Generated by Django 2.1.3 on 2018-11-07 18:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_auto_20181107_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='msg_text',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='message',
            name='msg_time',
            field=models.TimeField(default=datetime.datetime(2018, 11, 7, 18, 30, 36, 22956)),
        ),
    ]
