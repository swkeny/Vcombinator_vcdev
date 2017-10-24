# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-17 15:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projectview', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='project',
            name='northstar',
            field=models.CharField(choices=[('alpha', 'More Efficient and New Sources of Alpha'), ('cost', 'Lower Cost to Invest'), ('markets', 'Enable New Markets'), ('risk', 'Eliminate Uncompensated Risk'), ('structure', 'New Market Structures'), ('culture', 'Build and Enable Innovative Culture')], max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='tech_relm',
            field=models.CharField(choices=[('DATA', 'Data Analytics'), ('PLAT', 'Platforms/Visualization'), ('INFRA', 'Market Infrastructure')], max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='tech_sub_relm',
            field=models.CharField(choices=[('DLT', 'Distributed Ledger Technology'), ('PYT', 'Python'), ('DNJ', 'Django')], max_length=64, null=True),
        ),
    ]
