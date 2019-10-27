from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


class User(AbstractUser):
    username = models.CharField(blank=True, null=True, max_length=50)
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return "{}".format(self.email)


class UserProfile(models.Model):
    USER_CHOICES = [("S", "Suppliers"), ("C", "Customer"), ("D", "Driver")]
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                related_name='profile')
    name = models.CharField( max_length=50, null=True)
    address = models.TextField(blank=True)
    user_type = models.CharField(choices=USER_CHOICES, max_length=1)
    status = models.BooleanField()
