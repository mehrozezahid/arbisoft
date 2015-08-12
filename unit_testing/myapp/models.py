from django.db import models


class Person(models.Model):

    first_name = models.TextField(max_length=50)
    last_name = models.TextField(max_length=50)

    def __unicode__(self):
        return "{name}".format(name=self.first_name+self.last_name)
