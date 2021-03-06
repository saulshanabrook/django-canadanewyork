# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-22 11:11
from __future__ import unicode_literals

import apps.press.models
from django.db import migrations, models
import django.db.models.deletion
import libs.ckeditor.fields
import libs.slugify.fields
import url_tracker.mixins


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('exhibitions', '0001_initial'),
        ('artists', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Press',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=500)),
                ('content', libs.ckeditor.fields.CKEditorField(blank=True)),
                ('content_file', models.FileField(blank=True, max_length=500, null=True, upload_to=apps.press.models.file_path)),
                ('content_link', models.URLField(blank=True)),
                ('date', models.DateField(help_text='Used for ordering', verbose_name='Precise Date')),
                ('date_text', models.CharField(blank=True, help_text='If set, will display <strong>instead of</strong> the precise date.', max_length=500, verbose_name='Imprecise Date')),
                ('publisher', models.CharField(blank=True, max_length=50)),
                ('author', models.CharField(blank=True, max_length=500)),
                ('pages_range', models.CharField(blank=True, max_length=50)),
                ('slug', libs.slugify.fields.SlugifyField(max_length=251, populate_from=('date_year', 'slug_title'), slug_template='{}/{}', unique=True)),
                ('artist', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='press', to='artists.Artist')),
                ('exhibition', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='press', to='exhibitions.Exhibition')),
            ],
            options={
                'verbose_name_plural': 'press',
                'ordering': ['-date'],
            },
            bases=(url_tracker.mixins.URLTrackingMixin, models.Model),
        ),
        migrations.AlterUniqueTogether(
            name='press',
            unique_together=set([('publisher', 'title', 'artist', 'exhibition')]),
        ),
    ]
