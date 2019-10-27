from rest_framework.generics import ListAPIView

from .serializers import ItemSerializer
from .models import Item


class ItemList(ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
