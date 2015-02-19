from django.db import models

from ...models import AddressMixin, CreateUpdateMixin, NameDescMixin


# class Places(CreateUpdateMixin, NameDescMixin):

#     locations = models.ManyToManyField(
#         'Location'
#     )


# Main Location class, linked to:
# - Thing VIA LocationThingCrossRef class
# - User VIA LocationUserCrossRef class
# - Event VIA EventLocationCrossRef class in Events models.py
class Location(CreateUpdateMixin, AddressMixin):

    type = models.ForeignKey(
        'LocationType'
    )

    name = models.CharField(
        max_length=512,
    )

    description = models.TextField(
        blank=True,
        null=True,
    )

    longitude = models.DecimalField(
        max_digits=25,
        decimal_places=5,
        blank=True,
        null=True,
    )

    latitude = models.DecimalField(
        max_digits=25,
        decimal_places=5,
        blank=True,
        null=True,
    )

    height_from_sea_level = models.IntegerField(
        max_length=6,
        blank=True,
        null=True
    )

    indoor_information = models.CharField(
        max_length=256,
        blank=True,
        null=True,
    )

    orientation = models.CharField(
        max_length=256,
        blank=True,
        null=True,
    )

    def __unicode__(self):
        return self.name


class LocationType(CreateUpdateMixin):

    name = models.CharField(
        max_length=100,
    )

    description = models.TextField(
        blank=True,
        null=True,
    )

    def __unicode__(self):
        return self.name


class LocationPersonCrossRef(CreateUpdateMixin):
    # LocationUserCrossRef links the Location Class to the User Class

    # FK to Location class
    location = models.ForeignKey(
        'Location',
    )

    # FK to User class
    person = models.ForeignKey(
        'users.Person',
    )

    common_name = models.CharField(
        max_length=100,
    )

    relationship_type = models.ForeignKey(
        'LocationPersonRelationshipType'
    )


class LocationPersonRelationshipType(CreateUpdateMixin, NameDescMixin):
    pass


class LocationThingCrossRef(CreateUpdateMixin):

    # FK to Location class
    location = models.ForeignKey(
        'Location'
    )

    # FK to User class
    thing = models.ForeignKey(
        'things.Thing'
    )

    common_name = models.CharField(
        max_length=45,
        blank=True,
        null=True,
    )

    relationship_type = models.ForeignKey(
        'LocationThingRelationshipType',
        blank=True,
        null=True,
    )


class LocationThingRelationshipType(CreateUpdateMixin, NameDescMixin):



class LocationToLocationCrossRef(CreateUpdateMixin):

    loc_one = models.ForeignKey(
        'Location',
        related_name='loc_one',
    )

    loc_two = models.ForeignKey(
        'Location',
        related_name='loc_two',
    )

    relationship_type = models.ForeignKey(
        'LocationToLocationRelationshipType',
    )

    relationship_description = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name_plural = u'Relationships'


class LocationToLocationRelationshipType(CreateUpdateMixin, NameDescMixin):
    pass

    class Meta:
        verbose_name_plural = u'L2L Relationships'


class LocationSensorCrossRef(CreateUpdateMixin):
    # LocationSensorCrossRef links the Location Class to the Sensor Class

    # FK to Location class
    location = models.ForeignKey(
        'Location',
    )

    # FK to Sensor class
    sensor = models.ForeignKey(
        'things.Sensor',
    )

    common_name = models.CharField(
        max_length=100,
    )

    relationship_type = models.ForeignKey(
        'LocationSensorRelationshipType'
    )


class LocationSensorRelationshipType(CreateUpdateMixin, NameDescMixin):
    pass


class InventoryLocationSecondary(CreateUpdateMixin):

    # FK to Location class
    location = models.ForeignKey(
        'Location'
    )

    # FK to ThingType
    thing = models.ForeignKey(
        'things.Thing',
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
