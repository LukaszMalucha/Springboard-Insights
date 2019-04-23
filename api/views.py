from rest_framework import generics, authentication, permissions, viewsets, status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.settings import api_settings
from api.serializers import UserSerializer, AuthTokenSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from core.permissions import IsAdminOrReadOnly
from core.models import Course
from api import serializers


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""
    serializer_class = UserSerializer  # generic view - specify serializer you want to use only


class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for user"""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user"""
    serializer_class = UserSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        """Retrieve and return authenticated user"""
        return self.request.user



class CourseViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, IsAdminOrReadOnly)
    serializer_class = serializers.CourseSerializer
    queryset = Course.objects.all()

    def get_queryset(self):
        queryset = self.queryset
        return queryset.order_by('-title')

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

