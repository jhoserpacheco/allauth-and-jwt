import jwt
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import permissions
from django.conf import settings
from .serializers import *
from apps.user_module.models import User

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer

class ProfileView(APIView):
    def get(self, request, format=None):
        token = request.META.get('HTTP_AUTHORIZATION')
        token = token.split(' ')[1]

        try:
            payload = jwt.decode(jwt=token, key=settings.SECRET_KEY, algorithms=['HS256'])
            user = User.objects.get(id=payload['user_id'])
            return Response(UserSerializer(user).data)
        except jwt.ExpiredSignatureError as e:
            return Response({'error': 'Activations link expired'})
        except jwt.exceptions.DecodeError as e:
            return Response({'error': 'Invalid Token'})