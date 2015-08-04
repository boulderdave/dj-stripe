# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djstripe', '0011_auto_20150728_2051'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='business_tax_id',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='account',
            name='business_vat_id',
            field=models.CharField(max_length=100, blank=True),
        ),
    ]
