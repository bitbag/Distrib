# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('distrib_api', '0032_auto_20160411_0954'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hosts',
            fields=[
                ('host_id', models.AutoField(serialize=False, primary_key=True)),
                ('host_name', models.TextField()),
                ('host_ip', models.CharField(max_length=20)),
                ('host_group', models.CharField(max_length=30)),
                ('remark', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Masters',
            fields=[
                ('master_id', models.AutoField(serialize=False, primary_key=True)),
                ('master_name', models.CharField(max_length=50)),
                ('master_ip', models.CharField(max_length=20)),
                ('master_location', models.CharField(max_length=30)),
                ('remark', models.CharField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='Host',
        ),
        migrations.DeleteModel(
            name='Master',
        ),
        migrations.AlterField(
            model_name='log',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 11, 13, 53, 16, 956000)),
        ),
        migrations.AlterField(
            model_name='log',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 11, 13, 53, 16, 956000)),
        ),
    ]
