from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
import hashlib


class AuthBackend(object):

    @staticmethod
    def authenticate(email, password):
        print("Inside custom authenticate function with the user id being {username}".format(username=email))
        try:
            user = User.objects.get(email=email)
            print("Inside try")
            sha = hashlib.sha256(password)
            print(user.password)
            print(sha)
            if user.check_password(password):
                print("Returning user")
                return user

        except ObjectDoesNotExist:
            print("Returning None")
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except ObjectDoesNotExist:
            return None
