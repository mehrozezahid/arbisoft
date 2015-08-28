# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Person.email'
        db.add_column(u'myapp_person', 'email',
                      self.gf('django.db.models.fields.EmailField')(default='hello@hello.com', max_length=75),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Person.email'
        db.delete_column(u'myapp_person', 'email')


    models = {
        u'myapp.person': {
            'Meta': {'object_name': 'Person'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'first_name': ('django.db.models.fields.TextField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.TextField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['myapp']