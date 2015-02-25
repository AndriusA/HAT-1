# Core imports
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hat.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^', include('hat.apps.site.urls', namespace="site")),
    # Login handling
    url(
        r'login/',
        'django.contrib.auth.views.login',
        {'template_name': 'registration/login.html'},
        name='login',
    ),

    url(
        r'logout/',
        'django.contrib.auth.views.logout',
        {'next_page': 'login'},
        name='logout',
    ),


    url(
        r'^ui-kit/',
        TemplateView.as_view(template_name="ui-kit/ui-kit.html")
    ),
    url(
        r'^ui-kit-full/',
        TemplateView.as_view(template_name="ui-kit/ui-kit-full.html")
    ),

    url(r'^api/v1/', include('hat.apps.api.urls')),

    url(r'^graph/',include('hat.apps.things.urls')),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += patterns('django.contrib.auth.views',
    url(r'^accounts/password/reset/$',
        'password_reset',
        name='password_reset'),
    url(r'^accounts/password/reset/done/$',
        'password_reset_done',
        name='password_reset_done'),
    url(r'^accounts/password/reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$',
        'password_reset_confirm',
        name='password_reset_confirm'),
    url(r'^accounts/password/reset/complete/$',
        'password_reset_complete',
        name='password_reset_complete')
)
