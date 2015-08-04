# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import localflavor.us.models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('djstripe', '0008_auto_20150728_1448'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='access_token',
            new_name='secret',
        ),
        migrations.RemoveField(
            model_name='account',
            name='name',
        ),
        migrations.RemoveField(
            model_name='account',
            name='refresh_token',
        ),
        migrations.AddField(
            model_name='account',
            name='bank_account_fingerprint',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='account',
            name='bank_account_id',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='account',
            name='bank_account_last4',
            field=models.CharField(max_length=4, blank=True),
        ),
        migrations.AddField(
            model_name='account',
            name='business_name',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='account',
            name='business_url',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='account',
            name='charges_enabled',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='account',
            name='debit_negative_balances',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='account',
            name='details_submitted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='account',
            name='display_name',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='account',
            name='dob_day',
            field=models.PositiveSmallIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(31), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AddField(
            model_name='account',
            name='dob_month',
            field=models.PositiveSmallIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(12), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AddField(
            model_name='account',
            name='dob_year',
            field=models.PositiveSmallIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(2100), django.core.validators.MinValueValidator(1915)]),
        ),
        migrations.AddField(
            model_name='account',
            name='legal_entity_address_city',
            field=models.CharField(max_length=500, blank=True),
        ),
        migrations.AddField(
            model_name='account',
            name='legal_entity_address_country',
            field=models.CharField(max_length=2, blank=True),
        ),
        migrations.AddField(
            model_name='account',
            name='legal_entity_address_line1',
            field=models.CharField(max_length=150, blank=True),
        ),
        migrations.AddField(
            model_name='account',
            name='legal_entity_address_line2',
            field=models.CharField(max_length=150, blank=True),
        ),
        migrations.AddField(
            model_name='account',
            name='legal_entity_address_postal_code',
            field=localflavor.us.models.USZipCodeField(default='', max_length=10, blank=True),
        ),
        migrations.AddField(
            model_name='account',
            name='legal_entity_address_state',
            field=localflavor.us.models.USStateField(default='', max_length=2, blank=True, choices=[(b'AL', b'Alabama'), (b'AK', b'Alaska'), (b'AS', b'American Samoa'), (b'AZ', b'Arizona'), (b'AR', b'Arkansas'), (b'AA', b'Armed Forces Americas'), (b'AE', b'Armed Forces Europe'), (b'AP', b'Armed Forces Pacific'), (b'CA', b'California'), (b'CO', b'Colorado'), (b'CT', b'Connecticut'), (b'DE', b'Delaware'), (b'DC', b'District of Columbia'), (b'FL', b'Florida'), (b'GA', b'Georgia'), (b'GU', b'Guam'), (b'HI', b'Hawaii'), (b'ID', b'Idaho'), (b'IL', b'Illinois'), (b'IN', b'Indiana'), (b'IA', b'Iowa'), (b'KS', b'Kansas'), (b'KY', b'Kentucky'), (b'LA', b'Louisiana'), (b'ME', b'Maine'), (b'MD', b'Maryland'), (b'MA', b'Massachusetts'), (b'MI', b'Michigan'), (b'MN', b'Minnesota'), (b'MS', b'Mississippi'), (b'MO', b'Missouri'), (b'MT', b'Montana'), (b'NE', b'Nebraska'), (b'NV', b'Nevada'), (b'NH', b'New Hampshire'), (b'NJ', b'New Jersey'), (b'NM', b'New Mexico'), (b'NY', b'New York'), (b'NC', b'North Carolina'), (b'ND', b'North Dakota'), (b'MP', b'Northern Mariana Islands'), (b'OH', b'Ohio'), (b'OK', b'Oklahoma'), (b'OR', b'Oregon'), (b'PA', b'Pennsylvania'), (b'PR', b'Puerto Rico'), (b'RI', b'Rhode Island'), (b'SC', b'South Carolina'), (b'SD', b'South Dakota'), (b'TN', b'Tennessee'), (b'TX', b'Texas'), (b'UT', b'Utah'), (b'VT', b'Vermont'), (b'VI', b'Virgin Islands'), (b'VA', b'Virginia'), (b'WA', b'Washington'), (b'WV', b'West Virginia'), (b'WI', b'Wisconsin'), (b'WY', b'Wyoming')]),
        ),
        migrations.AddField(
            model_name='account',
            name='legal_entity_business_name',
            field=models.CharField(max_length=150, blank=True),
        ),
        migrations.AddField(
            model_name='account',
            name='legal_entity_type',
            field=models.CharField(default='', max_length=50, choices=[('individual', 'Individual'), ('company', 'Company')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='account',
            name='managed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='account',
            name='personal_address_city',
            field=models.CharField(max_length=500, blank=True),
        ),
        migrations.AddField(
            model_name='account',
            name='personal_address_country',
            field=models.CharField(max_length=2, blank=True),
        ),
        migrations.AddField(
            model_name='account',
            name='personal_address_line1',
            field=models.CharField(max_length=150, blank=True),
        ),
        migrations.AddField(
            model_name='account',
            name='personal_address_line2',
            field=models.CharField(max_length=150, blank=True),
        ),
        migrations.AddField(
            model_name='account',
            name='personal_address_postal_code',
            field=localflavor.us.models.USZipCodeField(default='', max_length=10, blank=True),
        ),
        migrations.AddField(
            model_name='account',
            name='personal_address_state',
            field=localflavor.us.models.USStateField(default='', max_length=2, blank=True, choices=[(b'AL', b'Alabama'), (b'AK', b'Alaska'), (b'AS', b'American Samoa'), (b'AZ', b'Arizona'), (b'AR', b'Arkansas'), (b'AA', b'Armed Forces Americas'), (b'AE', b'Armed Forces Europe'), (b'AP', b'Armed Forces Pacific'), (b'CA', b'California'), (b'CO', b'Colorado'), (b'CT', b'Connecticut'), (b'DE', b'Delaware'), (b'DC', b'District of Columbia'), (b'FL', b'Florida'), (b'GA', b'Georgia'), (b'GU', b'Guam'), (b'HI', b'Hawaii'), (b'ID', b'Idaho'), (b'IL', b'Illinois'), (b'IN', b'Indiana'), (b'IA', b'Iowa'), (b'KS', b'Kansas'), (b'KY', b'Kentucky'), (b'LA', b'Louisiana'), (b'ME', b'Maine'), (b'MD', b'Maryland'), (b'MA', b'Massachusetts'), (b'MI', b'Michigan'), (b'MN', b'Minnesota'), (b'MS', b'Mississippi'), (b'MO', b'Missouri'), (b'MT', b'Montana'), (b'NE', b'Nebraska'), (b'NV', b'Nevada'), (b'NH', b'New Hampshire'), (b'NJ', b'New Jersey'), (b'NM', b'New Mexico'), (b'NY', b'New York'), (b'NC', b'North Carolina'), (b'ND', b'North Dakota'), (b'MP', b'Northern Mariana Islands'), (b'OH', b'Ohio'), (b'OK', b'Oklahoma'), (b'OR', b'Oregon'), (b'PA', b'Pennsylvania'), (b'PR', b'Puerto Rico'), (b'RI', b'Rhode Island'), (b'SC', b'South Carolina'), (b'SD', b'South Dakota'), (b'TN', b'Tennessee'), (b'TX', b'Texas'), (b'UT', b'Utah'), (b'VT', b'Vermont'), (b'VI', b'Virgin Islands'), (b'VA', b'Virginia'), (b'WA', b'Washington'), (b'WV', b'West Virginia'), (b'WI', b'Wisconsin'), (b'WY', b'Wyoming')]),
        ),
        migrations.AddField(
            model_name='account',
            name='product_description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='account',
            name='statement_description',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='account',
            name='stripe_account_id',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='account',
            name='support_phone',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AddField(
            model_name='account',
            name='timezone',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='account',
            name='transfers_enabled',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='event',
            name='account',
            field=models.ForeignKey(to='djstripe.Account', null=True),
        ),
    ]
