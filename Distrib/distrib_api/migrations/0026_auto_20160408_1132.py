# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('distrib_api', '0025_auto_20160408_1013'),
    ]

    operations = [
        migrations.CreateModel(
            name='Masters',
            fields=[
                ('master_id', models.AutoField(serialize=False, primary_key=True)),
                ('master_host_name', models.CharField(max_length=50)),
                ('master_host_ip', models.CharField(max_length=20)),
                ('master_host_location', models.CharField(max_length=30)),
                ('remark', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='hosts',
            name='host_name',
            field=models.ForeignKey(to='distrib_api.Masters'),
        ),
        migrations.AlterField(
            model_name='log',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 8, 11, 32, 26, 587000)),
        ),
        migrations.AlterField(
            model_name='log',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 8, 11, 32, 26, 587000)),
        ),
        migrations.AlterField(
            model_name='playbook',
            name='p_type',
            field=models.ManyToManyField(to='distrib_api.Masters'),
        ),
        migrations.DeleteModel(
            name='Master',
        ),
    ]
