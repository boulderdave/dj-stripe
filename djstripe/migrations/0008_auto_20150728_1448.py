# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('djstripe', '0007_auto_20150625_1243'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('stripe_id', models.CharField(unique=True, max_length=50)),
                ('publishable_key', models.CharField(max_length=200)),
                ('access_token', models.CharField(max_length=200)),
                ('refresh_token', models.CharField(max_length=200, blank=True)),
                ('name', models.CharField(max_length=200, blank=True)),
                ('email', models.EmailField(max_length=254, blank=True)),
                ('user', models.OneToOneField(null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='customer',
            name='account',
            field=models.ForeignKey(to='djstripe.Account', null=True),
        ),
        migrations.AddField(
            model_name='plan',
            name='account',
            field=models.ForeignKey(to='djstripe.Account', null=True),
        ),
        migrations.AddField(
            model_name='transfer',
            name='account',
            field=models.ForeignKey(to='djstripe.Account', null=True),
        ),
    ]
