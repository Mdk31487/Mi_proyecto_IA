from django.urls import path
from .views import RegistrarInteraccionView

urlpatterns = [
    path('registrar/', RegistrarInteraccionView.as_view(), name='registrar_interaccion'),
]
