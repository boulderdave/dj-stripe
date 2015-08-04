# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djstripe', '0020_auto_20150729_2057'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='statement_description',
            new_name='statement_descriptor',
        ),
    ]
