from django.http import HttpResponse, QueryDict
from django.views.generic import View, TemplateView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from ..system.models import UnitOfMeasurement
from ..things.models import Thing, ThingSensorCrossRef, SensorDataType, SensorData
from ..events.models import EVENT_STATUS_CODES, EVENT_TIME_TYPES, Event, EventType, EventPersonCrossRef, EventLocationCrossRef, EventSensorDataCrossRef
from ..locations.models import Location, LocationType
from ..users.models import Person
from django_extensions.db.fields import UUIDField
from ..users.models import Recipient

from datetime import datetime

import json
from pprint import pformat

# Api documentation viewer
class ApiDocumentation(TemplateView):
    template_name = "api/documentation.html"

    def get_context_data(self, **kwargs):
        context = super(ApiDocumentation, self).get_context_data(**kwargs)
        context['units'] = UnitOfMeasurement.objects.all()
        context['data_types'] = SensorDataType.objects.all()
        context['event_types'] = EventType.objects.all()
        context['event_statuses'] = EVENT_STATUS_CODES
        context['event_time_types'] = EVENT_TIME_TYPES
        context['location_types'] = LocationType.objects.all()
        return context


class ApiException(Exception):
    pass


# Api authentication mixin
class ApiAuthenticationMixin(View):

    required_fields = []

    def __init__(self, **kwargs):
        # Set blank response data
        self.response_data = {
            'response': '',
            'errors': []
        }

        self.post_data = None

        self.device = None

    # Disable CSRF and run auth check
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):

        # Manually parse post for devices that do not support headers
        self.request.POST = QueryDict(request.body)

        # Auth check
        if not self.check_auth(request):
            return self.response(request, *args, **kwargs)

        # Data check
        if request.META['REQUEST_METHOD'] == 'POST':
            if 'data' not in request.POST:
                self.add_error('Data field is missing from POST.')
                return self.response(request, *args, **kwargs)
            else:
                try:
                    self.post_data = json.loads(request.POST.get("data"))
                except Exception:
                    self.add_error('Json decode error'.format(
                        ', '.join(self.required_fields)
                    ))
                    return self.response(request, *args, **kwargs)

        # Validation check
        for field in self.required_fields:
            if field not in self.post_data:
                self.add_error('One or more required fields are missing. Fields required are: {}.'.format(
                    ', '.join(self.required_fields)
                ))
                return self.response(request, *args, **kwargs)

        return super(ApiAuthenticationMixin, self).dispatch(request, *args, **kwargs)

    # Check to see if the requested method actually exists, a device is being used, and is allowed to use the
    # requested method
    def check_auth(self, request):

        # Make sure we have the device ID header
        device = request.META.get('HTTP_DEVICE_ID', None)
        if not device:
            if not request.POST.get("device_id", None):
                self.add_error('Device authentication missing.')
                return False
            else:
                device = request.POST.get("device_id", None)

        try:
            self.device = Thing.objects.get(device_id=device)
        except Exception:
            self.add_error('Device not found with the ID of "{}".'.format(
                device
            ))
            return False

        return True

    # Api json response
    def response(self, request, *args, **kwargs):

        # Set the response result based on errors
        if not self.has_errors():
            self.response_data['response'] = 'success'
            self.response_data.pop("errors", None)
        else:
            self.response_data['response'] = 'error'

        # Return json response
        return HttpResponse(json.dumps(self.response_data), content_type="application/json")

    def http_method_not_allowed(self, request, *args, **kwargs):
        self.add_error('Not implemented')
        return self.response(request, *args, **kwargs)

    # Check to see if the current request has any errors
    def has_errors(self):
        return len(self.response_data['errors']) > 0

    # Add an error to the respose
    def add_error(self, error):
        self.response_data['errors'].append(error)

    # Add data to the response
    def add_data(self, key, value):
        self.response_data[key] = value


class SensorsView(ApiAuthenticationMixin):

    def get(self, request, *args, **kwargs):

        # Get sensors
        sensors = ThingSensorCrossRef.objects.filter(thing=self.device)

        # Set sensors
        self.add_data('sensors', [{sensor_ref.sensor.sensor_id: sensor_ref.sensor.name} for sensor_ref in sensors])

        # Call the super post, this does the error checking
        return super(SensorsView, self).response(request, *args, **kwargs)


class SensorDataView(ApiAuthenticationMixin):

    required_fields = ['id', 'value', 'unit', 'data_type']

    def save_data(self, data):

        # Main try catch, this allows me to be more specific with errors
        try:

            # Get sensor
            try:
                sensor = ThingSensorCrossRef.objects.get(thing=self.device, sensor__sensor_id=data.get('id')).sensor
            except ThingSensorCrossRef.DoesNotExist:
                raise ApiException("Device sensor with the id '{}' could not be found.".format(data.get('id')))

            # Convert timestamp from INT to datetime object
            if not data.get('timestamp', None):
                timestamp = datetime.now()
            else:
                timestamp = datetime.fromtimestamp(float(data.get('timestamp')))

            # Get value
            value = data.get('value')

            # Get unit
            unit = UnitOfMeasurement.objects.get(pk=data.get('unit'))

            # Get data type
            data_type = SensorDataType.objects.get(pk=data.get('data_type'))

            # Get description
            description = data.get('description', "")

            if not isinstance(value, list):
                value = [value]

            for data in value:

                # Add and save the sensor data
                sensor_data = SensorData(
                    date_created=timestamp,
                    sensor=sensor,
                    type=data_type,
                    unit=unit,
                    value=data,
                    source_description=description
                )

                sensor_data.save()

                self.sensor_data_ids.append(sensor_data.pk)

        except ApiException as error:

            # Get error string
            error_string = str(error) if str(error) != "" else "Unknown error has occured."
            self.add_error(error_string)


    def post(self, request, *args, **kwargs):

        self.sensor_data_ids = []

        self.save_data(self.post_data)

        self.add_data('sensor_data_ids', self.sensor_data_ids)

        return super(SensorDataView, self).response(request, *args, **kwargs)


class BatchSensorDataView(ApiAuthenticationMixin):

    required_fields = ['sensor_data']

    def save_data(self, data):

        # Main try catch, this allows me to be more specific with errors
        try:

            # Get sensor
            try:
                sensor = ThingSensorCrossRef.objects.get(thing=self.device, sensor__sensor_id=data.get('id')).sensor
            except ThingSensorCrossRef.DoesNotExist:
                raise ApiException("Device sensor with the id '{}' could not be found.".format(data.get('id')))

            # Convert timestamp from INT to datetime object
            if not data.get('timestamp', None):
                timestamp = datetime.now()
            else:
                timestamp = datetime.fromtimestamp(float(data.get('timestamp')))

            # Get value
            value = data.get('value')

            # Get unit
            unit = UnitOfMeasurement.objects.get(pk=data.get('unit'))

            # Get data type
            data_type = SensorDataType.objects.get(pk=data.get('data_type'))

            # Get description
            description = data.get('description', "")

            if not isinstance(value, list):
                value = [value]

            for data in value:

                # Add and save the sensor data
                sensor_data = SensorData(
                    date_created=timestamp,
                    sensor=sensor,
                    type=data_type,
                    unit=unit,
                    value=data,
                    source_description=description
                )

                sensor_data.save()

                self.sensor_data_ids.append(sensor_data.pk)


        except ApiException as error:

            # Get error string
            error_string = str(error) if str(error) != "" else "Unknown error has occured."
            self.add_error(error_string)

    def post(self, request, *args, **kwargs):

        self.sensor_data_ids = []

        # Loop the sensor data we have
        for data in self.post_data.get('sensor_data'):

            data_set_valid = True

            # Validation check
            for field in SensorDataView.required_fields:
                if field not in data:
                    data_set_valid = False
                    continue;

            if data_set_valid:
                self.save_data(data)

        self.add_data('sensor_data_ids', self.sensor_data_ids)

        return super(BatchSensorDataView, self).response(request, *args, **kwargs)


class CreateEventView(ApiAuthenticationMixin):

    required_fields = ['name', 'type', 'status', 'time_type', 'start_timestamp', 'end_timestamp']

    def post(self, request, *args, **kwargs):

        # Main try catch, this allows me to be more specific with errors
        try:

            # Get event name
            name = self.post_data.get('name', '')

            # Get description
            description = self.post_data.get('description', '')

            # Get type
            try:
                type = EventType.objects.get(pk=int(self.post_data.get('type')))
            except Exception:
                raise ApiException("Invalid event type provided.")

            # Get status
            if str(self.post_data.get('status')) in dict(EVENT_STATUS_CODES).keys():
                status = str(self.post_data.get('status'))
            else:
                raise ApiException("Invalid event status provided.")

            # Get time type
            if str(self.post_data.get('time_type')) in dict(EVENT_TIME_TYPES).keys():
                time_type = str(self.post_data.get('time_type'))
            else:
                raise ApiException("Invalid event time type provided.")

            try:
                # Convert start and end timestamps from INT to datetime objects
                start_timestamp = datetime.fromtimestamp(float(self.post_data.get('start_timestamp')))
                end_timestamp = datetime.fromtimestamp(float(self.post_data.get('end_timestamp')))
            except:
                raise ApiException("There was an error converting converting the start and end timestamp values to floats.")

            # Add and save the event
            event = Event(
                name=name,
                description=description,
                type=type,
                status=status,
                event_time_type=time_type,
                start_date=start_timestamp,
                end_date=end_timestamp,
                date_created=datetime.now()
            )

            event.save()

            # Loop through sensor data and join it to the event
            for sensor_data_id in self.post_data.get('sensor_data', []):

                # Get the sensor data
                try:
                    sensor_data = SensorData.objects.get(pk=sensor_data_id)
                except Exception:
                    raise ApiException("Sensor data with the ID of {} does not exist.".format(
                        sensor_data_id
                    ))

                # Add the sensor to the event sensor ref table
                sensor_data_ref = EventSensorDataCrossRef(
                    event=event,
                    sensor_data=sensor_data,
                    date_created=datetime.now()
                )
                sensor_data_ref.save()

            # Loop through locations data and join it to the event
            for location_id in self.post_data.get('locations', []):

                # Get the location
                try:
                    location = Location.objects.get(pk=location_id)
                except Exception:
                    raise ApiException("Location with the ID of {} does not exist.".format(
                        location_id
                    ))

                # Add the location to the event location ref table
                location_ref = EventLocationCrossRef(
                    event=event,
                    location=location,
                    date_created=datetime.now()
                )
                location_ref.save()


            # Loop through people data and join it to the event
            for person_id in self.post_data.get('people', []):

                # Get the person
                try:
                    person = Person.objects.get(pk=person_id)
                except Exception:
                    raise ApiException("Person with the ID of {} does not exist.".format(
                        person_id
                    ))

                # Add the person to the event person ref table
                person_ref = EventPersonCrossRef(
                    event=event,
                    person=person,
                    date_created=datetime.now()
                )
                person_ref.save()


        except ApiException as error:

            # Get error string
            error_string = str(error) if str(error) != "" else "Unknown error has occured."
            self.add_error(error_string)

        return super(CreateEventView, self).response(request, *args, **kwargs)


class CreateLocationView(ApiAuthenticationMixin):

    required_fields = ['name', 'type']

    def post(self, request, *args, **kwargs):

        # Main try catch, this allows me to be more specific with errors
        try:

            # Get location name
            name = self.post_data.get('name', '')

            # Get description
            description = self.post_data.get('description', '')

            # Get type
            try:
                type = LocationType.objects.get(pk=int(self.post_data.get('type', 0)))
            except Exception:
                raise ApiException("Invalid location type provided.")

            # Get address data
            address = self.post_data.get('address', {})
            house_name = address.get('house_name', '')
            address_1 = address.get('address_1', '')
            address_2 = address.get('address_2', '')
            town = address.get('town', '')
            county = address.get('county', '')
            postal_code = address.get('postal_code', '')

            # Get longitude and latitude
            longitude = float(self.post_data.get('longitude', 0))
            latitude = float(self.post_data.get('latitude', 0))

            # Get height from sea level
            height_from_sea_level = int(self.post_data.get('height_from_sea_level', 0))

            # Get indoor information
            indoor_information = self.post_data.get('indoor_information', '')

            # Get oriention
            orientation = self.post_data.get('orientation', '')

            # Add and save the location
            location, location_created = Location.objects.get_or_create(
                name=name,
                description=description,
                type=type,
                longitude=longitude,
                latitude=latitude,
                height_from_sea_level=height_from_sea_level,
                indoor_information=indoor_information,
                orientation=orientation,

                number=house_name,
                address_line_1=address_1,
                address_line_2=address_2,
                city=town,
                county=county,
                postal_code=postal_code,
                defaults={
                    'date_created': datetime.now()
                }
            )

            # Return the location ID
            self.add_data('location_id', location.pk)

        except ApiException as error:

            # Get error string
            error_string = str(error) if str(error) != "" else "Unknown error has occured."
            self.add_error(error_string)

        return super(CreateLocationView, self).response(request, *args, **kwargs)


class CreateRecipientView(ApiAuthenticationMixin):

    required_fields = ['user_GUID', 'name']

    def post(self, request, *args, **kwargs):

        # Main try catch, this allows me to be more specific with errors
        try:

            # Get persons first name and last name
            user_GUID = self.post_data.get('user_GUID', '')
            name = self.post_data.get('name', '')

            # Add and save the person
            recipient, recipient_created = Recipient.objects.get_or_create(
                name=name,
                user_GUID=user_GUID,
                defaults={
                    'date_created': datetime.now()
                }
            )
            recipient.save()

            # Return the person ID
            self.add_data('recipient_id', recipient.pk)

        except ApiException as error:

            # Get error string
            error_string = str(error) if str(error) != "" else "Unknown error has occured."
            self.add_error(error_string)

        return super(CreateRecipentView, self).response(request, *args, **kwargs)


class CreatePersonView(ApiAuthenticationMixin):

    required_fields = ['first_name', 'last_name']

    def post(self, request, *args, **kwargs):

        # Main try catch, this allows me to be more specific with errors
        try:

            # Get persons first name and last name
            first_name = self.post_data.get('first_name', '')
            last_name = self.post_data.get('last_name', '')

            # Add and save the person
            person, person_created = Person.objects.get_or_create(
                user=self.device.user,
                first_name=first_name,
                last_name=last_name,
                defaults={
                    'date_created': datetime.now()
                }
            )
            person.save()

            # Return the person ID
            self.add_data('person_id', person.pk)

        except ApiException as error:

            # Get error string
            error_string = str(error) if str(error) != "" else "Unknown error has occured."
            self.add_error(error_string)

        return super(CreatePersonView, self).response(request, *args, **kwargs)



