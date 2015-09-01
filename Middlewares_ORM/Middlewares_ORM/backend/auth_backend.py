from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
import hashlib


class AuthBackend(object):

    @staticmethod
    def authenticate(email, password):
        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                return user

        except ObjectDoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except ObjectDoesNotExist:
            return None
