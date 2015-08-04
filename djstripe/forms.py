# -*- coding: utf-8 -*-
"""
.. module:: djstripe.forms
   :synopsis: dj-stripe Forms.

.. moduleauthor:: Daniel Greenfeld (@pydanny)

"""

from django import forms
from .settings import PLAN_CHOICES
from .models import Account


class PlanForm(forms.Form):
    plan = forms.ChoiceField(choices=PLAN_CHOICES)


class CancelSubscriptionForm(forms.Form):
    pass


class AccountForm(forms.ModelForm):

    class Meta:
        model = Account
        exclude = ('user', 'email', 'statement_descriptor', 'secret_key', 'publishable_key',
                   'display_name', 'timezone', 'details_submitted', 'charges_enabled',
                   'transfers_enabled', 'managed', 'debit_negative_balances',
                   'legal_entity_address_country', 'stripe_id', 'tos_acceptance_ip', 'tos_acceptance_date',
                   'bank_account_id', 'bank_account_last4')
