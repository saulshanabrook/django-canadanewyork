# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Press.slug'
        db.alter_column('press_press', 'slug', self.gf('^apps\\.slugify\\.fields\\.SlugifyField')(max_length=50, populate_from=('title',)))

    def backwards(self, orm):

        # Changing field 'Press.slug'
        db.alter_column('press_press', 'slug', self.gf('django.db.models.fields.SlugField')(max_length=50))

    models = {
        'artists.artist': {
            'Meta': {'ordering': "['last_name', 'first_name']", 'unique_together': "(('first_name', 'last_name'),)", 'object_name': 'Artist'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'resume': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'slug': ('^apps\\.slugify\\.fields\\.SlugifyField', [], {'max_length': '50', 'populate_from': "('first_name', 'last_name')"}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        'exhibitions.exhibition': {
            'Meta': {'ordering': "['-start_date']", 'object_name': 'Exhibition'},
            'artists': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'exhibitions'", 'symmetrical': 'False', 'to': "orm['artists.Artist']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'slug': ('^apps\\.slugify\\.fields\\.SlugifyField', [], {'max_length': '50', 'populate_from': "('name',)"}),
            'start_date': ('django.db.models.fields.DateField', [], {})
        },
        'press.press': {
            'Meta': {'ordering': "['-date']", 'object_name': 'Press'},
            'artists': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'press'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['artists.Artist']"}),
            'author': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'exhibition': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'press'", 'null': 'True', 'to': "orm['exhibitions.Exhibition']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'image_height': ('django.db.models.fields.IntegerField', [], {'default': '500'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'publisher': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'slug': ('^apps\\.slugify\\.fields\\.SlugifyField', [], {'max_length': '50', 'populate_from': "('title',)"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['press']