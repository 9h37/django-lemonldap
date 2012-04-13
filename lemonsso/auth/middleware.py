from django.contrib.auth.models import User
from django.contrib import auth
from django.core.exceptions import ImproperlyConfigured

class LemonLDAPMiddleware(object):
    """
    Middleware for utilizing LemonLDAP::NG SSO provided authentication.

    If request.user is not authenticated, then this middleware attempts to
    authenticate the username passed in the ``HTTP_AUTH_USER`` request header.
    If authentication is successful, the user is automatically logged in to
    persist the user in the session.

    The headers ``HTTP_AUTH_MAIL`` and ``HTTP_AUTH_REALNAME`` are getted
    to pass informations about the user to the authentication backend.

    You can subclass the middleware and change ``header_username``,
    ``header_mail`` and ``header_realname`` if you need to use a different header.
    """

    header_username = "HTTP_AUTH_USER"
    header_mail     = "HTTP_AUTH_MAIL"
    header_realname = "HTTP_AUTH_NAME"

    def process_request(self, request):
        # AuthenticationMiddleware is required so that request.user exists.
        if not hasattr(request, 'user'):
            raise ImproperlyConfigured(
                    "The Django LemonLDAP auth middleware requires the"
                    " authentication middleware to be installed. Edit your"
                    " MIDDLEWARE_CLASSES setting to insert"
                    " 'django.contrib.auth.middleware.AuthenticationMiddleware'"
                    " before the LemonLDAPMiddleware class.")

        try:
            userinfo = {
                'username': request.META[self.header_username],
                'mail':     request.META[self.header_mail],
                'name':     request.META[self.header_realname]
            }
        except KeyError:
            # If specified header doesn't exist then return (leaving
            # request.user set to AnonymousUser by the AuthenticationMiddleware).
            return

        # If the user is already autheniticated and that user is the user we are
        # getting passed in the headers, then the correct user is already persisted
        # in the session and we don't need to continue.
        if request.user.is_authenticated():
            if request.user.username == self.clean_username(userinfo['username'], request):
                return

        # We are seeing this user for the first time in this session, attempt
        # to authenticate the user.
        user = auth.authenticate(remote_userinfo=userinfo)

        if user:
            # User is valid. Set request.user and persist user in the session
            # by logging the user in
            request.user = user
            auth.login(request, user)

    def clean_username(self, username, request):
        """
        Allows the backend to clean the username, if the backend defines a
        clean_username method.
        """

        backend_str = request.session[auth.BACKEND_SESSION_KEY]
        backend = auth.load_backend(backend_str)

        try:
            username = backend.clean_username(username)
        except AttributeError: # Backend has no clean_username method.
            pass

        return username
