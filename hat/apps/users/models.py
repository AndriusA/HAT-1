from django.db import models


# This is extended by a pretty huge number of classes across all apps in the system.
class CreateUpdateMixin(models.Model):

    date_created = models.DateTimeField(
    )

    last_updated = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        abstract = True


class NameDescMixin(models.Model):

    name = models.CharField(
        max_length=100,
    )

    description = models.TextField(
        blank=True,
        null=True,
    )

    def __unicode__(self):
        return self.name

    class Meta:
        abstract = True


class AddressMixin(models.Model):

    number = models.CharField(
        "house name",
        max_length=100,
        blank=True,
        null=True,
    )

    address_line_1 = models.CharField(
        "address 1",
        max_length=100,
        blank=True,
        null=True,
    )

    address_line_2 = models.CharField(
        "address 2",
        max_length=100,
        blank=True,
        null=True,
    )

    city = models.CharField(
        "town",
        max_length=64,
        blank=True,
        null=True,
    )

    county = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )

    postal_code = models.CharField(
        max_length=15,
        blank=True,
        null=True,
    )

    class Meta:
        abstract = True
