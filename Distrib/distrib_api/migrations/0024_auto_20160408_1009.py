# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('distrib_api', '0023_auto_20160407_0908'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hosts',
            old_name='note_host_id',
            new_name='host_id',
        ),
        migrations.RenameField(
            model_name='hosts',
            old_name='note_host_ip',
            new_name='host_ip',
        ),
        migrations.RenameField(
            model_name='hosts',
            old_name='note_host_name',
            new_name='host_name',
        ),
        migrations.AlterField(
            model_name='log',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 8, 10, 9, 44, 546000)),
        ),
        migrations.AlterField(
            model_name='log',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 8, 10, 9, 44, 546000)),
        ),
    ]
