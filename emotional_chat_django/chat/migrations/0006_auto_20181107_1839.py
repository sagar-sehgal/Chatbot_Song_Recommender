# Generated by Django 2.1.3 on 2018-11-07 18:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0005_auto_20181107_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='msg_time',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]
