"""
Production settings for HAT project.

For an explanation of these settings, please see the Django documentation at:

<http://docs.djangoproject.com/en/dev/>

While many of these settings assume sensible defaults, you must provide values
for the site, database, media and email sections below.
"""

import os


# The name of this site.  Used for branding in the online admin area.
from django.core.urlresolvers import reverse_lazy

SITE_NAME = "HAT"

SITE_DOMAIN = "hat.onespace.media"

SERVER_IP = "178.62.49.164"

PREPEND_WWW = False

DEBUG = True

ALLOWED_HOSTS = ['*']

SUIT_CONFIG = {
    'ADMIN_NAME': SITE_NAME
}

# Database settings.

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "hat",
        "USER": "hat",
        "PASSWORD": "bn2qrb62To",
        "HOST": "",
        "PORT": ""
    }
}

# Absolute path to the directory where all uploaded media files are stored.

MEDIA_ROOT = "/var/www/hat_media"

MEDIA_URL = "/media/"

FILE_UPLOAD_PERMISSIONS = 0644


# Absolute path to the directory where static files will be collected.

STATIC_ROOT = "/var/www/hat_static"

STATIC_URL = "/static/"


# Email settings.

EMAIL_HOST = "smtp.mandrillapp.com"

EMAIL_HOST_USER = "developers@onespacemedia.com"

EMAIL_HOST_PASSWORD = "LtR0Hwa7hMer0SVqoaKncg"

EMAIL_PORT = 587

EMAIL_USE_TLS = True

SERVER_EMAIL = u"{name} <notifications@{domain}>".format(
    name = SITE_NAME,
    domain = SITE_DOMAIN,
)

DEFAULT_FROM_EMAIL = SERVER_EMAIL

EMAIL_SUBJECT_PREFIX = "[%s] " % SITE_NAME


# Error reporting settings.  Use these to set up automatic error notifications.

ADMINS = (
    ("Onespacemedia Errors", "errors@onespacemedia.com"),
)

MANAGERS = ()

SEND_BROKEN_LINK_EMAILS = False


# Locale settings.

TIME_ZONE = "Europe/London"

LANGUAGE_CODE = "en-gb"

USE_I18N = False

USE_L10N = True

USE_TZ = True


# Auto-discovery of project location.

SITE_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


# A list of additional installed applications.

INSTALLED_APPS = (
    "django.contrib.sessions",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "suit",
    "django.contrib.admin",
    "django.contrib.sitemaps",
    "south",
    "django_extensions",
    "markdown_deux",
    "optimizations",
    "pure_pagination",
    

    "hat.apps.events",
    "hat.apps.locations",
    "hat.apps.system",
    "hat.apps.things",
    "hat.apps.users",
    "hat.apps.organisations",
    "hat.apps.site",
    "hat.apps.api",
    "gcharts",
)

GOOGLECHARTS_API = '1.1'
GOOGLECHARTS_PACKAGES = ["corechart", "gauge", "geochart", "table", "treemap"]

# Additional static file locations.

STATICFILES_DIRS = (
    os.path.join(SITE_ROOT, "static"),
)

STATIC_ASSETS = {
    "default": {
        "js": {
            "include": (
                "js/vendor/jquery.js",
                "js/vendor/jquery.pjax.js",
                "js/vendor/perspective-nav/modernizr.js",
                "js/vendor/perspective-nav/classie.js",
                "js/vendor/perspective-nav/menu.js",

                "js/foundation/foundation.js",
                "js/foundation/foundation.equalizer.js",

                "js/vendor/nprogress.js",
            ),
        },
        "css": {
            "include": (
                "css/*.css",
            ),
            "exclude": (
                "css/screen.content.css",
            ),
        },
    },
}


# Dispatch settings.

MIDDLEWARE_CLASSES = (
    "django.middleware.transaction.TransactionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "hat.middleware.LoginRequiredMiddleware",
)

ROOT_URLCONF = "hat.urls"

WSGI_APPLICATION = "hat.wsgi.application"

PUBLICATION_MIDDLEWARE_EXCLUDE_URLS = (
    "^admin/.*",
)

SESSION_ENGINE = "django.contrib.sessions.backends.signed_cookies"
# SESSION_COOKIE_NAME = "cookie_DP0_2"
# CSRF_COOKIE_NAME = "cookie_DP0_2"
# CSRF_COOKIE_DOMAIN = "hubofallthings.net"
MESSAGE_STORAGE = "django.contrib.messages.storage.cookie.CookieStorage"

SITE_ID = 1


# Absolute path to the directory where templates are stored.

TEMPLATE_DIRS = (
    os.path.join(SITE_ROOT, "templates"),
)

TEMPLATE_LOADERS = (
    ("django.template.loaders.cached.Loader", (
        "django.template.loaders.filesystem.Loader",
        "django.template.loaders.app_directories.Loader",
    )),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",
    "hat.context_processors.pjax",
)

# Namespace for cache keys, if using a process-shared cache.

CACHE_MIDDLEWARE_KEY_PREFIX = "hat"

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
    },
    # Used for efficient caching of static assets.
    "optimizations": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "TIMEOUT": 60 * 60 * 24,
        "LOCATION": "optimizations",
    },
}


# A secret key used for cryptographic algorithms.

SECRET_KEY = "exx)j3)rk3ctdv&=74b*2zzm+q+s$is)w9591u=r2zfd%%r(%t"


# TinyMCE settings.

RICHTEXT_SETTINGS = {
    "default": {
        "theme": "advanced",
        "plugins": "table, advimage, inlinepopups, paste",
        "paste_auto_cleanup_on_paste": True,
        "paste_remove_spans": True,
        "paste_remove_styles": True,
        "theme_advanced_buttons1": "code,|,formatselect,styleselect,|,bullist,numlist,table,hr,|,bold,italic,|,link,unlink,image",
        "theme_advanced_buttons2": "",
        "theme_advanced_buttons3": "",
        "theme_advanced_resizing": True,
        "theme_advanced_path": False,
        "theme_advanced_statusbar_location": "bottom",
        "width": "700px",
        "height": "350px",
        "dialog_type": "modal",
        "theme_advanced_blockformats": "h1,h2,h3,p,blockquote",
        "content_css": "css/screen.content.css",
        "extended_valid_elements": "iframe[scrolling|frameborder|class|id|src|width|height|name|align],article[id|class],section[id|class]",
        "convert_urls": False,
        "accessibility_warnings": False,
    }
}


# Logging configuration.

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse"
        }
    },
    "handlers": {
        "mail_admins": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler"
        }
    },
    "loggers": {
        "django.request": {
            "handlers": ["mail_admins"],
            "level": "ERROR",
            "propagate": True,
        },
    }
}

LOGIN_URL = reverse_lazy('login')
LOGIN_REDIRECT_URL = reverse_lazy('site:welcome')

LOGIN_WHITELIST = [
    reverse_lazy('login'),
    reverse_lazy('logout'),
    '/api/v1/',
    '/accounts',
    # reverse_lazy('application:register'),
    # reverse_lazy('application:register_success'),
    # reverse_lazy('admin:index'),
    # '/register/confirm/',
    # '/password-reset/',
    # '/password-reset-done/',
    # '/reset-password/',
    # '/reset/done/',
]

# Set your DSN value
RAVEN_CONFIG = {
    'dsn': 'https://b525f6988d774051b7ac9d3b3bfc1d2c:e2fb250d53344eaebe7dc150aad2d9fb@app.getsentry.com/30400',
}

# Add raven to the list of installed apps
INSTALLED_APPS = INSTALLED_APPS + (
    # ...
    'raven.contrib.django.raven_compat',
)

PAGINATION_SETTINGS = {
    'PAGE_RANGE_DISPLAYED': 4,
    'MARGIN_PAGES_DISPLAYED': 2,
}
