# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('distrib_api', '0020_auto_20160406_1739'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hosts',
            fields=[
                ('note_host_id', models.IntegerField(serialize=False, primary_key=True)),
                ('note_host_ip', models.CharField(max_length=20)),
                ('host_group', models.CharField(max_length=30)),
                ('remark', models.CharField(max_length=30)),
                ('note_host_name', models.ForeignKey(to='distrib_api.Master')),
            ],
        ),
        migrations.AlterField(
            model_name='log',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 6, 17, 41, 20, 689000)),
        ),
        migrations.AlterField(
            model_name='log',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 6, 17, 41, 20, 689000)),
        ),
    ]
