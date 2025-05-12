# urls.py

from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Vista para la ruta raíz
def home(request):
    return JsonResponse({"mensaje": "¡Bienvenido a mi IA Backend!"})

# Configuración de la documentación de la API con Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="Mi API",
        default_version='v1',
        description="Documentación de mi API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@miapi.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# URL patterns
urlpatterns = [
    # Rutas principales
    path('admin/', admin.site.urls),  # Panel de administración
    path('', home, name='home'),  # Ruta raíz
    path('favicon.ico', RedirectView.as_view(url='/static/favicon.ico', permanent=True)),  # Redirección de favicon

    # Rutas de autenticación
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Rutas de autenticación con JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Ruta para la documentación Swagger
    path('swagger/', schema_view.as_view(), name='schema-swagger-ui'),

    # Rutas de la app 'api'
    path('api/', include('api.urls')),  # Conectar las URLs de la app 'api'
]

# Servir archivos estáticos en modo DEBUG
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
