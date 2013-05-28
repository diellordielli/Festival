# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Sponsor.ordering'
        db.add_column(u'sponsors_sponsor', 'ordering',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Sponsor.ordering'
        db.delete_column(u'sponsors_sponsor', 'ordering')


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
        },
        u'sponsors.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'sponsors': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'categories'", 'symmetrical': 'False', 'through': u"orm['sponsors.SponsorCategoryYear']", 'to': u"orm['sponsors.Sponsor']"})
        },
        u'sponsors.sponsor': {
            'Meta': {'object_name': 'Sponsor'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'years': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'sponsors'", 'symmetrical': 'False', 'through': u"orm['sponsors.SponsorCategoryYear']", 'to': u"orm['festival.Year']"})
        },
        u'sponsors.sponsorcategoryyear': {
            'Meta': {'object_name': 'SponsorCategoryYear'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sponsors.Category']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sponsor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sponsors.Sponsor']"}),
            'year': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['festival.Year']"})
        }
    }

    complete_apps = ['sponsors']