# Generated by Django 3.0.6 on 2020-05-20 12:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0002_auto_20200520_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='pub_date',
            field=models.DateTimeField(null=True, verbose_name=datetime.datetime(2020, 5, 20, 12, 47, 32, 411398, tzinfo=utc)),
        ),
    ]