import requests
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from django.contrib.auth.hashers import make_password
from django.contrib import auth
from django.conf import settings
from apps.user_module.models import User
from .serializers import MyTokenObtainPairSerializer, MyTokenRefreshSerializer

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class MyTokenRefreshView(TokenRefreshView):
    serializer_class = MyTokenRefreshSerializer

class GenerateTokenView(APIView):
    def get(self, request):
        user = User.objects.get(id=request.user.id)

        #Si el usuario es nuevo no tendra clave por django, es decir no tiene el prefije pbkdf2
        if 'pbkdf2' not in user.password:
            user.password = make_password(settings.SECRET_KEY)
            user.save()

        refresh = RefreshToken.for_user(user)
        return Response({'access': str(refresh.access_token), 'refresh': str(refresh)})
