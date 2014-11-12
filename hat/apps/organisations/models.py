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
