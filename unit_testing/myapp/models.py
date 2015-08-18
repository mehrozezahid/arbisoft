from django.db import models
from django.core.cache import cache


class Person(models.Model):

    first_name = models.TextField(max_length=50)
    last_name = models.TextField(max_length=50)

    cache_key = u'person_{}'

    def __unicode__(self):
        return "{name}".format(name=self.first_name+self.last_name)

    def save(self, *args, **kwargs):
        super(Person, self).save(*args, **kwargs)
        print("Object is saved")

    def delete(self, *args, **kwargs):
        cache.delete(self.first_name)
        super(Person, self).delete(*args, **kwargs)

    @classmethod
    def get_person(self, fname):
        cache_key = self.cache_key.format(fname)
        val = cache.get(cache_key)

        if val is None:
            obj = Person.objects.get(first_name=fname)
            cache.set(cache_key, obj)
            return obj

        return val
