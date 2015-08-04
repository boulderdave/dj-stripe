# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djstripe', '0015_auto_20150728_2311'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='legal_entity_ssn_last_4',
            field=models.CharField(max_length=4, blank=True),
        ),
    ]
