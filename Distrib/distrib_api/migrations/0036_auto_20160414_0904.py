# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('distrib_api', '0035_auto_20160414_0900'),
    ]

    operations = [
        migrations.RenameField(
            model_name='miss',
            old_name='Release_date',
            new_name='finish_time',
        ),
        migrations.RenameField(
            model_name='submiss',
            old_name='Release_date',
            new_name='finish_time',
        ),
        migrations.AddField(
            model_name='miss',
            name='release_time',
            field=models.CharField(default=None, max_length=30),
        ),
        migrations.AddField(
            model_name='submiss',
            name='release_time',
            field=models.CharField(default=None, max_length=30),
        ),
        migrations.AlterField(
            model_name='log',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 14, 9, 4, 9, 729000)),
        ),
        migrations.AlterField(
            model_name='log',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 14, 9, 4, 9, 729000)),
        ),
    ]
