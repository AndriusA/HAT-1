# Core imports
from django.conf.urls import patterns, url

# Local imports
import views

urlpatterns = patterns('',
    url(r'^$', views.graph),
)
