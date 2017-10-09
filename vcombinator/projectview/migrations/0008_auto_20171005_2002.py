# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-05 20:02
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('projectview', '0007_auto_20171005_1856'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='northstar',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='round',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='tech_relm',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='tech_sub_relm',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='submission_date',
            field=models.DateField(default=datetime.datetime(2017, 10, 5, 20, 2, 26, 21201, tzinfo=utc)),
        ),
    ]
