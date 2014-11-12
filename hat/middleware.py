from django.conf import settings
from django.contrib.auth.views import redirect_to_login


class LoginRequiredMiddleware(object):

    def process_request(self, request):
        # If the user is already authenticated, don't do anything else.
        if request.user.is_authenticated():
            return None

        # Don't apply to the favicon.
        if request.path == '/favicon.ico':
            return None

        # We have a number of whitelisted URLs which the user is not required
        # to be authenticated to see.
        whitelist = getattr(settings, 'LOGIN_WHITELIST', [])

        if request.path not in whitelist:

            # We also want to be sure we're not redirecting static assets on the
            # development server.
            if settings.DEBUG and request.path.startswith(settings.MEDIA_URL):
                return None

            # Does the URL start with an allowed URL?
            for path in whitelist:
                if request.path.startswith(str(path)):
                    return None

            return redirect_to_login(request.path)
        return None
