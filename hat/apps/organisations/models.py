from django.db import models

from ...models import AddressMixin, CreateUpdateMixin, NameDescMixin


class Organisation(NameDescMixin):

    type = models.ForeignKey(
        'OrganisationType'
    )

    url = models.URLField(
        blank=True,
        null=True,
    )

    # Returns true if the organisation has no end_date
    def is_current(self):
        return bool(self.end_date)

    class Meta:
        verbose_name_plural = u'Organisations'


class OrganisationType(CreateUpdateMixin, NameDescMixin):
    pass

    class Meta:
        verbose_name_plural = u'Organisation Types'


class OrganisationAddress(CreateUpdateMixin, AddressMixin):

    #FK to person the address belongs to
    organisation = models.ForeignKey(
        Organisation,
    )

    is_current = models.BooleanField(
        default=False,
    )

    class Meta:
        verbose_name_plural = u'Organisation Addresses'


class OrganisationLocationCrossRef(CreateUpdateMixin):
    # LocationSensorCrossRef links the Location Class to the Sensor Class

    # FK to Location class
    location = models.ForeignKey(
        'locations.Location',
    )

    # FK to Sensor class
    Organisation = models.ForeignKey(
        'Organisation',
    )

    common_name = models.CharField(
        max_length=100,
    )

    relationship_type = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )


class OrganisationSensorRef(CreateUpdateMixin):
    # LocationSensorCrossRef links the Location Class to the Sensor Class

    # FK to Location class
    Organisation = models.ForeignKey(
        'Organisation',
    )

    # FK to User class
    Sensor = models.ForeignKey(
        'things.Sensor',
    )

    common_name = models.CharField(
        max_length=100,
    )

    relationship_type = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )


class OrganisationContactMethod(CreateUpdateMixin):

    # FK to Organisation class
    Organisation = models.ForeignKey(
        Organisation
    )

    type = models.ForeignKey(
        'system.ContactMethodType'
    )

    detail = models.CharField(
        max_length=254,
    )

    priority = models.PositiveIntegerField(
        max_length=5,
        default=0,
    )

    class Meta:
        verbose_name_plural = u'Organisation Contact Methods'
