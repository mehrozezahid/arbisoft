# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Filedata.precipitationcm'
        db.alter_column(u'myapp_filedata', 'precipitationcm', self.gf('django.db.models.fields.FloatField')(null=True))

    def backwards(self, orm):

        # Changing field 'Filedata.precipitationcm'
        db.alter_column(u'myapp_filedata', 'precipitationcm', self.gf('django.db.models.fields.IntegerField')(null=True))

    models = {
        u'myapp.filedata': {
            'Meta': {'object_name': 'Filedata'},
            'cloud_cover': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dew_pointc': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'events': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'file_name': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['myapp.Filename']", 'to_field': "'file_name'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_gust_speedkmh': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'max_humidity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'max_sea_level_pressurehPa': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'max_temperaturec': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'max_visibilityKm': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'max_wind_speedKmh': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'mean_humidity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'mean_sea_level_pressurehPa': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'mean_temperaturec': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'mean_visibilityKm': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'mean_wind_speedKmh': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'meandew_pointc': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'min_humidity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'min_sea_level_pressurehPa': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'min_temperaturec': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'min_visibilityKm': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'mindew_pointc': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pkt': ('django.db.models.fields.DateField', [], {}),
            'precipitationcm': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'wind_dir_degrees': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'myapp.filename': {
            'Meta': {'object_name': 'Filename'},
            'file_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['myapp']