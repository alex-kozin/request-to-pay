from django.core.mail import send_mail
from django.conf import settings
from .models import User


class EmailNotifications():
    def notify(receiver: User, subject: str, message:str):
        send_mail(subject, message,
            settings.EMAIL_HOST_USER,
            [receiver.email],
            fail_silently=False,)
