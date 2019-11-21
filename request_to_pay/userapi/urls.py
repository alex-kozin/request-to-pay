from django.urls import path
<<<<<<< Updated upstream
from rest_framework.authtoken import views as drf_views
from . import views
from . import api_views

urlpatterns = [
    path('', views.ProfileView.as_view(), name='whoami'),
    path('hello/', views.HelloView.as_view(), name='hello'),
    path('auth/', drf_views.obtain_auth_token, name='auth'),

=======
from . import api_views, views

urlpatterns = [
    path('', views.whoami),
>>>>>>> Stashed changes
    path('users/', api_views.UserProfileList.as_view()),
    path('users/<int:id>/', api_views.UserProfileRetrieveUpdate.as_view()),
]
