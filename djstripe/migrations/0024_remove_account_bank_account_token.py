# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djstripe', '0023_auto_20150729_2158'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='bank_account_token',
        ),
    ]
