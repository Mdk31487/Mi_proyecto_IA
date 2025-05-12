# api/urls.py

from django.urls import path
from .views import SaludoAPIView, TestView, index, UserList  # Importar todas las vistas necesarias
from rest_framework_simplejwt import views as jwt_views  # Importar vistas de autenticación JWT

# Mensaje de depuración
print("Cargando las rutas de API...")

# Definición de las rutas de la API
urlpatterns = [
    # Rutas principales
    path('', index, name='index'),  # Ruta principal de la API
    path('saludo/', SaludoAPIView.as_view(), name='saludo'),  # Ruta para saludo
    path('test/', TestView.as_view(), name='test'),  # Ruta de prueba de la IA

    # Rutas de autenticación con JWT
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

    # Rutas para los usuarios
    path('users/', UserList.as_view(), name='user-list'),  # Ruta para lista de usuarios
]
