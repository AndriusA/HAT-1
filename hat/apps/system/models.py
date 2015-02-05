from django.db import models

from ...models import CreateUpdateMixin, NameDescMixin


# Log is designed to log system events to the database.
# Full functionality is yet to be discussed (valid as of 01/07/2014).
class EventLog(models.Model):

    event_type = models.CharField(
        max_length=45,
    )

    date = models.DateField()

    time = models.TimeField()

    creator = models.CharField(
        max_length=100,
    )

    command = models.CharField(
        max_length=100,
    )

    result = models.CharField(
        max_length=45,
    )


# System wide Currency table
class Currency(CreateUpdateMixin):

    name = models.CharField(
        max_length=45,
        unique=True,
    )

    code = models.CharField(
        max_length=16,
    )

    symbol = models.CharField(
        max_length=16,
        blank=True,
    )

    class Meta:
        ordering = ('name',)
        verbose_name_plural = u'currencies'


class UnitOfMeasurement(CreateUpdateMixin, NameDescMixin):

    symbol = models.CharField(
        max_length=16,
        blank=False,
        null=True,
    )

    class Meta:
        verbose_name_plural = u'Units'

class UnitOfMeasurementThingPropertyCrossRef(CreateUpdateMixin):

     #FK to unit_id
        unit_id = models.ForeignKey(
        'UnitOfMeasurement',
    )


    thing_property = models.ForeignKey(
        'things.ThingProperty'
    )

    relationship_type = models.ForeignKey(
        'UnitOfMeasurementRelationshipType'
    )

    is_current = models.BooleanField(
        default=False,
    )

class UnitOfMeasurementRelationshipType(CreateUpdateMixin, NameDescMixin):
pass
# System wide Nationality table
class Nationality(CreateUpdateMixin, NameDescMixin):

    class Meta:
        verbose_name_plural = u'Nationalities'


# System wide Ethnicity table
class Ethnicity(CreateUpdateMixin, NameDescMixin):

    class Meta:
        verbose_name_plural = u'Ethnicities'


# System wide Gender table
class Gender(CreateUpdateMixin, NameDescMixin):

    class Meta:
        verbose_name_plural = u'Genders'


# System wide MaritalStatus table
class MaritalStatus(CreateUpdateMixin, NameDescMixin):

    class Meta:
        verbose_name_plural = u'Marital Statuses'


# System wide Religion table
class Religion(CreateUpdateMixin, NameDescMixin):

    class Meta:
        verbose_name_plural = u'Religions'


# System wide Prefixes table
class Prefix(CreateUpdateMixin, NameDescMixin):

    class Meta:
        verbose_name_plural = u'Prefixes'


# System wide ContactMethodTypes table
class ContactMethodType(CreateUpdateMixin, NameDescMixin):

    class Meta:
        verbose_name_plural = u'Contact Method Types'