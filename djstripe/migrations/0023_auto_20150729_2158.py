# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djstripe', '0022_auto_20150729_2144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='tos_acceptance_date',
            field=models.DateTimeField(null=True),
        ),
    ]
