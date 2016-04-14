# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('distrib_api', '0034_auto_20160414_0847'),
    ]

    operations = [
        migrations.AddField(
            model_name='miss',
            name='Release_date',
            field=models.CharField(default=None, max_length=30),
        ),
        migrations.AddField(
            model_name='submiss',
            name='Release_date',
            field=models.CharField(default=None, max_length=30),
        ),
        migrations.AlterField(
            model_name='log',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 14, 9, 0, 30, 426000)),
        ),
        migrations.AlterField(
            model_name='log',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 14, 9, 0, 30, 426000)),
        ),
    ]
