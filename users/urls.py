from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomUserViewSet, profile_view

router = DefaultRouter()
router.register(r'users', CustomUserViewSet)

urlpatterns = [
    path('perfil/', profile_view, name='profile'),  # Vista del perfil con login requerido
    path('', include(router.urls)),  # API de usuarios
]
