from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from users.serializers import UserSerializer, AuthTokenSerializer
from rest_framework.settings import api_settings


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    serialzer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

# Create your views here.
