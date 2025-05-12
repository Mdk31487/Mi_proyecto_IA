# mi_ia_backend/urls.py
from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

# Vista para la ruta raíz
def home(request):
    return JsonResponse({"mensaje": "¡Bienvenido a mi IA Backend!"})

urlpatterns = [
    path('admin/', admin.site.urls),  # Ruta para el panel de administración
    path('api/', include('api.urls')),  # Incluir las rutas de la app 'api'
    path('', home, name='home'),  # Ruta raíz
    path('favicon.ico', RedirectView.as_view(url='/static/favicon.ico', permanent=True)),  # Redirige favicon
]

# Servir archivos estáticos en modo DEBUG
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
