from django.contrib import admin
from django.urls import path
from .api import *
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenObtainPairView,
    TokenVerifyView,
)

prefix_app = 'auth/'

urlpatterns = [
    path(prefix_app + 'get-token/', GenerateTokenView.as_view()),
    path(prefix_app + 'token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path(prefix_app + 'token/refresh/', MyTokenRefreshView.as_view(), name='token_refresh'),
    path(prefix_app + 'token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]