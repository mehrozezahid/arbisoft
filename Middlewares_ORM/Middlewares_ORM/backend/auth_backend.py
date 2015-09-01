from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


class AuthBackend(object):

    def authenticate(self, email, password):
        print("Inside custom authenticate function with the user id being {username}".format(username=email))
        try:
            user = User.objects.get(email=email)
            if user.password == password:
                return user

        except ObjectDoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except ObjectDoesNotExist:
            return None
