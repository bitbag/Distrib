# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('distrib_api', '0002_auto_20160330_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host',
            name='host_name',
            field=models.ForeignKey(to='distrib_api.Master'),
        ),
        migrations.AlterField(
            model_name='log',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 31, 9, 0, 2, 168000)),
        ),
        migrations.AlterField(
            model_name='log',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 31, 9, 0, 2, 168000)),
        ),
    ]
