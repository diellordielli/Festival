# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Category'
        db.delete_table(u'gallery_category')

        # Removing M2M table for field categories on 'Image'
        db.delete_table('gallery_image_categories')


    def backwards(self, orm):
        # Adding model 'Category'
        db.create_table(u'gallery_category', (
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'gallery', ['Category'])

        # Adding M2M table for field categories on 'Image'
        db.create_table(u'gallery_image_categories', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('image', models.ForeignKey(orm[u'gallery.image'], null=False)),
            ('category', models.ForeignKey(orm[u'gallery.category'], null=False))
        ))
        db.create_unique(u'gallery_image_categories', ['image_id', 'category_id'])


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
        u'gallery.image': {
            'Meta': {'object_name': 'Image'},
            'band': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'images'", 'null': 'True', 'to': u"orm['festival.Band']"}),
            'choice': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'is_yearcover': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'year': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['festival.Year']"})
        }
    }

    complete_apps = ['gallery']