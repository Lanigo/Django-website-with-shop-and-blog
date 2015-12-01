# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='AcrylicPainting',
            fields=[
                ('product_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='shop.Product')),
                ('picture', models.ImageField(upload_to=b'img/acrylic')),
                ('medium', models.CharField(default=0, max_length=30)),
                ('height', models.IntegerField(default=0)),
                ('width', models.IntegerField(default=0)),
                ('short_description', models.CharField(default=0, max_length=255)),
                ('long_description', models.TextField(null=True, blank=True)),
            ],
            options={
                'ordering': ['date_added'],
            },
            bases=('shop.product',),
        ),
        migrations.CreateModel(
            name='OilPainting',
            fields=[
                ('product_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='shop.Product')),
                ('picture', models.ImageField(upload_to=b'img/oil')),
                ('medium', models.CharField(default=0, max_length=30)),
                ('height', models.IntegerField(default=0)),
                ('width', models.IntegerField(default=0)),
                ('short_description', models.CharField(default=0, max_length=255)),
                ('long_description', models.TextField(null=True, blank=True)),
            ],
            options={
                'ordering': ['date_added'],
            },
            bases=('shop.product',),
        ),
        migrations.CreateModel(
            name='PastelDrawing',
            fields=[
                ('product_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='shop.Product')),
                ('picture', models.ImageField(upload_to=b'img/pastel')),
                ('medium', models.CharField(default=0, max_length=30)),
                ('height', models.IntegerField(default=0)),
                ('width', models.IntegerField(default=0)),
                ('short_description', models.CharField(default=0, max_length=255)),
                ('long_description', models.TextField(null=True, blank=True)),
            ],
            options={
                'ordering': ['date_added'],
            },
            bases=('shop.product',),
        ),
        migrations.CreateModel(
            name='PencilSketch',
            fields=[
                ('product_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='shop.Product')),
                ('picture', models.ImageField(upload_to=b'img/pencil')),
                ('medium', models.CharField(default=0, max_length=30)),
                ('height', models.IntegerField(default=0)),
                ('width', models.IntegerField(default=0)),
                ('short_description', models.CharField(default=0, max_length=255)),
                ('long_description', models.TextField(null=True, blank=True)),
            ],
            options={
                'ordering': ['date_added'],
                'verbose_name_plural': 'pencil sketches',
            },
            bases=('shop.product',),
        ),
    ]
