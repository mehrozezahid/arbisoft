from django.db import models
from django.contrib.auth.admin import User


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    picture = models.TextField(max_length=50)

    def __unicode__(self):
        return self.user.username
