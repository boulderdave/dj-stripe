# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djstripe', '0012_auto_20150728_2223'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='business_tax_id',
            new_name='legal_entity_business_tax_id',
        ),
        migrations.RenameField(
            model_name='account',
            old_name='business_vat_id',
            new_name='legal_entity_business_vat_id',
        ),
    ]
