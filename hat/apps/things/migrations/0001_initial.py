# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Thing'
        db.create_table(u'things_thing', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')()),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('brand', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['things.ThingType'])),
            ('purchase_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('point_of_purchase_id', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('supplier_id', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('value_creation_practice_type', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='related_value_event', null=True, to=orm['things.ValueCreationEvent'])),
            ('source_thing', self.gf('django.db.models.fields.PositiveIntegerField')(max_length=5, null=True, blank=True)),
            ('device_id', self.gf('django.db.models.fields.CharField')(default='5c96b88b-10f2-4573-a533-960e15b22d19', max_length=36)),
            ('ip_address', self.gf('django.db.models.fields.GenericIPAddressField')(max_length=39)),
            ('is_service', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'things', ['Thing'])

        # Adding model 'ThingType'
        db.create_table(u'things_thingtype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')()),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('parent_node', self.gf('django.db.models.fields.PositiveIntegerField')(max_length=5)),
        ))
        db.send_create_signal(u'things', ['ThingType'])

        # Adding model 'ThingPersonCrossRef'
        db.create_table(u'things_thingpersoncrossref', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')()),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['users.Person'])),
            ('thing', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['things.Thing'])),
            ('relationship_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['things.ThingPersonRelationshipType'])),
            ('is_relationship_current', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'things', ['ThingPersonCrossRef'])

        # Adding model 'ThingPersonRelationshipType'
        db.create_table(u'things_thingpersonrelationshiptype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')()),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'things', ['ThingPersonRelationshipType'])

        # Adding model 'ThingPropertyCrossRef'
        db.create_table(u'things_thingpropertycrossref', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')()),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('thing', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['things.Thing'])),
            ('thing_property', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['things.ThingProperty'])),
            ('relationship_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['things.ThingPropertyRelationshipType'])),
            ('is_current', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'things', ['ThingPropertyCrossRef'])

        # Adding model 'ThingPropertyRelationshipType'
        db.create_table(u'things_thingpropertyrelationshiptype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')()),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'things', ['ThingPropertyRelationshipType'])

        # Adding model 'ThingProperty'
        db.create_table(u'things_thingproperty', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')()),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('unit', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('value', self.gf('django.db.models.fields.PositiveIntegerField')(max_length=5, null=True, blank=True)),
        ))
        db.send_create_signal(u'things', ['ThingProperty'])

        # Adding model 'InventoryThingSecondary'
        db.create_table(u'things_inventorythingsecondary', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')()),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('thing', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['things.Thing'])),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['things.ThingPersonCrossRef'])),
            ('ud_inventory_name', self.gf('django.db.models.fields.CharField')(max_length=45)),
            ('thing_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('stock_level', self.gf('django.db.models.fields.PositiveIntegerField')(max_length=5)),
            ('unit_name', self.gf('django.db.models.fields.CharField')(max_length=45)),
            ('threshold', self.gf('django.db.models.fields.PositiveIntegerField')(max_length=5)),
        ))
        db.send_create_signal(u'things', ['InventoryThingSecondary'])

        # Adding model 'ThingSensorCrossRef'
        db.create_table(u'things_thingsensorcrossref', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')()),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('thing', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['things.Thing'])),
            ('sensor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['things.Sensor'])),
            ('relationship_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['things.ThingSensorRelationshipType'])),
        ))
        db.send_create_signal(u'things', ['ThingSensorCrossRef'])

        # Adding model 'ThingSensorRelationshipType'
        db.create_table(u'things_thingsensorrelationshiptype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')()),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'things', ['ThingSensorRelationshipType'])

        # Adding model 'Sensor'
        db.create_table(u'things_sensor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')()),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('manufacturer', self.gf('django.db.models.fields.CharField')(max_length=45, null=True, blank=True)),
            ('sensor_id', self.gf('django.db.models.fields.CharField')(default='0db4df5b-ae51-4185-81a5-099f33403a47', max_length=36)),
        ))
        db.send_create_signal(u'things', ['Sensor'])

        # Adding model 'SensorData'
        db.create_table(u'things_sensordata', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')()),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('sensor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['things.Sensor'])),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['things.SensorDataType'])),
            ('unit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['system.UnitOfMeasurement'])),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=45)),
            ('source_description', self.gf('django.db.models.fields.TextField')(max_length=45, null=True, blank=True)),
            ('change_of_status', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'things', ['SensorData'])

        # Adding model 'SensorDataType'
        db.create_table(u'things_sensordatatype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')()),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'things', ['SensorDataType'])

        # Adding model 'ValueCreationEvent'
        db.create_table(u'things_valuecreationevent', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')()),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['things.ValueCreationType'])),
            ('start_time', self.gf('django.db.models.fields.TimeField')()),
            ('end_time', self.gf('django.db.models.fields.TimeField')()),
            ('start_value', self.gf('django.db.models.fields.CharField')(max_length=45)),
            ('end_value', self.gf('django.db.models.fields.CharField')(max_length=45)),
            ('consumption_rules_id', self.gf('django.db.models.fields.PositiveIntegerField')(max_length=5, blank=True)),
        ))
        db.send_create_signal(u'things', ['ValueCreationEvent'])

        # Adding model 'ValueCreationType'
        db.create_table(u'things_valuecreationtype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')()),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'things', ['ValueCreationType'])


    def backwards(self, orm):
        # Deleting model 'Thing'
        db.delete_table(u'things_thing')

        # Deleting model 'ThingType'
        db.delete_table(u'things_thingtype')

        # Deleting model 'ThingPersonCrossRef'
        db.delete_table(u'things_thingpersoncrossref')

        # Deleting model 'ThingPersonRelationshipType'
        db.delete_table(u'things_thingpersonrelationshiptype')

        # Deleting model 'ThingPropertyCrossRef'
        db.delete_table(u'things_thingpropertycrossref')

        # Deleting model 'ThingPropertyRelationshipType'
        db.delete_table(u'things_thingpropertyrelationshiptype')

        # Deleting model 'ThingProperty'
        db.delete_table(u'things_thingproperty')

        # Deleting model 'InventoryThingSecondary'
        db.delete_table(u'things_inventorythingsecondary')

        # Deleting model 'ThingSensorCrossRef'
        db.delete_table(u'things_thingsensorcrossref')

        # Deleting model 'ThingSensorRelationshipType'
        db.delete_table(u'things_thingsensorrelationshiptype')

        # Deleting model 'Sensor'
        db.delete_table(u'things_sensor')

        # Deleting model 'SensorData'
        db.delete_table(u'things_sensordata')

        # Deleting model 'SensorDataType'
        db.delete_table(u'things_sensordatatype')

        # Deleting model 'ValueCreationEvent'
        db.delete_table(u'things_valuecreationevent')

        # Deleting model 'ValueCreationType'
        db.delete_table(u'things_valuecreationtype')


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
        u'things.inventorythingsecondary': {
            'Meta': {'object_name': 'InventoryThingSecondary'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['things.ThingPersonCrossRef']"}),
            'stock_level': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '5'}),
            'thing': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['things.Thing']"}),
            'thing_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'threshold': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '5'}),
            'ud_inventory_name': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'unit_name': ('django.db.models.fields.CharField', [], {'max_length': '45'})
        },
        u'things.sensor': {
            'Meta': {'object_name': 'Sensor'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'manufacturer': ('django.db.models.fields.CharField', [], {'max_length': '45', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'sensor_id': ('django.db.models.fields.CharField', [], {'default': "'8e3018fd-29f7-4100-bc1d-7d0ba627346d'", 'max_length': '36'})
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
        u'things.thing': {
            'Meta': {'object_name': 'Thing'},
            'brand': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'device_id': ('django.db.models.fields.CharField', [], {'default': "'01c396f6-6624-4a26-b244-72a8fa6831d4'", 'max_length': '36'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.GenericIPAddressField', [], {'max_length': '39'}),
            'is_service': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'point_of_purchase_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'purchase_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'source_thing': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'supplier_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['things.ThingType']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'value_creation_practice_type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'related_value_event'", 'null': 'True', 'to': u"orm['things.ValueCreationEvent']"})
        },
        u'things.thingpersoncrossref': {
            'Meta': {'object_name': 'ThingPersonCrossRef'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_relationship_current': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['users.Person']"}),
            'relationship_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['things.ThingPersonRelationshipType']"}),
            'thing': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['things.Thing']"})
        },
        u'things.thingpersonrelationshiptype': {
            'Meta': {'object_name': 'ThingPersonRelationshipType'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'things.thingproperty': {
            'Meta': {'object_name': 'ThingProperty'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'unit': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'value': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'})
        },
        u'things.thingpropertycrossref': {
            'Meta': {'object_name': 'ThingPropertyCrossRef'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_current': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'relationship_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['things.ThingPropertyRelationshipType']"}),
            'thing': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['things.Thing']"}),
            'thing_property': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['things.ThingProperty']"})
        },
        u'things.thingpropertyrelationshiptype': {
            'Meta': {'object_name': 'ThingPropertyRelationshipType'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'things.thingsensorcrossref': {
            'Meta': {'object_name': 'ThingSensorCrossRef'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'relationship_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['things.ThingSensorRelationshipType']"}),
            'sensor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['things.Sensor']"}),
            'thing': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['things.Thing']"})
        },
        u'things.thingsensorrelationshiptype': {
            'Meta': {'object_name': 'ThingSensorRelationshipType'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'things.thingtype': {
            'Meta': {'object_name': 'ThingType'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'parent_node': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '5'})
        },
        u'things.valuecreationevent': {
            'Meta': {'object_name': 'ValueCreationEvent'},
            'consumption_rules_id': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '5', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {}),
            'end_time': ('django.db.models.fields.TimeField', [], {}),
            'end_value': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'start_time': ('django.db.models.fields.TimeField', [], {}),
            'start_value': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['things.ValueCreationType']"})
        },
        u'things.valuecreationtype': {
            'Meta': {'object_name': 'ValueCreationType'},
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
        }
    }

    complete_apps = ['things']