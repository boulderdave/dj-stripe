# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djstripe', '0013_auto_20150728_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='legal_entity_type',
            field=models.CharField(default='individual', max_length=50, choices=[('individual', 'Individual'), ('company', 'Company')]),
        ),
    ]
