# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Event'
        db.create_table(u'events_event', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')()),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['events.EventType'], max_length=45)),
            ('status', self.gf('django.db.models.fields.PositiveIntegerField')(max_length=1)),
            ('event_time_type', self.gf('django.db.models.fields.PositiveIntegerField')(max_length=1)),
            ('start_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 11, 21, 0, 0))),
            ('end_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 11, 21, 0, 0))),
            ('recurrence_interval', self.gf('django.db.models.fields.PositiveIntegerField')(max_length=100, null=True, blank=True)),
            ('confirmation', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'events', ['Event'])

        # Adding model 'EventType'
        db.create_table(u'events_eventtype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')()),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'events', ['EventType'])

        # Adding model 'EventToEventCrossRef'
        db.create_table(u'events_eventtoeventcrossref', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')()),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('event_one', self.gf('django.db.models.fields.related.ForeignKey')(related_name='ev_one', to=orm['events.Event'])),
            ('event_two', self.gf('django.db.models.fields.related.ForeignKey')(related_name='ev_two', to=orm['events.Event'])),
            ('relationship_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['events.EventToEventRelationshipType'], null=True, blank=True)),
            ('relationship_description', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'events', ['EventToEventCrossRef'])

        # Adding model 'EventToEventRelationshipType'
        db.create_table(u'events_eventtoeventrelationshiptype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')()),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'events', ['EventToEventRelationshipType'])

        # Adding model 'EventSensorDataCrossRef'
        db.create_table(u'events_eventsensordatacrossref', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')()),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['events.Event'])),
            ('sensor_data', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['things.SensorData'])),
            ('relationship_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['events.EventSensorDataRelationshipType'], null=True, blank=True)),
        ))
        db.send_create_signal(u'events', ['EventSensorDataCrossRef'])

        # Adding model 'EventSensorDataRelationshipType'
        db.create_table(u'events_eventsensordatarelationshiptype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')()),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'events', ['EventSensorDataRelationshipType'])

        # Adding model 'EventLocationCrossRef'
        db.create_table(u'events_eventlocationcrossref', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')()),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['events.Event'])),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['locations.Location'])),
            ('relationship_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['events.EventLocationRelationshipType'], null=True, blank=True)),
        ))
        db.send_create_signal(u'events', ['EventLocationCrossRef'])

        # Adding model 'EventLocationRelationshipType'
        db.create_table(u'events_eventlocationrelationshiptype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')()),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'events', ['EventLocationRelationshipType'])

        # Adding model 'EventPersonCrossRef'
        db.create_table(u'events_eventpersoncrossref', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')()),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['events.Event'])),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['users.Person'])),
            ('user_defined_name', self.gf('django.db.models.fields.CharField')(max_length=45, null=True, blank=True)),
            ('relationship_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['events.EventPersonRelationshipType'], null=True, blank=True)),
        ))
        db.send_create_signal(u'events', ['EventPersonCrossRef'])

        # Adding model 'EventPersonRelationshipType'
        db.create_table(u'events_eventpersonrelationshiptype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')()),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'events', ['EventPersonRelationshipType'])

        # Adding model 'DataDebit'
        db.create_table(u'events_datadebit', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')()),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('sell_rent', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('event_time_type', self.gf('django.db.models.fields.PositiveIntegerField')(max_length=1)),
            ('contract_start_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 11, 21, 0, 0))),
            ('contract_end_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 11, 21, 0, 0))),
            ('rolling', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'events', ['DataDebit'])

        # Adding model 'DataDebitRecipientCrossRef'
        db.create_table(u'events_datadebitrecipientcrossref', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')()),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('DataDebit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['events.DataDebit'])),
            ('Recipient', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['users.Recipient'])),
            ('relationship_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['events.DataDebitRecipientRelationshipType'], null=True, blank=True)),
        ))
        db.send_create_signal(u'events', ['DataDebitRecipientCrossRef'])

        # Adding model 'DataDebitRecipientRelationshipType'
        db.create_table(u'events_datadebitrecipientrelationshiptype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')()),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'events', ['DataDebitRecipientRelationshipType'])

        # Adding model 'DataDebitEventCrossRef'
        db.create_table(u'events_datadebiteventcrossref', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')()),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('DataDebit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['events.DataDebit'])),
            ('Event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['events.Event'])),
            ('relationship_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['events.DataDebitEventRelationshipType'], null=True, blank=True)),
        ))
        db.send_create_signal(u'events', ['DataDebitEventCrossRef'])

        # Adding model 'DataDebitEventRelationshipType'
        db.create_table(u'events_datadebiteventrelationshiptype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')()),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'events', ['DataDebitEventRelationshipType'])


    def backwards(self, orm):
        # Deleting model 'Event'
        db.delete_table(u'events_event')

        # Deleting model 'EventType'
        db.delete_table(u'events_eventtype')

        # Deleting model 'EventToEventCrossRef'
        db.delete_table(u'events_eventtoeventcrossref')

        # Deleting model 'EventToEventRelationshipType'
        db.delete_table(u'events_eventtoeventrelationshiptype')

        # Deleting model 'EventSensorDataCrossRef'
        db.delete_table(u'events_eventsensordatacrossref')

        # Deleting model 'EventSensorDataRelationshipType'
        db.delete_table(u'events_eventsensordatarelationshiptype')

        # Deleting model 'EventLocationCrossRef'
        db.delete_table(u'events_eventlocationcrossref')

        # Deleting model 'EventLocationRelationshipType'
        db.delete_table(u'events_eventlocationrelationshiptype')

        # Deleting model 'EventPersonCrossRef'
        db.delete_table(u'events_eventpersoncrossref')

        # Deleting model 'EventPersonRelationshipType'
        db.delete_table(u'events_eventpersonrelationshiptype')

        # Deleting model 'DataDebit'
        db.delete_table(u'events_datadebit')

        # Deleting model 'DataDebitRecipientCrossRef'
        db.delete_table(u'events_datadebitrecipientcrossref')

        # Deleting model 'DataDebitRecipientRelationshipType'
        db.delete_table(u'events_datadebitrecipientrelationshiptype')

        # Deleting model 'DataDebitEventCrossRef'
        db.delete_table(u'events_datadebiteventcrossref')

        # Deleting model 'DataDebitEventRelationshipType'
        db.delete_table(u'events_datadebiteventrelationshiptype')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'events.datadebit': {
            'Meta': {'object_name': 'DataDebit'},
            'contract_end_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 11, 21, 0, 0)'}),
            'contract_start_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 11, 21, 0, 0)'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'event_time_type': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'rolling': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sell_rent': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'events.datadebiteventcrossref': {
            'DataDebit': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['events.DataDebit']"}),
            'Event': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['events.Event']"}),
            'Meta': {'object_name': 'DataDebitEventCrossRef'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'relationship_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['events.DataDebitEventRelationshipType']", 'null': 'True', 'blank': 'True'})
        },
        u'events.datadebiteventrelationshiptype': {
            'Meta': {'object_name': 'DataDebitEventRelationshipType'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'events.datadebitrecipientcrossref': {
            'DataDebit': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['events.DataDebit']"}),
            'Meta': {'object_name': 'DataDebitRecipientCrossRef'},
            'Recipient': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['users.Recipient']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'relationship_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['events.DataDebitRecipientRelationshipType']", 'null': 'True', 'blank': 'True'})
        },
        u'events.datadebitrecipientrelationshiptype': {
            'Meta': {'object_name': 'DataDebitRecipientRelationshipType'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'events.event': {
            'Meta': {'object_name': 'Event'},
            'confirmation': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 11, 21, 0, 0)'}),
            'event_time_type': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'recurrence_interval': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 11, 21, 0, 0)'}),
            'status': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '1'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['events.EventType']", 'max_length': '45'})
        },
        u'events.eventlocationcrossref': {
            'Meta': {'object_name': 'EventLocationCrossRef'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['events.Event']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['locations.Location']"}),
            'relationship_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['events.EventLocationRelationshipType']", 'null': 'True', 'blank': 'True'})
        },
        u'events.eventlocationrelationshiptype': {
            'Meta': {'object_name': 'EventLocationRelationshipType'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'events.eventpersoncrossref': {
            'Meta': {'object_name': 'EventPersonCrossRef'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['events.Event']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['users.Person']"}),
            'relationship_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['events.EventPersonRelationshipType']", 'null': 'True', 'blank': 'True'}),
            'user_defined_name': ('django.db.models.fields.CharField', [], {'max_length': '45', 'null': 'True', 'blank': 'True'})
        },
        u'events.eventpersonrelationshiptype': {
            'Meta': {'object_name': 'EventPersonRelationshipType'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'events.eventsensordatacrossref': {
            'Meta': {'object_name': 'EventSensorDataCrossRef'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['events.Event']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'relationship_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['events.EventSensorDataRelationshipType']", 'null': 'True', 'blank': 'True'}),
            'sensor_data': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['things.SensorData']"})
        },
        u'events.eventsensordatarelationshiptype': {
            'Meta': {'object_name': 'EventSensorDataRelationshipType'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'events.eventtoeventcrossref': {
            'Meta': {'object_name': 'EventToEventCrossRef'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {}),
            'event_one': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'ev_one'", 'to': u"orm['events.Event']"}),
            'event_two': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'ev_two'", 'to': u"orm['events.Event']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'relationship_description': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'relationship_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['events.EventToEventRelationshipType']", 'null': 'True', 'blank': 'True'})
        },
        u'events.eventtoeventrelationshiptype': {
            'Meta': {'object_name': 'EventToEventRelationshipType'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'events.eventtype': {
            'Meta': {'object_name': 'EventType'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'locations.location': {
            'Meta': {'object_name': 'Location'},
            'address_line_1': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'address_line_2': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'county': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'height_from_sea_level': ('django.db.models.fields.IntegerField', [], {'max_length': '6', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indoor_information': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '25', 'decimal_places': '5', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '25', 'decimal_places': '5', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'orientation': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'postal_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['locations.LocationType']"})
        },
        u'locations.locationtype': {
            'Meta': {'object_name': 'LocationType'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'organisations.organisation': {
            'Meta': {'object_name': 'Organisation'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['organisations.OrganisationType']"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'organisations.organisationtype': {
            'Meta': {'object_name': 'OrganisationType'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'system.currency': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Currency'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '45'}),
            'symbol': ('django.db.models.fields.CharField', [], {'max_length': '16', 'blank': 'True'})
        },
        u'system.ethnicity': {
            'Meta': {'object_name': 'Ethnicity'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'system.gender': {
            'Meta': {'object_name': 'Gender'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'system.maritalstatus': {
            'Meta': {'object_name': 'MaritalStatus'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'system.nationality': {
            'Meta': {'object_name': 'Nationality'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'system.prefix': {
            'Meta': {'object_name': 'Prefix'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'system.religion': {
            'Meta': {'object_name': 'Religion'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'system.unitofmeasurement': {
            'Meta': {'object_name': 'UnitOfMeasurement'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'symbol': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True'})
        },
        u'things.sensor': {
            'Meta': {'object_name': 'Sensor'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'manufacturer': ('django.db.models.fields.CharField', [], {'max_length': '45', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'sensor_id': ('django.db.models.fields.CharField', [], {'default': "'85103e15-3d8e-4898-85df-e2e8f06c49da'", 'max_length': '36'})
        },
        u'things.sensordata': {
            'Meta': {'ordering': "['-date_created']", 'object_name': 'SensorData'},
            'change_of_status': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'sensor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['things.Sensor']"}),
            'source_description': ('django.db.models.fields.TextField', [], {'max_length': '45', 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['things.SensorDataType']"}),
            'unit': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['system.UnitOfMeasurement']"}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '45'})
        },
        u'things.sensordatatype': {
            'Meta': {'object_name': 'SensorDataType'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'users.person': {
            'Meta': {'object_name': 'Person'},
            'address': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['users.PersonAddress']", 'null': 'True', 'blank': 'True'}),
            'annual_income': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'avatar': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'currency': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['system.Currency']", 'null': 'True', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'email_address': ('django.db.models.fields.EmailField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'ethnicity': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['system.Ethnicity']", 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'gender': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['system.Gender']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'marital_status': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['system.MaritalStatus']", 'null': 'True', 'blank': 'True'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'nationality': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['system.Nationality']", 'null': 'True', 'blank': 'True'}),
            'prefix': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['system.Prefix']", 'null': 'True', 'blank': 'True'}),
            'related_organisations': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'person_related_organisations'", 'null': 'True', 'to': u"orm['organisations.Organisation']"}),
            'religion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['system.Religion']", 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'related_user_ac'", 'to': u"orm['auth.User']"}),
            'user_GUID': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'})
        },
        u'users.personaddress': {
            'Meta': {'object_name': 'PersonAddress'},
            'address_line_1': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'address_line_2': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'county': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_current': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'postal_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'})
        },
        u'users.recipient': {
            'Meta': {'object_name': 'Recipient'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'recipient_UUID': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'})
        }
    }

    complete_apps = ['events']