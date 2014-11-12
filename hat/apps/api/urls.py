from django.conf.urls import patterns, url, include
from views import ApiDocumentation, SensorsView, SensorDataView, BatchSensorDataView, CreateEventView, CreateLocationView, CreatePersonView

urlpatterns = patterns('',
    url(r'^$', ApiDocumentation.as_view()),
    url(r'^sensors/$', SensorsView.as_view()),
    url(r'^sensor_data/$', SensorDataView.as_view()),
    url(r'^batch_sensor_data/$', BatchSensorDataView.as_view()),
    url(r'^create_event/$', CreateEventView.as_view()),
    url(r'^create_location/$', CreateLocationView.as_view()),
    url(r'^create_person/$', CreatePersonView.as_view()),
)
