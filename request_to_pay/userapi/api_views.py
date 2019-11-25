from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import UserSerializer

from .models import User


class UserList(ListAPIView):
    """
    View all users ever created. Filtering based on user type and email enabled.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (DjangoFilterBackend, )
    filter_fields = ('id', 'user_type', 'email')


class UserRetrieveUpdate(RetrieveUpdateAPIView):
    """
    Read, update or delete users based on id.
    """
    queryset = User.objects.all()
    lookup_field = "id"
    serializer_class = UserSerializer
