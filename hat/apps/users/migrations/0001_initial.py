# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UserAccount'
        db.create_table(u'users_useraccount', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')()),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('username', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal(u'users', ['UserAccount'])

        # Adding model 'AffiliateService'
        db.create_table(u'users_affiliateservice', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')()),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('service_type', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('user_web_id', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('displayable', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'users', ['AffiliateService'])

        # Adding model 'Person'
        db.create_table(u'users_person', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')()),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='related_user_ac', to=orm['auth.User'])),
            ('avatar', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('middle_name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('user_GUID', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
            ('date_of_birth', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('email_address', self.gf('django.db.models.fields.EmailField')(max_length=254, null=True, blank=True)),
            ('gender', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['system.Gender'], null=True, blank=True)),
            ('prefix', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['system.Prefix'], null=True, blank=True)),
            ('nationality', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['system.Nationality'], null=True, blank=True)),
            ('ethnicity', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['system.Ethnicity'], null=True, blank=True)),
            ('religion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['system.Religion'], null=True, blank=True)),
            ('marital_status', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['system.MaritalStatus'], null=True, blank=True)),
            ('related_organisations', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='person_related_organisations', null=True, to=orm['organisations.Organisation'])),
            ('currency', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['system.Currency'], null=True, blank=True)),
            ('annual_income', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
        ))
        db.send_create_signal(u'users', ['Person'])

        # Adding M2M table for field address on 'Person'
        m2m_table_name = db.shorten_name(u'users_person_address')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('person', models.ForeignKey(orm[u'users.person'], null=False)),
            ('personaddress', models.ForeignKey(orm[u'users.personaddress'], null=False))
        ))
        db.create_unique(m2m_table_name, ['person_id', 'personaddress_id'])

        # Adding model 'PersonAddress'
        db.create_table(u'users_personaddress', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')()),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('number', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('address_line_1', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('address_line_2', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True)),
            ('county', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('postal_code', self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True)),
            ('is_current', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'users', ['PersonAddress'])

        # Adding model 'PersonContactMethod'
        db.create_table(u'users_personcontactmethod', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')()),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['users.Person'])),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['system.ContactMethodType'])),
            ('detail', self.gf('django.db.models.fields.CharField')(max_length=254)),
            ('priority', self.gf('django.db.models.fields.PositiveIntegerField')(default=0, max_length=5)),
        ))
        db.send_create_signal(u'users', ['PersonContactMethod'])

        # Adding model 'PersonOrganisation'
        db.create_table(u'users_personorganisation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')()),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['users.Person'])),
            ('organisation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['organisations.Organisation'])),
            ('person_role', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('end_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'users', ['PersonOrganisation'])

        # Adding model 'PersonToPersonCrossRef'
        db.create_table(u'users_persontopersoncrossref', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')()),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('person_one', self.gf('django.db.models.fields.related.ForeignKey')(related_name='person1', to=orm['users.Person'])),
            ('person_two', self.gf('django.db.models.fields.related.ForeignKey')(related_name='person2', to=orm['users.Person'])),
            ('relationship_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['users.PersonToPersonRelationshipType'])),
            ('relationship_description', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'users', ['PersonToPersonCrossRef'])

        # Adding model 'PersonToPersonRelationshipType'
        db.create_table(u'users_persontopersonrelationshiptype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')()),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'users', ['PersonToPersonRelationshipType'])

        # Adding model 'Emotion'
        db.create_table(u'users_emotion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')()),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['users.Person'])),
            ('time', self.gf('django.db.models.fields.TimeField')()),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['users.EmotionType'])),
        ))
        db.send_create_signal(u'users', ['Emotion'])

        # Adding model 'EmotionType'
        db.create_table(u'users_emotiontype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')()),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'users', ['EmotionType'])

        # Adding model 'PersonDynamic'
        db.create_table(u'users_persondynamic', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')()),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['users.Person'])),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['users.DynamicType'])),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=45)),
            ('priority', self.gf('django.db.models.fields.PositiveIntegerField')(max_length=5, null=True, blank=True)),
            ('is_current', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'users', ['PersonDynamic'])

        # Adding model 'DynamicType'
        db.create_table(u'users_dynamictype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')()),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('sensor_data', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['things.SensorData'])),
            ('source_description', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'users', ['DynamicType'])

        # Adding model 'Recipient'
        db.create_table(u'users_recipient', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')()),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('recipient_UUID', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
        ))
        db.send_create_signal(u'users', ['Recipient'])

        # Adding model 'PersonDataDebitCrossRef'
        db.create_table(u'users_persondatadebitcrossref', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')()),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['users.Person'])),
            ('DataDebit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['events.DataDebit'])),
            ('relationship_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['users.PersonDataDebitRelationshipType'], null=True, blank=True)),
        ))
        db.send_create_signal(u'users', ['PersonDataDebitCrossRef'])

        # Adding model 'PersonDataDebitRelationshipType'
        db.create_table(u'users_persondatadebitrelationshiptype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')()),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'users', ['PersonDataDebitRelationshipType'])

        # Adding model 'PersonAddressLocationCrossRef'
        db.create_table(u'users_personaddresslocationcrossref', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')()),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('person_address_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['users.PersonAddress'])),
            ('location_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['locations.Location'])),
            ('relationship_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['users.PersonAddressRelationshipType'], null=True, blank=True)),
        ))
        db.send_create_signal(u'users', ['PersonAddressLocationCrossRef'])

        # Adding model 'PersonAddressRelationshipType'
        db.create_table(u'users_personaddressrelationshiptype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')()),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'users', ['PersonAddressRelationshipType'])


    def backwards(self, orm):
        # Deleting model 'UserAccount'
        db.delete_table(u'users_useraccount')

        # Deleting model 'AffiliateService'
        db.delete_table(u'users_affiliateservice')

        # Deleting model 'Person'
        db.delete_table(u'users_person')

        # Removing M2M table for field address on 'Person'
        db.delete_table(db.shorten_name(u'users_person_address'))

        # Deleting model 'PersonAddress'
        db.delete_table(u'users_personaddress')

        # Deleting model 'PersonContactMethod'
        db.delete_table(u'users_personcontactmethod')

        # Deleting model 'PersonOrganisation'
        db.delete_table(u'users_personorganisation')

        # Deleting model 'PersonToPersonCrossRef'
        db.delete_table(u'users_persontopersoncrossref')

        # Deleting model 'PersonToPersonRelationshipType'
        db.delete_table(u'users_persontopersonrelationshiptype')

        # Deleting model 'Emotion'
        db.delete_table(u'users_emotion')

        # Deleting model 'EmotionType'
        db.delete_table(u'users_emotiontype')

        # Deleting model 'PersonDynamic'
        db.delete_table(u'users_persondynamic')

        # Deleting model 'DynamicType'
        db.delete_table(u'users_dynamictype')

        # Deleting model 'Recipient'
        db.delete_table(u'users_recipient')

        # Deleting model 'PersonDataDebitCrossRef'
        db.delete_table(u'users_persondatadebitcrossref')

        # Deleting model 'PersonDataDebitRelationshipType'
        db.delete_table(u'users_persondatadebitrelationshiptype')

        # Deleting model 'PersonAddressLocationCrossRef'
        db.delete_table(u'users_personaddresslocationcrossref')

        # Deleting model 'PersonAddressRelationshipType'
        db.delete_table(u'users_personaddressrelationshiptype')


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
            'contract_end_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2015, 2, 19, 0, 0)'}),
            'contract_start_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2015, 2, 19, 0, 0)'}),
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
        u'system.contactmethodtype': {
            'Meta': {'object_name': 'ContactMethodType'},
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
            'sensor_id': ('django.db.models.fields.CharField', [], {'default': "'489cf299-70ff-4ae8-b196-612effe9d9c5'", 'max_length': '36'})
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
        u'users.affiliateservice': {
            'Meta': {'object_name': 'AffiliateService'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {}),
            'displayable': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'service_type': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'user_web_id': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'users.dynamictype': {
            'Meta': {'object_name': 'DynamicType'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'sensor_data': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['things.SensorData']"}),
            'source_description': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'users.emotion': {
            'Meta': {'object_name': 'Emotion'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['users.Person']"}),
            'time': ('django.db.models.fields.TimeField', [], {}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['users.EmotionType']"})
        },
        u'users.emotiontype': {
            'Meta': {'object_name': 'EmotionType'},
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
        u'users.personaddresslocationcrossref': {
            'Meta': {'object_name': 'PersonAddressLocationCrossRef'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'location_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['locations.Location']"}),
            'person_address_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['users.PersonAddress']"}),
            'relationship_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['users.PersonAddressRelationshipType']", 'null': 'True', 'blank': 'True'})
        },
        u'users.personaddressrelationshiptype': {
            'Meta': {'object_name': 'PersonAddressRelationshipType'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'users.personcontactmethod': {
            'Meta': {'object_name': 'PersonContactMethod'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {}),
            'detail': ('django.db.models.fields.CharField', [], {'max_length': '254'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['users.Person']"}),
            'priority': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'max_length': '5'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['system.ContactMethodType']"})
        },
        u'users.persondatadebitcrossref': {
            'DataDebit': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['events.DataDebit']"}),
            'Meta': {'object_name': 'PersonDataDebitCrossRef'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['users.Person']"}),
            'relationship_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['users.PersonDataDebitRelationshipType']", 'null': 'True', 'blank': 'True'})
        },
        u'users.persondatadebitrelationshiptype': {
            'Meta': {'object_name': 'PersonDataDebitRelationshipType'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'users.persondynamic': {
            'Meta': {'object_name': 'PersonDynamic'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_current': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['users.Person']"}),
            'priority': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['users.DynamicType']"}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '45'})
        },
        u'users.personorganisation': {
            'Meta': {'object_name': 'PersonOrganisation'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'organisation': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['organisations.Organisation']"}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['users.Person']"}),
            'person_role': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'start_date': ('django.db.models.fields.DateField', [], {})
        },
        u'users.persontopersoncrossref': {
            'Meta': {'object_name': 'PersonToPersonCrossRef'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'person_one': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'person1'", 'to': u"orm['users.Person']"}),
            'person_two': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'person2'", 'to': u"orm['users.Person']"}),
            'relationship_description': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'relationship_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['users.PersonToPersonRelationshipType']"})
        },
        u'users.persontopersonrelationshiptype': {
            'Meta': {'object_name': 'PersonToPersonRelationshipType'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'users.recipient': {
            'Meta': {'object_name': 'Recipient'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'recipient_UUID': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'})
        },
        u'users.useraccount': {
            'Meta': {'object_name': 'UserAccount'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        }
    }

    complete_apps = ['users']