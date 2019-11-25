from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from django.core.mail import send_mail
from request_to_pay.RTPBackend.models import Invoice
from time import sleep

class DriverNotificationView(APIView):

    def post(self, request):
        sleep(1)
        invoice_id = request.data.get("invoice_id")
        invoice_object = Invoice.objects.get(pk=invoice_id)
        send_mail("UPDATE ON INVOICE",
            'The invoice has been paid.',
            'scotia_app@interac.com',
            [invoice_object.driver.email, "supplier@interac.com"],
            fail_silently=False,)

class CustomerNotificationVIew(APIView):
    def post(self, request):
        invoice_id = request.data.get("invoice_id")
        invoice_object = Invoice.objects.get(pk=invoice_id)
        send_mail("UPDATE ON ORDER",
                  'The order has been delivered.',
                  'scotia_app@interac.com',
                  [invoice_object.customer.email],
                  fail_silently=False, )