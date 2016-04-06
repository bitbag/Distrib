# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('distrib_api', '0019_auto_20160406_1427'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='host',
            name='note_host_name',
        ),
        migrations.RenameField(
            model_name='service_type',
            old_name='alise',
            new_name='alias',
        ),
        migrations.RenameField(
            model_name='status',
            old_name='alise',
            new_name='alias',
        ),
        migrations.AlterField(
            model_name='log',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 6, 17, 38, 52, 748000)),
        ),
        migrations.AlterField(
            model_name='log',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 6, 17, 38, 52, 748000)),
        ),
        migrations.DeleteModel(
            name='Host',
        ),
    ]
