# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Person'
        db.create_table(u'myapp_person', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.TextField')(max_length=50)),
            ('last_name', self.gf('django.db.models.fields.TextField')(max_length=50)),
        ))
        db.send_create_signal(u'myapp', ['Person'])


    def backwards(self, orm):
        # Deleting model 'Person'
        db.delete_table(u'myapp_person')


    models = {
        u'myapp.person': {
            'Meta': {'object_name': 'Person'},
            'first_name': ('django.db.models.fields.TextField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.TextField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['myapp']