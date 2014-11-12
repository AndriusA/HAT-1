# Core imports
from django.views.generic import TemplateView, View
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from ..things.models import Thing, SensorData, Sensor
from ..locations.models import LocationThingCrossRef, Location
from ..events.models import Event, EventType, EventSensorDataCrossRef, EventLocationCrossRef, EventToEventCrossRef

from datetime import date, datetime, timedelta, time

import json

class WelcomeView(TemplateView):
    template_name = 'site/welcome.html'


class MyProfileView(TemplateView):
    template_name = 'site/my-profile.html'

    def get_context_data(self, **kwargs):
        context = super(MyProfileView, self).get_context_data(**kwargs)
        context['user'] = self.request.user

        # Get the users device locations
        context['device_locaitions'] = LocationThingCrossRef.objects.filter(thing__in=Thing.objects.filter(user=self.request.user)).distinct('location')

        return context


class LocationListView(TemplateView):
    template_name = 'site/location-list.html'

    def get_context_data(self, **kwargs):
        context = super(LocationListView, self).get_context_data(**kwargs)
        context['locations'] = Location.objects.all()
        return context


class LocationDetailView(TemplateView):
    template_name = 'site/location-detail.html'

    def get_context_data(self, **kwargs):
        context = super(LocationDetailView, self).get_context_data(**kwargs)
        context['location'] = get_object_or_404(Location, pk=kwargs.get('location_id'))
        return context


class LocationActivityView(TemplateView):
    template_name = 'site/location-activity.html'

    def get_context_data(self, **kwargs):
        context = super(LocationActivityView, self).get_context_data(**kwargs)
        context['location'] = get_object_or_404(Location, pk=kwargs.get('location_id'))
        context['page'] = self.kwargs.get('page', None)
        return context


class DataView(TemplateView):
    template_name = 'site/data.html'

    def get_context_data(self, **kwargs):
        context = super(DataView, self).get_context_data(**kwargs)
        context['device_count'] = Thing.objects.filter(user=self.request.user, is_service=False).count()
        return context

class ConnectedHatsView(TemplateView):
    template_name = 'site/connected-hats.html'


class TimeView(TemplateView):
    template_name = 'site/time.html'


class EventListView(TemplateView):
    template_name = 'site/event-list.html'

    def get_context_data(self, **kwargs):
        context = super(EventListView, self).get_context_data(**kwargs)

        event_list = Event.objects.all()

        page = self.kwargs.get('page', 1)

        paginator = Paginator(event_list, 20)

        try:
            events = paginator.page(page)
        except PageNotAnInteger:
            events = paginator.page(1)
        except EmptyPage:
            events = paginator.page(paginator.num_pages)

        context['events'] = events

        return context


class EventDetailView(TemplateView):
    template_name = 'site/event-detail.html'

    def get_context_data(self, **kwargs):
        context = super(EventDetailView, self).get_context_data(**kwargs)
        context['event'] = get_object_or_404(Event, pk=kwargs.get('event_id'))
        context['events'] = EventToEventCrossRef.objects.filter(event_one=context['event'])
        return context


class EventCreateView(TemplateView):
    template_name = 'site/event-create.html'

    def get_context_data(self, **kwargs):
        context = super(EventCreateView, self).get_context_data(**kwargs)
        context['hours'] = xrange(1, 13)
        context['days'] = xrange(1, 32)
        context['months'] = [date(2014, month, 1) for month in xrange(1, 13)]
        context['years'] = xrange(date.today().year, 1900, -1)

        context['start_date'] = datetime.now()
        context['end_date'] = datetime.now()

        context['locations'] = Location.objects.all()
        context['devices'] = Thing.objects.filter(
            user=self.request.user,
            is_service=False
        )
        context['events'] = Event.objects.all();

        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        name = request.POST.get('event_name', '')

        start_date = datetime.strptime("{}-{}-{} {}:{}:00{}".format(
            request.POST.get('start_date_year'),
            request.POST.get('start_date_month'),
            request.POST.get('start_date_day'),
            request.POST.get('start_time_hour'),
            request.POST.get('start_time_minute'),
            request.POST.get('start_time_suffix')
        ), "%Y-%m-%d %I:%M:%S%p")

        end_date = datetime.strptime("{}-{}-{} {}:{}:00{}".format(
            request.POST.get('start_date_year'),
            request.POST.get('start_date_month'),
            request.POST.get('start_date_day'),
            request.POST.get('end_time_hour'),
            request.POST.get('end_time_minute'),
            request.POST.get('end_time_suffix')
        ), "%Y-%m-%d %I:%M:%S%p")

        # We need a user created event type, make one if it doesn't exists

        device_id_list = request.POST.get('devices', '').split(',')
        device_id_list = [ int(x) for x in filter(None, device_id_list) ]
        devices = Thing.objects.filter(pk__in=device_id_list)

        location_id_list = request.POST.get('locations', '').split(',')
        location_id_list = [ int(x) for x in filter(None, location_id_list) ]
        locations = Location.objects.filter(pk__in=location_id_list)

        event_id_list = request.POST.get('events', '').split(',')
        event_id_list = [ int(x) for x in filter(None, event_id_list) ]
        events = Event.objects.filter(pk__in=event_id_list)

        # Get the sensor data using the devices
        sensor_data = SensorData.objects.filter(
            sensor__in=Sensor.objects.filter(thingsensorcrossref__thing__in=devices),
            date_created__range=(start_date, end_date)
        )

        user_created_type, type_created = EventType.objects.get_or_create(
            name="User created event",
            description="Event created by the user",
            defaults={
                'date_created' : datetime.now()
            }
        )

        event = Event(
            name=name,
            description="",
            type=user_created_type,
            status=3,
            event_time_type=4,
            date_created=datetime.now(),
            start_date=start_date,
            end_date=end_date
        )

        event.save()


        # Loop sensor data and add the event sensor data references
        for data in sensor_data:
            sensor_data_ref = EventSensorDataCrossRef(
                event=event,
                sensor_data=data,
                date_created=datetime.now()
            )
            sensor_data_ref.save()


        # Loop locations and create a location event ref
        for location in locations:
            location_event_ref = EventLocationCrossRef(
                event=event,
                location=location,
                date_created=datetime.now()
            )
            location_event_ref.save()


        # Loop events and create a event event ref
        for sub_event in events:
            event_event_ref = EventToEventCrossRef(
                event_one=event,
                event_two=sub_event,
                date_created=datetime.now()
            )
            event_event_ref.save()


        return redirect('/events')


class EventSummary(TemplateView):
    template_name = 'site/event-summary.html'

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        context['name'] = request.POST.get('event_name', '')

        context['start_date'] = datetime.strptime("{}-{}-{} {}:{}:00{}".format(
            request.POST.get('start_date_year'),
            request.POST.get('start_date_month'),
            request.POST.get('start_date_day'),
            request.POST.get('start_time_hour'),
            request.POST.get('start_time_minute'),
            request.POST.get('start_time_suffix')
        ), "%Y-%m-%d %I:%M:%S%p")

        context['end_date'] = datetime.strptime("{}-{}-{} {}:{}:00{}".format(
            request.POST.get('start_date_year'),
            request.POST.get('start_date_month'),
            request.POST.get('start_date_day'),
            request.POST.get('end_time_hour'),
            request.POST.get('end_time_minute'),
            request.POST.get('end_time_suffix')
        ), "%Y-%m-%d %I:%M:%S%p")

        device_id_list = request.POST.get('devices', '').split(',')
        device_id_list = [ int(x) for x in filter(None, device_id_list) ]
        context['devices'] = Thing.objects.filter(pk__in=device_id_list)

        location_id_list = request.POST.get('locations', '').split(',')
        location_id_list = [ int(x) for x in filter(None, location_id_list) ]
        context['locations'] = Location.objects.filter(pk__in=location_id_list)

        event_id_list = request.POST.get('events', '').split(',')
        event_id_list = [ int(x) for x in filter(None, event_id_list) ]
        context['events'] = Event.objects.filter(pk__in=event_id_list)

        return self.render_to_response(context)


class EventCreateStepView(TemplateView):
    template_name = 'site/event-create-step.html'


class StoreView(TemplateView):
    template_name = 'site/store.html'


class SettingsView(TemplateView):
    template_name = 'site/settings.html'


class AddUserView(TemplateView):
    template_name = 'site/add-user.html'


class DeviceListView(TemplateView):
    template_name = 'site/device-list.html'

    def get_context_data(self, **kwargs):
        context = super(DeviceListView, self).get_context_data(**kwargs)
        context['devices'] = []
        for device in Thing.objects.filter(user=self.request.user, is_service=False):
            try:
                device.location = LocationThingCrossRef.objects.get(thing=device)
            except:
                device.location = None
            context['devices'].append(device)
        return context


class DeviceDetailView(TemplateView):
    template_name = 'site/device-detail.html'

    def get_context_data(self, **kwargs):
        context = super(DeviceDetailView, self).get_context_data(**kwargs)
        context['device'] = get_object_or_404(Thing, pk=kwargs.get('device_id'))
        return context


class DeviceActivityView(TemplateView):
    template_name = 'site/device-activity.html'

    def get_context_data(self, **kwargs):
        context = super(DeviceActivityView, self).get_context_data(**kwargs)
        context['device'] = get_object_or_404(Thing, pk=kwargs.get('device_id'))
        context['page'] = self.kwargs.get('page', None)
        return context


class WidgetDetailView(TemplateView):
    template_name = 'site/widget-detail.html'


class TimeDetailView(TemplateView):
    template_name = 'site/time-detail.html'

    def get_context_data(self, **kwargs):
        context = super(TimeDetailView, self).get_context_data(**kwargs)

        # Get the users device locations
        context['device_locaitions'] = LocationThingCrossRef.objects.filter(thing__in=Thing.objects.filter(user=self.request.user)).distinct('location')

        return context


class TimeFilterView(TemplateView):
    template_name = 'site/time-filter.html'

    def get_context_data(self, **kwargs):
        context = super(TimeFilterView, self).get_context_data(**kwargs)

        context['hours'] = xrange(1, 13)
        context['days'] = xrange(1, 32)
        context['months'] = [date(2014, month, 1) for month in xrange(1, 13)]
        context['years'] = xrange(date.today().year, 1900, -1)

        context['start_date'] = datetime.now()
        context['end_date'] = datetime.now()

        context['current_time'] = datetime.now().strftime('%s')
        context['hour_ago'] = (datetime.now() - timedelta(hours = 1)).strftime('%s')
        context['day_start'] = date.today().strftime('%s')
        context['week_ago'] = (datetime.now() - timedelta(weeks = 1)).strftime('%s')
        context['month_ago'] = (datetime.now() - timedelta(weeks = 4)).strftime('%s')
        context['6_months_ago'] = (datetime.now() - timedelta(weeks = 24)).strftime('%s')
        context['year_ago'] = (datetime.now() - timedelta(weeks = 52)).strftime('%s')

        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        start_date = datetime.strptime("{}-{}-{} {}:{}:00{}".format(
            request.POST.get('start_date_year'),
            request.POST.get('start_date_month'),
            request.POST.get('start_date_day'),
            request.POST.get('start_time_hour'),
            request.POST.get('start_time_minute'),
            request.POST.get('start_time_suffix')
        ), "%Y-%m-%d %I:%M:%S%p")

        end_date = datetime.strptime("{}-{}-{} {}:{}:00{}".format(
            request.POST.get('end_date_year'),
            request.POST.get('end_date_month'),
            request.POST.get('end_date_day'),
            request.POST.get('end_time_hour'),
            request.POST.get('end_time_minute'),
            request.POST.get('end_time_suffix')
        ), "%Y-%m-%d %I:%M:%S%p")

        context['start_date'] = start_date
        context['end_date'] = end_date

        if start_date >= end_date:
            return self.render_to_response(context)
        else:
            return redirect('/time/{}/{}/'.format(
                start_date.strftime('%s'),
                end_date.strftime('%s')
            ))


class TimeFilterResultsView(TemplateView):
    template_name = 'site/time-filter-results.html'

    def get_context_data(self, **kwargs):
        context = super(TimeFilterResultsView, self).get_context_data(**kwargs)

        context['start_stamp'] = self.kwargs.get('start_time')
        context['end_stamp'] = self.kwargs.get('end_time')

        context['start_date'] = datetime.utcfromtimestamp(float(self.kwargs.get('start_time')))
        context['end_date'] = datetime.utcfromtimestamp(float(self.kwargs.get('end_time')))
        context['page'] = self.kwargs.get('page', None)

        return context