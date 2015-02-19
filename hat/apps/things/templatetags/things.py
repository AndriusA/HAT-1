from django import template, db
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from ..models import Thing, Sensor, SensorData
from ...events.models import Event, EventSensorDataCrossRef

register = template.Library()

from datetime import datetime, timedelta

@register.filter()
def fix_value(value):
    parsed_value = eval(value)

    if isinstance(parsed_value, list):
        value = parsed_value[0]

    return value


@register.inclusion_tag('site/includes/data_stream.html', takes_context=True)
def data_stream(context, device=None, location=None, limit=None, start_date=None, end_date=None, event=None, page=None, base_url=""):

    if not event:

        # Use the provided device if provided, otherwise use users devices
        if device:
            if isinstance(device, db.models.query.QuerySet):
                devices = Thing.objects.filter(pk__in=[d.pk for d in device])
            else:
                devices = Thing.objects.filter(pk=device.pk)
        else:
            devices = Thing.objects.filter(user=context['request'].user)

        if location:
            devices = devices.filter(locationthingcrossref__location=location)

        # Get the sensor data using the devices
        sensor_data = SensorData.objects.filter(sensor__in=Sensor.objects.filter(thingsensorcrossref__thing__in=devices))

        if start_date and end_date:
            sensor_data = sensor_data.filter(date_created__range=(start_date, end_date))

    else:
        event_data = EventSensorDataCrossRef.objects.filter(event=event)
        sensor_data = [event.sensor_data for event in event_data]


    if page:
        page = int(page)
    else:
        page = 1

    if limit:
        paginate = False
        sensor_data = sensor_data[:limit]
        paginator = Paginator(sensor_data, 500)
    else:
        paginate = True
        paginator = Paginator(sensor_data, 20)

    try:
        sensor_data = paginator.page(page)
    except PageNotAnInteger:
        sensor_data = paginator.page(1)
    except EmptyPage:
        sensor_data = paginator.page(paginator.num_pages)


    return {
        'sensor_data': sensor_data,
        'paginate': paginate,
        'base_url': base_url
    }


@register.inclusion_tag('site/includes/stream_graph.html', takes_context=True)
def stream_graph(context, location=None, device=None, days=1):

    query_days = context['request'].GET.get('days', None)

    if query_days:
        days = int(query_days)

    # Create list of last 24 hours
    current_time = datetime.now()
    last_24_hours = [datetime.strptime("{}-{}-{} {}:00:00".format(
        current_time.year,
        current_time.month,
        current_time.day,
        current_time.hour,
    ), "%Y-%m-%d %H:%M:%S") - timedelta(hours=i) for i in range(24*days)]

    # Get the data from the current location
    devices = []
    if location:
        devices = Thing.objects.filter(locationthingcrossref__location=location)
    if device:
        devices = [device]

    sensor_data = SensorData.objects.filter(
        sensor__in=Sensor.objects.filter(thingsensorcrossref__thing__in=devices),
    )

    temperature_values = []
    illuminance_values = []

    # Get temperature for the dates we have
    for date in last_24_hours:
        value = sensor_data.filter(type=11, date_created__lte=date).order_by('-date_created')[:1]
        if value:
            value = value[0]
        temperature_values.append(value)

    # Get illuminance for the dates we have
    for date in last_24_hours:
        value = sensor_data.filter(type=12, date_created__lte=date).order_by('-date_created')[:1]
        if value:
            value = value[0]
        illuminance_values.append(value)

    return {
        'current_time': current_time,
        'last_24_hours': last_24_hours,
        'temperature_values': temperature_values,
        'illuminance_values': illuminance_values,
        'location': location,
        'device': device,
        'days': days
    }


