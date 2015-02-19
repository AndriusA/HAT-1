from django.conf.urls import patterns, url, include
from views import ApiDocumentation, SensorsView, SensorDataView, BatchSensorDataView, CreateLocationView, CreatePersonView, CreateSensorView
from views import GetSensorDataView
from views import GetSensorDescriptionView
#, CreateRecipientView, CreateEventView,

urlpatterns = patterns('',
    url(r'^$', ApiDocumentation.as_view()),
    url(r'^sensors/$', SensorsView.as_view()),
    url(r'^sensor_data/$', SensorDataView.as_view()),
    url(r'^batch_sensor_data/$', BatchSensorDataView.as_view()),
    #url(r'^create_event/$', CreateEventView.as_view()),
    url(r'^create_location/$', CreateLocationView.as_view()),
    url(r'^create_person/$', CreatePersonView.as_view()),
    # url(r'^create_recipient/$', CreateRecipientView.as_view()),
    url(r'^get_sensor_description/$', GetSensorDescriptionView.as_view()),
    url(r'^get_sensor_data/$', GetSensorDataView.as_view()),
)
