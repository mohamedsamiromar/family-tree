from django.db.models import signals
from django.dispatch import receiver
from family.models import  Person
from notification.models import Notification
import json


@receiver(signals.post_save, sender=Person)
def person_email(sender, instance, created, **kwargs):
    if created: 
        notification = Notification(
            type='Email',
            template='family/email/welcome.html',
            title='Welcom To Family Tree',
            data=json.dumps({
                "name": '{} {}'.format(instance.user.first_name, instance.user.last_name),
                "FAMILY_TREE_EMAIL": 'familytree@mail.com',
                "corporate_name": instance.name
                }),
            receiver_email=instance.user.email
        )
        notification.save()