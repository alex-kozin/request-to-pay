from rest_framework.generics import ListAPIView, CreateAPIView, \
    RetrieveUpdateAPIView
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import UserProfileSerializer

from .models import UserProfile


class UserProfileList(ListAPIView):
    """
    View all user profiles ever created. Filtering based on user type enabled.
    """
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    filter_backends = (DjangoFilterBackend, )
    filter_fields = ('id', 'user_type')


class UserProfileRetrieveUpdate(RetrieveUpdateAPIView):
    """
    Read, update or delete user profiles based on id.
    """
    queryset = UserProfile.objects.all()
    lookup_field = "id"
    serializer_class = UserProfileSerializer
