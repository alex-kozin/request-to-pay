from django.urls import path
from . import api_views

urlpatterns = [
    path('items/', api_views.ItemList.as_view()),
    path('items/new', api_views.ItemCreate.as_view()),
]
