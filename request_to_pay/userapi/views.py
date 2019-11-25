from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


class ProfileView(APIView):
    """Decode the current user based on their token,
    and return their serialized profile information."""
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        return Response(UserSerializer(request.user).data)
