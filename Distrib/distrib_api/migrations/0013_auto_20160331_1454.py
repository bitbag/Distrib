# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('distrib_api', '0012_auto_20160331_1453'),
    ]

    operations = [
        migrations.RenameField(
            model_name='host',
            old_name='host_ip',
            new_name='note_host_ip',
        ),
        migrations.RenameField(
            model_name='host',
            old_name='host_name',
            new_name='note_host_name',
        ),
        migrations.AlterField(
            model_name='log',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 31, 14, 54, 46, 568000)),
        ),
        migrations.AlterField(
            model_name='log',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 31, 14, 54, 46, 568000)),
        ),
    ]
