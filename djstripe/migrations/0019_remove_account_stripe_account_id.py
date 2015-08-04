# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djstripe', '0018_auto_20150729_1849'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='stripe_account_id',
        ),
    ]
