# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-18 11:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0011_auto_20170403_0842'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='out_of_stock',
            field=models.BooleanField(default=False, help_text="If true, won't allow people to purchase and will display text saying out of stock"),
        ),
    ]