# Core imports
from django.conf.urls import patterns, url

# Local imports
import views

urlpatterns = patterns('',
    url(r'^$', views.WelcomeView.as_view(), name='welcome'),
    url(r'^my-profile/$', views.MyProfileView.as_view(), name='my-profile'),
    url(r'^locations/$', views.LocationListView.as_view(), name='locations'),
	url(r'^locations/map/$', views.LocationMapView.as_view(), name='locations_map'),
    url(r'^locations/detail/(?P<location_id>\d+)/$', views.LocationDetailView.as_view(), name='location'),
    url(r'^locations/activity/(?P<location_id>\d+)/$', views.LocationActivityView.as_view(), name='location_activity'),
    url(r'^locations/activity/(?P<location_id>\d+)/(?P<page>\d+)/$', views.LocationActivityView.as_view(), name='location_activity'),
    url(r'^data/$', views.DataView.as_view(), name='data'),
    url(r'^connected/$', views.ConnectedHatsView.as_view(), name='connected'),
    url(r'^time/$', views.TimeView.as_view(), name='times'),
    url(r'^time/detail$', views.TimeDetailView.as_view(), name='time'),
    url(r'^time/filter$', views.TimeFilterView.as_view(), name='time_filter'),
    url(r'^time/(?P<start_time>\d+)/(?P<end_time>\d+)/$', views.TimeFilterResultsView.as_view(), name='time_filter_results'),
    url(r'^time/(?P<start_time>\d+)/(?P<end_time>\d+)/(?P<page>\d+)/$', views.TimeFilterResultsView.as_view(), name='time_filter_results'),
    url(r'^events/$', views.EventListView.as_view(), name='events'),
    url(r'^events/(?P<page>\d+)/$', views.EventListView.as_view(), name='events'),
    url(r'^events/detail/(?P<event_id>\d+)/$', views.EventDetailView.as_view(), name='event'),
    url(r'^events/create$', views.EventCreateView.as_view(), name='create'),
    url(r'^events/summary$', views.EventSummary.as_view(), name='summary'),
    url(r'^events/create/step$', views.EventCreateStepView.as_view(), name='step'),
    url(r'^store/$', views.StoreView.as_view(), name='store'),
    url(r'^settings/$', views.SettingsView.as_view(), name='settings'),
    url(r'^settings/add-user$', views.AddUserView.as_view(), name='add-user'),
    url(r'^devices/$', views.DeviceListView.as_view(), name='devices'),
    url(r'^devices/(?P<device_id>\d+)/detail/$', views.DeviceDetailView.as_view(), name='device'),
    url(r'^devices/(?P<device_id>\d+)/activity/$', views.DeviceActivityView.as_view(), name='activity'),
    url(r'^devices/(?P<device_id>\d+)/activity/(?P<page>\d+)/$', views.DeviceActivityView.as_view(), name='activity'),
    url(r'^widgets/detail$', views.WidgetDetailView.as_view(), name='widget'),
)
