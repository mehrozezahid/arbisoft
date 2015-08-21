# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Filedata'
        db.create_table(u'myapp_filedata', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('file_name', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['myapp.Filename'], to_field='file_name')),
            ('pkt', self.gf('django.db.models.fields.DateField')()),
            ('max_temperaturec', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('mean_temperaturec', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('min_temperaturec', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('dew_pointc', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('meandew_pointc', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('mindew_pointc', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('max_humidity', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('mean_humidity', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('min_humidity', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('max_sea_level_pressurehPa', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('mean_sea_level_pressurehPa', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('min_sea_level_pressurehPa', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('max_visibilityKm', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('mean_visibilityKm', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('min_visibilityKm', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('max_wind_speedKmh', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('mean_wind_speedKmh', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('max_gust_speedkmh', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('precipitationcm', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('cloud_cover', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('events', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('wind_dir_degrees', self.gf('django.db.models.fields.IntegerField')(null=True)),
        ))
        db.send_create_signal(u'myapp', ['Filedata'])


    def backwards(self, orm):
        # Deleting model 'Filedata'
        db.delete_table(u'myapp_filedata')


    models = {
        u'myapp.filedata': {
            'Meta': {'object_name': 'Filedata'},
            'cloud_cover': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'dew_pointc': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'events': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'file_name': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['myapp.Filename']", 'to_field': "'file_name'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_gust_speedkmh': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'max_humidity': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'max_sea_level_pressurehPa': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'max_temperaturec': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'max_visibilityKm': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'max_wind_speedKmh': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'mean_humidity': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'mean_sea_level_pressurehPa': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'mean_temperaturec': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'mean_visibilityKm': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'mean_wind_speedKmh': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'meandew_pointc': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'min_humidity': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'min_sea_level_pressurehPa': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'min_temperaturec': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'min_visibilityKm': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'mindew_pointc': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'pkt': ('django.db.models.fields.DateField', [], {}),
            'precipitationcm': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'wind_dir_degrees': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        },
        u'myapp.filename': {
            'Meta': {'object_name': 'Filename'},
            'file_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['myapp']