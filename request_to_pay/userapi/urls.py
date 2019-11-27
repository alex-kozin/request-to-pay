from django.urls import path
from rest_framework.authtoken import views as drf_views
from . import views
from . import api_views

urlpatterns = [
    path('users/', api_views.UserList.as_view()),
    path('users/<int:id>/', api_views.UserRetrieveUpdate.as_view()),
]
