# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-22 11:11
from __future__ import unicode_literals

import apps.photos.models
from django.db import migrations, models
import django.db.models.deletion
import libs.ckeditor.fields
import url_tracker.mixins


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Update',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', libs.ckeditor.fields.CKEditorField(blank=True)),
                ('post_date', models.DateField(verbose_name='Date')),
            ],
            options={
                'ordering': ['-post_date'],
            },
            bases=(url_tracker.mixins.URLTrackingMixin, models.Model),
        ),
        migrations.CreateModel(
            name='UpdatePhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=400)),
                ('caption', models.TextField(blank=True, verbose_name='Extra Text')),
                ('image', models.ImageField(max_length=1000, upload_to=apps.photos.models.original_image_path_function, verbose_name='Image File')),
                ('thumbnail_image', models.ImageField(blank=True, editable=False, height_field='thumbnail_image_height', max_length=1000, null=True, upload_to=apps.photos.models.thumbnail_image_path_function, width_field='thumbnail_image_width')),
                ('large_image', models.ImageField(blank=True, editable=False, height_field='large_image_height', max_length=1000, null=True, upload_to=apps.photos.models.large_image_path_function, width_field='large_image_width')),
                ('thumbnail_image_height', models.PositiveIntegerField(blank=True, editable=False, null=True)),
                ('thumbnail_image_width', models.PositiveIntegerField(blank=True, editable=False, null=True)),
                ('large_image_height', models.PositiveIntegerField(blank=True, editable=False, null=True)),
                ('large_image_width', models.PositiveIntegerField(blank=True, editable=False, null=True)),
                ('position', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='')),
                ('content_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='updates.Update')),
            ],
            options={
                'abstract': False,
                'ordering': ['position'],
            },
        ),
    ]
