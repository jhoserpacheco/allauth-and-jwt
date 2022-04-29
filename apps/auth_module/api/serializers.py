from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer, ValidationError
from rest_framework_simplejwt.state import token_backend

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Si se quiere agregar algo al token
        # ...

        return token

class MyTokenRefreshSerializer(TokenRefreshSerializer):
    def validate(self, attrs):
        data = super(MyTokenRefreshSerializer, self).validate(attrs)
        
        # En caso de que se requiera personalizar el token de refresh
        #decoded_payload = token_backend.decode(data['access'], verify=True)
        #user_uid=decoded_payload['user_id']

        return data