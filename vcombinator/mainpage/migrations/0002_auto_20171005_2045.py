# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-05 20:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectimage',
            name='project_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectview.Project'),
        ),
    ]
