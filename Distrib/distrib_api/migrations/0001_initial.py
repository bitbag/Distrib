# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='log',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_time', models.DateTimeField(default=datetime.datetime(2016, 3, 29, 13, 58, 45, 37000))),
                ('end_time', models.DateTimeField(default=datetime.datetime(2016, 3, 29, 13, 58, 45, 37000))),
                ('status', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Miss',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('group', models.TextField()),
                ('version', models.CharField(max_length=80)),
                ('remark', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Service_type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('alise', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('alise', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='miss',
            name='status',
            field=models.ForeignKey(to='distrib_api.Status'),
        ),
        migrations.AddField(
            model_name='miss',
            name='type',
            field=models.ForeignKey(to='distrib_api.Service_type'),
        ),
        migrations.AddField(
            model_name='log',
            name='mission',
            field=models.ForeignKey(to='distrib_api.Miss'),
        ),
    ]
