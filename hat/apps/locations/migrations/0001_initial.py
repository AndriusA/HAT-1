# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Location'
        db.create_table(u'locations_location', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')()),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('number', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('address_line_1', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('address_line_2', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True)),
            ('county', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('postal_code', self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['locations.LocationType'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('longitude', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=25, decimal_places=5, blank=True)),
            ('latitude', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=25, decimal_places=5, blank=True)),
            ('height_from_sea_level', self.gf('django.db.models.fields.IntegerField')(max_length=6, null=True, blank=True)),
            ('indoor_information', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('orientation', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
        ))
        db.send_create_signal(u'locations', ['Location'])

        # Adding model 'LocationType'
        db.create_table(u'locations_locationtype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')()),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'locations', ['LocationType'])

        # Adding model 'LocationPersonCrossRef'
        db.create_table(u'locations_locationpersoncrossref', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')()),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['locations.Location'])),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['users.Person'])),
            ('common_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('relationship_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['locations.LocationPersonRelationshipType'])),
        ))
        db.send_create_signal(u'locations', ['LocationPersonCrossRef'])

        # Adding model 'LocationPersonRelationshipType'
        db.create_table(u'locations_locationpersonrelationshiptype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')()),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'locations', ['LocationPersonRelationshipType'])

        # Adding model 'LocationThingCrossRef'
        db.create_table(u'locations_locationthingcrossref', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')()),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['locations.Location'])),
            ('thing', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['things.Thing'])),
            ('common_name', self.gf('django.db.models.fields.CharField')(max_length=45, null=True, blank=True)),
            ('relationship_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['locations.LocationThingRelationshipType'], null=True, blank=True)),
        ))
        db.send_create_signal(u'locations', ['LocationThingCrossRef'])

        # Adding model 'LocationThingRelationshipType'
        db.create_table(u'locations_locationthingrelationshiptype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')()),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'locations', ['LocationThingRelationshipType'])

        # Adding model 'LocationToLocationCrossRef'
        db.create_table(u'locations_locationtolocationcrossref', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')()),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('loc_one', self.gf('django.db.models.fields.related.ForeignKey')(related_name='loc_one', to=orm['locations.Location'])),
            ('loc_two', self.gf('django.db.models.fields.related.ForeignKey')(related_name='loc_two', to=orm['locations.Location'])),
            ('relationship_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['locations.LocationToLocationRelationshipType'])),
            ('relationship_description', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'locations', ['LocationToLocationCrossRef'])

        # Adding model 'LocationToLocationRelationshipType'
        db.create_table(u'locations_locationtolocationrelationshiptype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')()),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'locations', ['LocationToLocationRelationshipType'])

        # Adding model 'LocationSensorCrossRef'
        db.create_table(u'locations_locationsensorcrossref', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')()),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['locations.Location'])),
            ('sensor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['things.Sensor'])),
            ('common_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('relationship_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['locations.LocationSensorRelationshipType'])),
        ))
        db.send_create_signal(u'locations', ['LocationSensorCrossRef'])

        # Adding model 'LocationSensorRelationshipType'
        db.create_table(u'locations_locationsensorrelationshiptype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')()),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'locations', ['LocationSensorRelationshipType'])

        # Adding model 'InventoryLocationSecondary'
        db.create_table(u'locations_inventorylocationsecondary', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')()),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['locations.Location'])),
            ('thing', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['things.Thing'])),
            ('ud_inventory_name', self.gf('django.db.models.fields.CharField')(max_length=45)),
            ('thing_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('stock_level', self.gf('django.db.models.fields.PositiveIntegerField')(max_length=5)),
            ('unit_name', self.gf('django.db.models.fields.CharField')(max_length=45)),
            ('threshold', self.gf('django.db.models.fields.PositiveIntegerField')(max_length=5)),
        ))
        db.send_create_signal(u'locations', ['InventoryLocationSecondary'])


    def backwards(self, orm):
        # Deleting model 'Location'
        db.delete_table(u'locations_location')

        # Deleting model 'LocationType'
        db.delete_table(u'locations_locationtype')

        # Deleting model 'LocationPersonCrossRef'
        db.delete_table(u'locations_locationpersoncrossref')

        # Deleting model 'LocationPersonRelationshipType'
        db.delete_table(u'locations_locationpersonrelationshiptype')

        # Deleting model 'LocationThingCrossRef'
        db.delete_table(u'locations_locationthingcrossref')

        # Deleting model 'LocationThingRelationshipType'
        db.delete_table(u'locations_locationthingrelationshiptype')

        # Deleting model 'LocationToLocationCrossRef'
        db.delete_table(u'locations_locationtolocationcrossref')

        # Deleting model 'LocationToLocationRelationshipType'
        db.delete_table(u'locations_locationtolocationrelationshiptype')

        # Deleting model 'LocationSensorCrossRef'
        db.delete_table(u'locations_locationsensorcrossref')

        # Deleting model 'LocationSensorRelationshipType'
        db.delete_table(u'locations_locationsensorrelationshiptype')

        # Deleting model 'InventoryLocationSecondary'
        db.delete_table(u'locations_inventorylocationsecondary')


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
        u'locations.inventorylocationsecondary': {
            'Meta': {'object_name': 'InventoryLocationSecondary'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['locations.Location']"}),
            'stock_level': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '5'}),
            'thing': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['things.Thing']"}),
            'thing_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'threshold': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '5'}),
            'ud_inventory_name': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'unit_name': ('django.db.models.fields.CharField', [], {'max_length': '45'})
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
        u'locations.locationpersoncrossref': {
            'Meta': {'object_name': 'LocationPersonCrossRef'},
            'common_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['locations.Location']"}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['users.Person']"}),
            'relationship_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['locations.LocationPersonRelationshipType']"})
        },
        u'locations.locationpersonrelationshiptype': {
            'Meta': {'object_name': 'LocationPersonRelationshipType'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'locations.locationsensorcrossref': {
            'Meta': {'object_name': 'LocationSensorCrossRef'},
            'common_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['locations.Location']"}),
            'relationship_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['locations.LocationSensorRelationshipType']"}),
            'sensor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['things.Sensor']"})
        },
        u'locations.locationsensorrelationshiptype': {
            'Meta': {'object_name': 'LocationSensorRelationshipType'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'locations.locationthingcrossref': {
            'Meta': {'object_name': 'LocationThingCrossRef'},
            'common_name': ('django.db.models.fields.CharField', [], {'max_length': '45', 'null': 'True', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['locations.Location']"}),
            'relationship_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['locations.LocationThingRelationshipType']", 'null': 'True', 'blank': 'True'}),
            'thing': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['things.Thing']"})
        },
        u'locations.locationthingrelationshiptype': {
            'Meta': {'object_name': 'LocationThingRelationshipType'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'locations.locationtolocationcrossref': {
            'Meta': {'object_name': 'LocationToLocationCrossRef'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'loc_one': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'loc_one'", 'to': u"orm['locations.Location']"}),
            'loc_two': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'loc_two'", 'to': u"orm['locations.Location']"}),
            'relationship_description': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'relationship_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['locations.LocationToLocationRelationshipType']"})
        },
        u'locations.locationtolocationrelationshiptype': {
            'Meta': {'object_name': 'LocationToLocationRelationshipType'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
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
        u'things.sensor': {
            'Meta': {'object_name': 'Sensor'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'manufacturer': ('django.db.models.fields.CharField', [], {'max_length': '45', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'sensor_id': ('django.db.models.fields.CharField', [], {'default': "'1fef7c7a-4f35-40e6-9bbf-dc73c2c298d1'", 'max_length': '36'})
        },
        u'things.thing': {
            'Meta': {'object_name': 'Thing'},
            'brand': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'device_id': ('django.db.models.fields.CharField', [], {'default': "'ae2de450-8982-4751-9941-de8b062f92fe'", 'max_length': '36'}),
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

    complete_apps = ['locations']