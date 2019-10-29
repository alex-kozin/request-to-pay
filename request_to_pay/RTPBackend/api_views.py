from rest_framework.generics import ValidationError
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import ItemSerializer, OrderSerializer
from .models import Item, Order


class ItemList(ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_backends = (DjangoFilterBackend, )
    filter_fields = ('id', )


class ItemCreate(CreateAPIView):
    serializer_class = ItemSerializer

    def create(self, request, *args, **kwargs):
        try:
            price = request.data.get("price")
            if price is not None and float(price) <= 0.0:
                raise ValidationError({"price": "Must be above $0.0"})
        except:
            raise ValidationError({"price": "A valid number is required"})
        return super().create(request, *args, **kwargs)


class ItemRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    lookup_field = "id"
    serializer_class = ItemSerializer


class OrderList(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = (DjangoFilterBackend, )
    filter_fields = ('id', )

