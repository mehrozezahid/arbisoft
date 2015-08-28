from datetime import datetime
from django.db import models
from django.contrib.auth.admin import User
from Image_Handling import settings


def content_file_name(instance, filename):
    var = '{folder}{user}/{file}'.format(folder=settings.MEDIA_URL,
                                         user=instance.user.username, file=datetime.today().strftime('%d-%m-%Y'))
    var = var[1:]
    return var


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    picture = models.ImageField(upload_to=content_file_name)

    def __unicode__(self):
        return self.user.username
