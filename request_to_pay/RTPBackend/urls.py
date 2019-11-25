from django.urls import path
from . import api_views
from . import views

urlpatterns = [
    path('items/', api_views.ItemList.as_view()),
    path('items/new', api_views.ItemCreate.as_view()),
    path('items/<int:id>/', api_views.ItemRetrieveUpdateDestroy.as_view()),

    path('orders/', api_views.OrderList.as_view()),
    path('orders/new', api_views.OrderCreate.as_view()),
    path('orders/<int:id>/', api_views.OrderRetrieveUpdateDestroy.as_view()),

    path('invoices/', api_views.InvoiceList.as_view()),
    path('invoices/new', api_views.InvoiceCreate.as_view()),
    path('invoices/<int:id>/', api_views.InvoiceRetrieveUpdateDestroy.as_view()),
    path('pay/', views.DriverNotificationView.as_view()),
]
