# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-08 14:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('updates', '0002_auto_20160108_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='updatephoto',
            name='position',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
