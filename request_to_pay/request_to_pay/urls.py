"""request_to_pay URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Request-To-Pay API')

# admin - built-in admin panel support
# userapi - module responsible for handling user creation, authentication, etc.
# api - module responsible for logic related to invoicing, ordering and payments

urlpatterns = [
    path('admin/', admin.site.urls),
    path('userapi/', include('userapi.urls')),
    path('api/', include('RTPBackend.urls')),
    path('docs/', schema_view),
    path('accounts/', include('rest_registration.api.urls')),
]
