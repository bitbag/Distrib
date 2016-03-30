# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('distrib_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('host_name', models.CharField(max_length=50)),
                ('host_ip', models.CharField(max_length=20)),
                ('host_group', models.CharField(max_length=30)),
                ('remark', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Master',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('host_name', models.CharField(max_length=50)),
                ('host_ip', models.CharField(max_length=20)),
                ('host_location', models.CharField(max_length=30)),
                ('remark', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Playbook',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('p_name', models.CharField(max_length=20)),
                ('p_type', models.ManyToManyField(to='distrib_api.Master')),
            ],
        ),
        migrations.AlterField(
            model_name='log',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 30, 15, 45, 52, 376000)),
        ),
        migrations.AlterField(
            model_name='log',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 30, 15, 45, 52, 376000)),
        ),
    ]
