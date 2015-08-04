# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djstripe', '0021_auto_20150729_2122'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='tos_acceptance_date',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='tos_acceptance_ip',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='statement_descriptor',
            field=models.CharField(default='Droners.io', max_length=100, blank=True),
        ),
    ]
