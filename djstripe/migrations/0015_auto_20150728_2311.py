# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djstripe', '0014_auto_20150728_2228'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='dob_day',
            new_name='legal_entity_dob_day',
        ),
        migrations.RenameField(
            model_name='account',
            old_name='dob_month',
            new_name='legal_entity_dob_month',
        ),
        migrations.RenameField(
            model_name='account',
            old_name='dob_year',
            new_name='legal_entity_dob_year',
        ),
    ]
