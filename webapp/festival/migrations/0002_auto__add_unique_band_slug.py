# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding unique constraint on 'Band', fields ['slug']
        db.create_unique(u'festival_band', ['slug'])


    def backwards(self, orm):
        # Removing unique constraint on 'Band', fields ['slug']
        db.delete_unique(u'festival_band', ['slug'])


    models = {
        u'festival.band': {
            'Meta': {'object_name': 'Band'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'genre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'slug': ('django.db.models.fields.SlugField', [], {'default': "'-'", 'unique': 'True', 'max_length': '50'})
        },
        u'festival.bandlinks': {
            'Meta': {'object_name': 'BandLinks'},
            'band': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['festival.Band']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'WS'", 'max_length': '20'})
        },
        u'festival.bandyear': {
            'Meta': {'object_name': 'BandYear'},
            'band': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['festival.Band']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'stage': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'time': ('django.db.models.fields.DateTimeField', [], {}),
            'year': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['festival.Year']"})
        },
        u'festival.year': {
            'Meta': {'ordering': "['year']", 'object_name': 'Year'},
            'bands': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'years'", 'symmetrical': 'False', 'through': u"orm['festival.BandYear']", 'to': u"orm['festival.Band']"}),
            'end': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'start': ('django.db.models.fields.DateField', [], {}),
            'year': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        }
    }

    complete_apps = ['festival']