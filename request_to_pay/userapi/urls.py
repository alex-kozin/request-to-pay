from . import views
from django.urls import path
from rest_framework.authtoken import views as drf_views

urlpatterns = [
    path('hello/', views.HelloView.as_view(), name='hello'),
    path('auth/', drf_views.obtain_auth_token, name='auth'),
]
