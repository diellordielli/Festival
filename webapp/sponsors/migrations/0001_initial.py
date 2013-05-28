# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Sponsor'
        db.create_table(u'sponsors_sponsor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('logo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal(u'sponsors', ['Sponsor'])

        # Adding model 'Category'
        db.create_table(u'sponsors_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'sponsors', ['Category'])

        # Adding model 'SponsorCategoryYear'
        db.create_table(u'sponsors_sponsorcategoryyear', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sponsor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sponsors.Sponsor'])),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sponsors.Category'])),
            ('year', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['festival.Year'])),
        ))
        db.send_create_signal(u'sponsors', ['SponsorCategoryYear'])


    def backwards(self, orm):
        # Deleting model 'Sponsor'
        db.delete_table(u'sponsors_sponsor')

        # Deleting model 'Category'
        db.delete_table(u'sponsors_category')

        # Deleting model 'SponsorCategoryYear'
        db.delete_table(u'sponsors_sponsorcategoryyear')


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