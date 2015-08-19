from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from django.core.cache import cache
from myapp.models import Person


@receiver(post_delete, sender=Person)
def post_delete_actions(sender, instance, **kwargs):
    cache.delete(sender.cache_key.format(instance.email))
    print instance.email, "Object is deleted"


@receiver(post_save, sender=Person)
def post_save_actions(sender, instance, **kwargs):
    print instance.email, "Object is saved"
    cache.delete(sender.cache_key.format(instance.email))
