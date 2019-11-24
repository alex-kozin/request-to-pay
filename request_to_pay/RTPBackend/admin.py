from django.contrib import admin
from . import models
from userapi import models as user_models
# Register your models here.

admin.site.register(user_models.User)
admin.site.register(user_models.UserProfile)
