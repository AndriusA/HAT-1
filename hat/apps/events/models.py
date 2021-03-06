from django.db import models

from ...models import CreateUpdateMixin, NameDescMixin

# Constants for Event Status Codes, called in Event.event_status
EVENT_STATUS_CODES = (
    ('1', 'Ongoing'),
    ('2', 'In the future'),
    ('3', 'Happened'),
    ('4', 'Never happened'),
)

# Constants for Event Time Types, called in Event.time_type
EVENT_TIME_TYPES = (
    ('1', 'Start'),
    ('2', 'End'),
    ('3', 'Ongoing'),
    ('4', 'One-off'),
    ('5', 'Recurrent'),
)

from datetime import date, datetime


# Main Event class, linked to:
# - Thing VIA EventThingCrossReference class
# - User VIA EventUserCrossReference class
# - Location VIA EventLocationCrossReference class

class Event(CreateUpdateMixin, NameDescMixin):

    type = models.ForeignKey(
        'EventType',
        blank=False,
        null=False,
        max_length=45
    )

    status = models.PositiveIntegerField(
        max_length=1,
        choices=EVENT_STATUS_CODES
    )

    event_time_type = models.PositiveIntegerField(
        max_length=1,
        choices=EVENT_TIME_TYPES
    )

    start_date = models.DateTimeField(
        blank=False,
        null=False,
        default=lambda: datetime.now()
    )

    end_date = models.DateTimeField(
        blank=False,
        null=False,
        default=lambda: datetime.now()
    )

    recurrence_interval = models.PositiveIntegerField(
        max_length=100,
        blank=True,
        null=True,
    )

    confirmation = models.BooleanField(
        default=False,
    )


# EventType class, determines the type of the event
# Could potentially be populated via 'choices' depending on requirement
class EventType(CreateUpdateMixin, NameDescMixin):
    pass


class EventToEventCrossRef(CreateUpdateMixin):

    event_one = models.ForeignKey(
        Event,
        related_name='ev_one',
    )

    event_two = models.ForeignKey(
        Event,
        related_name='ev_two',
    )

    relationship_type = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )

    relationship_description = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name_plural = u'EventToEventRelationships'


# EventSensorDataCrossReference is a link between Event and Sensor Data
class EventSensorDataCrossRef(CreateUpdateMixin):

    #FK to Event class
    event = models.ForeignKey(
        Event
    )

    #FK to Thing class
    sensor_data = models.ForeignKey(
        'things.SensorData'
    )

    relationship_type = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )

# EventLocationCrossReflinks the Event class and the Location class
class EventLocationCrossRef(CreateUpdateMixin):

    #FK to Event class
    event = models.ForeignKey(
        Event
    )

    #FK to Location class
    location = models.ForeignKey(
        'locations.Location'
    )

    relationship_type = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )

# EventUserCrossRef links the Event class and the User class
class EventPersonCrossRef(CreateUpdateMixin):

    #FK to Event class
    event = models.ForeignKey(
        Event
    )

    #FK to User class
    person = models.ForeignKey(
        'users.Person'
    )

    user_defined_name = models.CharField(
        max_length=45,
        blank=True,
        null=True,
    )

    relationship_type = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )

################################################################
# Code additions made after code handover from "One Space Media"
################################################################


# DataDebit class, defines the data direct debit
class DataDebit(CreateUpdateMixin, NameDescMixin):

    sell_rent = models.BooleanField(
        default=False
        )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
        )

    event_time_type = models.PositiveIntegerField(
        max_length=1,
        choices=EVENT_TIME_TYPES
    )

    contract_start_date = models.DateTimeField(
        blank=False,
        null=False,
        default=lambda: datetime.now()
    )

    contract_end_date = models.DateTimeField(
        blank=False,
        null=False,
        default=lambda: datetime.now()
    )

    rolling = models.BooleanField(
        default=False,
    )


#Data Debit and Recipient cross relationship class
class DataDebitRecipientCrossRef(CreateUpdateMixin):

    #FK to DataDebit Class
    DataDebit = models.ForeignKey(
        DataDebit
    )

     #FK to Recipient class
    Recipient = models.ForeignKey(
        'users.Recipient'
    )

    relationship_type = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )

#Direct Debit and Recipient cross relationship class
class DataDebitEventCrossRef(CreateUpdateMixin):

    #FK to DataDebit Class
    DataDebit = models.ForeignKey(
        DataDebit
    )

    #FK to Event class
    Event = models.ForeignKey(
        'events.Event'
    )

    relationship_type = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )