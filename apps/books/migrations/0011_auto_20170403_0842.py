# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-03 08:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0010_bookphoto_gfycat_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.PositiveSmallIntegerField(blank=True, help_text='If blank, will not show buy button.', null=True),
        ),
    ]
