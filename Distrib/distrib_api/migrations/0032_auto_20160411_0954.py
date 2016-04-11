# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('distrib_api', '0031_auto_20160408_1153'),
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('host_name', models.TextField()),
                ('host_ip', models.CharField(max_length=20)),
                ('host_group', models.CharField(max_length=30)),
                ('remark', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Master',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('master_host_name', models.CharField(max_length=50)),
                ('master_host_ip', models.CharField(max_length=20)),
                ('master_host_location', models.CharField(max_length=30)),
                ('remark', models.CharField(max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='hosts',
            name='host_name',
        ),
        migrations.RemoveField(
            model_name='playbook',
            name='p_name',
        ),
        migrations.RemoveField(
            model_name='playbook',
            name='p_type',
        ),
        migrations.AddField(
            model_name='playbook',
            name='play_name',
            field=models.CharField(default=None, max_length=40),
        ),
        migrations.AddField(
            model_name='playbook',
            name='play_type',
            field=models.CharField(default=None, max_length=30),
        ),
        migrations.AlterField(
            model_name='log',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 11, 9, 54, 0, 741000)),
        ),
        migrations.AlterField(
            model_name='log',
            name='mission',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='log',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 11, 9, 54, 0, 741000)),
        ),
        migrations.AlterField(
            model_name='miss',
            name='status',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='miss',
            name='type',
            field=models.TextField(),
        ),
        migrations.DeleteModel(
            name='Hosts',
        ),
        migrations.DeleteModel(
            name='Masters',
        ),
    ]
