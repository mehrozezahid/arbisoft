from django.db import models
from django.core.cache import cache
from django.core.exceptions import ObjectDoesNotExist


class Person(models.Model):

    first_name = models.TextField(max_length=50)
    last_name = models.TextField(max_length=50)
    email = models.EmailField(unique=True)

    cache_key = u'person_{}'

    def __unicode__(self):
        return u"{fname} {lname}".format(fname=self.first_name, lname=self.last_name)

    # def save(self, *args, **kwargs):
    #     """Overridden save function"""
    #
    #     super(Person, self).save(*args, **kwargs)
    #     cache.clear()
    #     print("Object is saved")
    #
    # def delete(self, *args, **kwargs):
    #     """Overridden delete function"""
    #
    #     cache.delete(self.cache_key.format(self.email))
    #     super(Person, self).delete(*args, **kwargs)

    @classmethod
    def get_person(cls, email):
        cache_key = cls.cache_key.format(email)
        val = cache.get(cache_key)

        if val is None:
            try:
                obj = Person.objects.get(email=email)
                cache.set(cache_key, obj)
                return obj

            except ObjectDoesNotExist:
                return None

        return val
