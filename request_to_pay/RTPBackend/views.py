from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.mail import send_mail
from request_to_pay.RTPBackend.models import Invoice

class DriverNotificationView(APIView):

    def post(self, request):
        invoice_id = request.data.get("invoice_id")
        invoice_object = Invoice.objects.get(pk=invoice_id)
        send_mail("UPDATE ON INVOICE",
            'The invoice has been paid.',
            'scotia_app@interac.com',
            [invoice_object.driver.email],
            fail_silently=False,)

