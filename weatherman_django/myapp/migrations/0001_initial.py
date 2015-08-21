# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Filename'
        db.create_table(u'myapp_filename', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('file_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'myapp', ['Filename'])


    def backwards(self, orm):
        # Deleting model 'Filename'
        db.delete_table(u'myapp_filename')


    models = {
        u'myapp.filename': {
            'Meta': {'object_name': 'Filename'},
            'file_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['myapp']