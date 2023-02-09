from django.db import models
import json
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from customuser.models import TimeStampedModel


class Notification(TimeStampedModel):
    type_notification = models.CharField(max_length=5, choices=(
        ('Email', 'Email'),
        ('SMS', 'SMS'),
        ('Push', 'Push'),
    ))
    receiver_email = models.EmailField(null=True, blank=True)
    receiver_mobile = models.CharField( max_length=10, blank=True, null=True)
    receivers_mobiles = models.TextField(null=True, blank=True)
    title = models.CharField(max_length=255)
    body = models.TextField(null=True, blank=True)
    data = models.TextField(null=True, blank=True)
    template = models.CharField(max_length=255, null=True, blank=True)
    result = models.TextField(null=True, blank=True)

    def send_email_notification(self):
        plaintext = get_template(self.template)
        html = get_template(self.template)
        subject = self.title
        data = json.loads(self.data)
        bcc = []

        if data.get('bcc'):
            bcc = data.get('bcc')

        msg = EmailMultiAlternatives(
            subject, plaintext.render(data),
            settings.DEFAULT_FROM_EMAIL,
            [self.receiver_email],
            bcc=bcc,
        )

        if data.get('contract'):
            contract_id = data.get('contract')
            pdf = self.print_contract_email(contract_id)
            msg.attach('munjiz-contract.pdf', pdf, 'application/pdf')

        msg.attach_alternative(html.render(data), "text/html")
        msg.send()

    def save(self, *args, **kwargs):
        if self.type == 'Email' :
            self.send_email_notification()
        super().save(*args, **kwargs)
