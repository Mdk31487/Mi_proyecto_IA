# users/urls.py
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CustomUserViewSet

# Crear el enrutador y registrar el viewset
router = DefaultRouter()
router.register(r'users', CustomUserViewSet)

# Definir las rutas a usar
urlpatterns = router.urls
