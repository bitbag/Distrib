# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('distrib_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mission',
            options={'ordering': ['-created_date']},
        ),
        migrations.AlterField(
            model_name='mission',
            name='remark',
            field=models.TextField(blank=True),
        ),
    ]
