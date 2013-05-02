# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Band'
        db.create_table(u'festival_band', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('genre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(default='-', max_length=50)),
        ))
        db.send_create_signal(u'festival', ['Band'])

        # Adding model 'BandLinks'
        db.create_table(u'festival_bandlinks', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('type', self.gf('django.db.models.fields.CharField')(default='WS', max_length=20)),
            ('band', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['festival.Band'])),
        ))
        db.send_create_signal(u'festival', ['BandLinks'])

        # Adding model 'Year'
        db.create_table(u'festival_year', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('start', self.gf('django.db.models.fields.DateField')()),
            ('end', self.gf('django.db.models.fields.DateField')()),
            ('logo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'festival', ['Year'])

        # Adding model 'BandYear'
        db.create_table(u'festival_bandyear', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('stage', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('time', self.gf('django.db.models.fields.DateTimeField')()),
            ('band', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['festival.Band'])),
            ('year', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['festival.Year'])),
        ))
        db.send_create_signal(u'festival', ['BandYear'])


    def backwards(self, orm):
        # Deleting model 'Band'
        db.delete_table(u'festival_band')

        # Deleting model 'BandLinks'
        db.delete_table(u'festival_bandlinks')

        # Deleting model 'Year'
        db.delete_table(u'festival_year')

        # Deleting model 'BandYear'
        db.delete_table(u'festival_bandyear')


    models = {
        u'festival.band': {
            'Meta': {'object_name': 'Band'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'genre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'slug': ('django.db.models.fields.SlugField', [], {'default': "'-'", 'max_length': '50'})
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