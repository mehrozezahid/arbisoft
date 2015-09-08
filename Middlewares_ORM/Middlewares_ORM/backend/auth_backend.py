from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
import logging


logger2 = logging.getLogger(__name__)


class AuthBackend(object):

    def authenticate(self, username=None, email=None, password=None):

        if email:
            user_value = email
            logger2.debug("Logging in using email")
        elif username:
            user_value = username
            logger2.debug("Logging in using email")

        try:
            user = User.objects.get(email=user_value)
            if user.check_password(password):
                logger2.info("Successful login")
                return user

        except ObjectDoesNotExist, e:
            logger2.exception(e)
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except ObjectDoesNotExist, e:
            logger2.exception(e)
            return None
