from rest_framework import serializers
from userapi.serializers import UserProfileSerializer
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
    customer = UserProfileSerializer(read_only=True)
    driver = UserProfileSerializer(read_only=True)

    class Meta:
        model = Invoice
        fields = ("id", "price", "status", "customer", "driver", "orders")
        depth = 2
