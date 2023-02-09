from django.db.models import signals
from django.dispatch import receiver
from family.models import  Person


@receiver(signals.post_save, sender=Person)
def person_email(sender, instance, created, **kwargs):
    pass