from django.urls import path
from . import api_views

urlpatterns = [
    path('users/', api_views.UserProfileList.as_view()),
    path('users/<int:id>/', api_views.UserProfileRetrieveUpdate.as_view()),
]
