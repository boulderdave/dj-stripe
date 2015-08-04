# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djstripe', '0019_remove_account_stripe_account_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='bank_account_fingerprint',
            new_name='bank_account_token',
        ),
    ]
