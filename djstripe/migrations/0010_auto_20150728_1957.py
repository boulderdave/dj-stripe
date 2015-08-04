# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djstripe', '0009_auto_20150728_1921'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='secret',
            new_name='secret_key',
        ),
    ]
