# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('theshop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyAddress',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('address', models.CharField(max_length=255, verbose_name='Address')),
                ('address2', models.CharField(max_length=255, verbose_name='Address2', blank=True)),
                ('postal_code', models.CharField(max_length=20, verbose_name='Postal Code')),
                ('city', models.CharField(max_length=20, verbose_name='City')),
                ('province', models.CharField(max_length=255, verbose_name='Province')),
                ('user_billing', models.OneToOneField(related_name='address_billing', null=True, blank=True, to=settings.AUTH_USER_MODEL)),
                ('user_shipping', models.OneToOneField(related_name='address_shipping', null=True, blank=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Address',
                'verbose_name_plural': 'Addresses',
            },
        ),
    ]
