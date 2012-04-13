from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User

class LemonLDAPBackend(ModelBackend):
    """
    This backend is to be used in conjunction with the ``LemonLDAPMiddleware``
    found in the middleware module of this package, and is used when the server
    is handling authentication outside of Django.

    By default, the ``authenticate`` method creates ``User`` objects for
    usernames that don't already exist in the database. Subclasses can disable
    this behavior by setting the ``create_unknown_user`` attribute to ``False``.
    """

    # Create a User object if not already in the database?
    create_unknown_user = True

    def authenticate(self, remote_userinfo):
        """
            The user informations passed as ``remote_userinfo`` dictionnary is considered
            as trusted. This method simply returns the ``User`` object with the given
            informations, creating a nez ``User`` object if ``create_unknown_user`` is ``True``.

            Returns None if ``create_unknown_user`` is ``False`` and a ``User`` object with
            the given informations is not found in the database.
        """
        if remote_userinfo is None:
            return

        user = None
        username = self.clean_username(remote_userinfo["username"])

        user, created = User.objects.get_or_create(username=username)
        user = self.configure_user(user, remote_userinfo)

        return user

    def clean_username(self, username):
        return username

    def configure_user(self, user, remote_userinfo):
        user.email = remote_userinfo["mail"]
        user.first_name = remote_userinfo["name"].split(' ')[0]
        user.last_name  = remote_userinfo["name"].split(' ')[1]
        return user
