from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4

from ...models import CreateUpdateMixin, NameDescMixin


class Thing(CreateUpdateMixin, NameDescMixin):

    # FK to User class
    user = models.ForeignKey(
        User
    )

    brand = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )

    type = models.ForeignKey(
        'ThingType'
    )

    purchase_date = models.DateField(
        blank=True,
        null=True,
    )

    point_of_purchase_id = models.PositiveIntegerField(
        blank=True,
        null=True,
    )

    supplier_id = models.PositiveIntegerField(
        blank=True,
        null=True,
    )

    value_creation_practice_type = models.ForeignKey(
        'ValueCreationEvent',
        related_name="related_value_event",
        blank=True,
        null=True,
    )

    source_thing = models.PositiveIntegerField(
        max_length=5,
        blank=True,
        null=True,
    )

    device_id = models.CharField(
        max_length=36,
        default=lambda: str(uuid4())
    )

    ip_address = models.GenericIPAddressField()

    is_service = models.BooleanField(
        default=False
    )

    # image = models.FileField(
    #     blank=True,
    #     null=True,
    # )

    def last_used(self):

        # Get all device sensors
        sensor_refs = ThingSensorCrossRef.objects.filter(thing=self)
        sensors = [sensor_ref.sensor for sensor_ref in sensor_refs]
        latest_data = SensorData.objects.filter(sensor__in=sensors).order_by('-date_created')[:1]

        if latest_data:
            return latest_data[0].date_created

        return None


class ThingType(CreateUpdateMixin, NameDescMixin):

    parent_node = models.PositiveIntegerField(
        max_length=5,
    )

    class Meta:
        verbose_name_plural = u"Thing Types"


class ThingPersonCrossRef(CreateUpdateMixin, NameDescMixin):

    #FK to owner
    owner = models.ForeignKey(
        'users.Person'
    )

    #FK to thing
    thing = models.ForeignKey(
        'Thing'
    )

    relationship_type = models.ForeignKey(
        'ThingPersonRelationshipType'
    )

    is_relationship_current = models.BooleanField(
        default=False,
    )


class ThingPersonRelationshipType(CreateUpdateMixin, NameDescMixin):
    pass


class ThingPropertyCrossRef(CreateUpdateMixin):

    #FK to thing
    thing = models.ForeignKey(
        Thing
    )

    thing_property = models.ForeignKey(
        'ThingProperty'
    )

    relationship_type = models.ForeignKey(
        'ThingPropertyRelationshipType'
    )

    is_current = models.BooleanField(
        default=False,
    )


class ThingPropertyRelationshipType(CreateUpdateMixin, NameDescMixin):
    pass


class ThingProperty(CreateUpdateMixin, NameDescMixin):

    unit = models.CharField(
        max_length=100,
    )

    value = models.PositiveIntegerField(
        max_length=5,
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name_plural = u'Thing Properties'


class InventoryThingSecondary(CreateUpdateMixin):

    thing = models.ForeignKey(
        Thing,
    )

    person = models.ForeignKey(
        'ThingPersonCrossRef'
    )

    ud_inventory_name = models.CharField(
        max_length=45,
    )

    thing_name = models.CharField(
        max_length=100,
    )

    stock_level = models.PositiveIntegerField(
        max_length=5
    )

    unit_name = models.CharField(
        max_length=45,
    )

    threshold = models.PositiveIntegerField(
        max_length=5,
    )


class ThingSensorCrossRef(CreateUpdateMixin, NameDescMixin):

        #FK to thing
    thing = models.ForeignKey(
        Thing
    )

    sensor = models.ForeignKey(
        'Sensor'
    )

    relationship_type = models.ForeignKey(
        'ThingSensorRelationshipType'
    )


class ThingSensorRelationshipType(CreateUpdateMixin, NameDescMixin):
    pass


class Sensor(CreateUpdateMixin, NameDescMixin):

    manufacturer = models.CharField(
        max_length=45,
        blank=True,
        null=True,
    )

    sensor_id = models.CharField(
        max_length=36,
        default=lambda: str(uuid4())
    )

    class Meta:
        verbose_name_plural = u'Sensors'


class SensorData(CreateUpdateMixin):

    sensor = models.ForeignKey(
        Sensor
    )

    type = models.ForeignKey(
        'SensorDataType'
    )

    unit = models.ForeignKey(
        'system.UnitOfMeasurement'
    )

    value = models.CharField(
        max_length=45,
    )

    source_description = models.TextField(
        max_length=45,
        blank=True,
        null=True,
    )

    change_of_status = models.BooleanField(
        default=False,
    )

    def thing(self):
        return ThingSensorCrossRef.objects.filter(sensor=self.sensor)[0].thing

    def __unicode__(self):
        return self.source_description

    class Meta:
        verbose_name_plural = u'Sensor Data'
        ordering = ['-date_created']


class SensorDataType(CreateUpdateMixin, NameDescMixin):

    class Meta:
        verbose_name_plural = u'Sensor Data Types'


class ValueCreationEvent(CreateUpdateMixin):

    type = models.ForeignKey(
        'ValueCreationType'
    )

    start_time = models.TimeField()

    end_time = models.TimeField()

    start_value = models.CharField(
        max_length=45,
    )

    end_value = models.CharField(
        max_length=45,
    )

    consumption_rules_id = models.PositiveIntegerField(
        max_length=5,
        blank=True,
    )


class ValueCreationType(CreateUpdateMixin, NameDescMixin):
    pass
