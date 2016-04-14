# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('distrib_api', '0033_auto_20160411_1353'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubMiss',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('host', models.CharField(max_length=15)),
                ('playbooks', models.TextField()),
                ('version', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=20)),
                ('remark', models.CharField(max_length=80, blank=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Service_type',
        ),
        migrations.DeleteModel(
            name='Status',
        ),
        migrations.RenameField(
            model_name='miss',
            old_name='group',
            new_name='hosts',
        ),
        migrations.RenameField(
            model_name='miss',
            old_name='type',
            new_name='playbooks',
        ),
        migrations.AlterField(
            model_name='log',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 14, 8, 47, 10, 27000)),
        ),
        migrations.AlterField(
            model_name='log',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 14, 8, 47, 10, 27000)),
        ),
        migrations.AlterField(
            model_name='miss',
            name='remark',
            field=models.CharField(max_length=80, blank=True),
        ),
        migrations.AlterField(
            model_name='miss',
            name='version',
            field=models.CharField(max_length=50),
        ),
    ]
