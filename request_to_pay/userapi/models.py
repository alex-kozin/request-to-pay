from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    """
    A User in the app with email as login

    Fields
    ----------
    email: EmailField
        the email and login of this user

    email_verified: BooleanField
        a flag whether this user verified their email

    user_type: CharField
        the type of user for this profile, can be:
        "S" - Supplier, "C" - Customer, "D" - Driver

    address: TextField
        the address of the customer

    === Representation Invariants ===
    -   email is not None
    -   user_type: "S" | "C" | "D"
    -   len(user_type) == 1
    -   if user_type == 'C' then address is not None
    """
    username = None
    email = models.EmailField(_('email address'), unique=True)
    email_verified = models.BooleanField(default=False)

    USER_CHOICES = [("S", "Supplier"), ("C", "Customer"), ("D", "Driver")]
    user_type = models.CharField(choices=USER_CHOICES, max_length=1)
    address = models.TextField(blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return "{}".format(self.email)
