from rest_framework import serializers

from .models import Item, Order


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ("id", "name", "price")


class OrderSerializer(serializers.ModelSerializer):
    item = ItemSerializer()

    class Meta:
        model = Order
        fields = ("id", "invoice", "item", "quantity", "price")
