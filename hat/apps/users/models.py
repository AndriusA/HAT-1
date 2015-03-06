from django_extensions.db.fields import UUIDField
from django.db import models
from django.contrib.auth.models import User

from ...models import AddressMixin, CreateUpdateMixin, NameDescMixin


class UserAccount(CreateUpdateMixin):

    username = models.CharField(
        max_length=100,
        unique=True,
    )

    password = models.CharField(
        max_length=128,
    )


class AffiliateService(CreateUpdateMixin):

    # FK to User class
    user = models.ForeignKey(
        User
    )

    service_type = models.CharField(
        max_length=100,
    )

    # User's ID if a web/social networking platform
    user_web_id = models.CharField(
        max_length=100,
    )

    # User's URL if a web/social networking platform
    url = models.URLField(
        blank=True,
        null=True,
    )

    displayable = models.BooleanField(
        default=True,
    )


class Person(CreateUpdateMixin):

    # FK to person, all users tied to a person
    user = models.ForeignKey(
        User,
        related_name='related_user_ac'
    )

    avatar = models.ImageField(
        blank=True,
        null=True,
        upload_to="uploads/files",
    )

    first_name = models.CharField(
        max_length=100,
    )

    middle_name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )

    last_name = models.CharField(
        max_length=100,
    )

    user_GUID = UUIDField(

    )

    date_of_birth = models.DateField(
        blank=True,
        null=True,
    )

    email_address = models.EmailField(
        max_length=254,
        blank=True,
        null=True,
    )

    gender = models.ForeignKey(
        'system.Gender',
        blank=True,
        null=True,
    )

    prefix = models.ForeignKey(
        'system.Prefix',
        blank=True,
        null=True,
    )

    nationality = models.ForeignKey(
        'system.Nationality',
        blank=True,
        null=True,
    )

    ethnicity = models.ForeignKey(
        'system.Ethnicity',
        blank=True,
        null=True,
    )

    religion = models.ForeignKey(
        'system.Religion',
        blank=True,
        null=True,
    )

    marital_status = models.ForeignKey(
        'system.MaritalStatus',
        blank=True,
        null=True,
    )

    related_organisations = models.ForeignKey(
        'organisations.Organisation',
        related_name='person_related_organisations',
        blank=True,
        null=True,
    )

    currency = models.ForeignKey(
        'system.Currency',
        blank=True,
        null=True,
    )

    annual_income = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        blank=True,
        null=True,
    )

    person_id = models.CharField(
        max_length=36,
        default=lambda: str(uuid4())
    )

    #FK to person the address belongs to
    address = models.ManyToManyField(
        'PersonAddress',
        blank=True,
        null=True,
    )

    def __unicode__(self):
        return self.first_name

    class Meta:
        verbose_name_plural = u'People'


class PersonAddress(CreateUpdateMixin, AddressMixin):

    is_current = models.BooleanField(
        default=False,
    )

    class Meta:
        verbose_name_plural = u'People Addresses'

class PersonAddressLocationCrossRef(CreateUpdateMixin):

    #FK to Person Class
    person_address_id = models.ForeignKey(
        PersonAddress
    )

     #FK to DataDebit class
    location_id = models.ForeignKey(
        'locations.location'
    )

    relationship_type = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )


class PersonContactMethod(CreateUpdateMixin):

    # FK to Person class
    person = models.ForeignKey(
        Person,
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
        verbose_name_plural = u'People Contact Methods'


class PersonOrganisationCrossRef(CreateUpdateMixin):

    # FK to Person class
    person = models.ForeignKey(
        'Person'
    )

    organisation = models.ForeignKey(
        'organisations.Organisation'
    )

    person_role = models.CharField(
        max_length=100,
    )

    start_date = models.DateField()

    end_date = models.DateField(
        blank=True,
        null=True,
    )


class PersonToPersonCrossRef(CreateUpdateMixin):

    person_one = models.ForeignKey(
        'Person',
        related_name='person1',
    )

    person_two = models.ForeignKey(
        'Person',
        related_name='person2',
    )

    relationship_type = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name_plural = u'Relationships'


class DynamicType(CreateUpdateMixin, NameDescMixin):

         #FK to Person
    person = models.ForeignKey(
        Person,
    )


    sensor_data = models.ForeignKey(
        'things.SensorData'
    )

    source_description = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )

################################################################
# Code additions made after code handover from "One Space Media"
################################################################


class Recipient(CreateUpdateMixin, NameDescMixin):

    # Reciepient Identifier number
    recipient_UUID = UUIDField(

    )


class PersonDataDebitCrossRef(CreateUpdateMixin):

    #FK to Person Class
    person = models.ForeignKey(
        Person
    )

     #FK to DataDebit class
    DataDebit = models.ForeignKey(
        'events.DataDebit'
    )

    relationship_type = models.CharField(
    max_length=100,
    blank=True,
    null=True,
    )