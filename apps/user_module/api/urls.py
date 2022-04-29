from django.urls import path
from rest_framework import routers
from .api import *

prefix_router = 'users'
prefix_app = 'u/'

# Con router y la configuracion del UserViewSet permite crear automaticamente el CRUD
# para la clase User
router = routers.DefaultRouter()
router.register(prefix_router, UserViewSet, 'users')

urlpatterns = router.urls

# Las rutas personalizadas
urlpatterns += [
    # No podia ser user/profile/ ya que user/ esta en el router
    path(prefix_app + 'profile/', ProfileView.as_view()),
]