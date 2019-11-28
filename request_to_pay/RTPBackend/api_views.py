from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ValidationError
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from time import sleep
from userapi.notifications import EmailNotifications as email
from .serializers import ItemSerializer, OrderSerializer, InvoiceSerializer
from .models import Item, Order, Invoice


class ItemList(ListAPIView):
    """View all items available for purchase"""
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_backends = (DjangoFilterBackend, )
    filter_fields = ('id', )


class ItemCreate(CreateAPIView):
    """Create a new item"""
    serializer_class = ItemSerializer

    def create(self, request, *args, **kwargs):
        """Check if price > 0"""
        try:
            price = request.data.get("price")
            if price is not None and float(price) <= 0.0:
                raise ValidationError({"price": "Must be above $0.0"})
        except:
            raise ValidationError({"price": "A valid number is required"})
        return super().create(request, *args, **kwargs)


class ItemRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    """Read and update, or delete an item based on id"""
    queryset = Item.objects.all()
    lookup_field = "id"
    serializer_class = ItemSerializer


class OrderList(ListAPIView):
    """View all orders made"""
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = (DjangoFilterBackend, )
    filter_fields = ('id', )


class OrderCreate(CreateAPIView):
    """Make a new order"""
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        """Check if quantity requested is greater than 0"""
        try:
            quantity = request.data.get("quantity")
            if quantity is not None and int(quantity) <= 0:
                raise ValidationError({"quantity": "Must be above 0"})
        except:
            raise ValidationError({"quantity": "A valid integer is required"})
        return super().create(request, *args, **kwargs)


class OrderRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    """Read and update, or delete an order based on id"""
    queryset = Order.objects.all()
    lookup_field = "id"
    serializer_class = OrderSerializer


class InvoiceList(ListAPIView):
    """View all invoices created"""
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    filter_backends = (DjangoFilterBackend, )
    filterset_fields = ('id', 'driver', 'customer', 'status')


class InvoiceCreate(CreateAPIView):
    """Create a new invoice"""
    serializer_class = InvoiceSerializer

    def create(self, request, *args, **kwargs):
        """Check if users have correct roles"""
        self._validate_user(request, "driver", "D")
        self._validate_user(request, "customer", "C")

        return super().create(request, *args, **kwargs)

    @staticmethod
    def _validate_user(request, user_role: str, user_type: str):
        """Check if user_type from request data fits the user_role"""
        try:
            user = request.data.get("user")
            if user is not None and getattr(user, "user_type") != user_type:
                raise ValidationError({user_role: f"Must be a {user_role} user"})
        except:
            raise ValidationError({user_role: "A valid driver is required"})


class InvoiceRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    """Read and update, or delete an invoice based on id"""
    queryset = Invoice.objects.all()
    lookup_field = "id"
    serializer_class = InvoiceSerializer


class InvoicePayView(APIView):

    def post(self, request, invoice_id):
        # Mocking the external Payment API
        # WARNING: replace this with actual Interac API call in production!
        sleep(1)

        # Update invoice to 'PAID'
        invoice = Invoice.objects.get(pk=invoice_id)

        # The invoice can't be delivered without being 'ACTIVE'
        if invoice.status != 'A':
            return Response(
                {invoice.status: "Invoice status must be 'A' (active)"},
                status=status.HTTP_406_NOT_ACCEPTABLE)

        invoice.status = 'P'
        invoice.save()

        # Notify the driver
        email.notify(receiver = invoice.driver,
                     subject = f"Invoice #{invoice.id} was paid",
                     message = f"Invoice #{invoice.id} was paid."
                               f" Please unload the goods at {invoice.customer.address}.")

        return Response(status=status.HTTP_200_OK)


class InvoiceDeliverView(APIView):

    def post(self, request, invoice_id):
        # Update invoice to 'DELIVERED'
        invoice = Invoice.objects.get(pk=invoice_id)

        # The invoice can't be delivered without being 'PAID'
        if invoice.status != 'P':
            return Response({invoice.status: "Invoice status must be 'P' (paid)"},
                            status=status.HTTP_402_PAYMENT_REQUIRED)

        invoice.status = 'D'
        invoice.save()

        # Notify the customer
        email.notify(receiver = invoice.customer,
                     subject = f"Items in the invoice #{invoice.id} have shipped",
                     message = f"Items in the invoice #{invoice.id} have shipped. Have a nice day!")

        return Response(status=status.HTTP_200_OK)
