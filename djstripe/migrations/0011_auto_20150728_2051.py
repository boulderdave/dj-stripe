# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djstripe', '0010_auto_20150728_1957'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='legal_entity_first_name',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AddField(
            model_name='account',
            name='legal_entity_last_name',
            field=models.CharField(max_length=50, blank=True),
        ),
    ]
