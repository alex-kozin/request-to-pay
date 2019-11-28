from rest_framework import serializers
from userapi.serializers import UserSerializer
from .models import Item, Order, Invoice


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ("id", "name", "price")

class OrderSerializer(serializers.ModelSerializer):
    item = ItemSerializer()

    class Meta:
        model = Order
        fields = ("id", "item", "quantity", "price")


class InvoiceSerializer(serializers.ModelSerializer):
    customer = UserSerializer(read_only=True)
    driver = UserSerializer(read_only=True)

    class Meta:
        model = Invoice
        fields = ("id", "price", "status", "customer", "driver", "orders")
        depth = 2


# class NotifySerializer(serializers.Serializer):
#
#     email_subject = serializers.CharField(max_length=120, allow_blank=False)
#     email_message = serializers.CharField(allow_blank=False)
