# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-05 18:55
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectview', '0005_auto_20171005_1847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='submission_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 5, 18, 55, 2, 452229)),
        ),
    ]
