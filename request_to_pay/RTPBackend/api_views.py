from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import ItemSerializer
from .models import Item


class ItemList(ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_backends = (DjangoFilterBackend, )
    filter_fields = ('id', )
