# interacciones/models.py
# Create your models here.

from django.db import models
from django.utils import timezone

class Interaccion(models.Model):
    usuario_id = models.CharField(max_length=100, null=True, blank=True)
    mensaje_usuario = models.TextField()
    respuesta_ia = models.TextField(blank=True, null=True)
    emocion_detectada = models.CharField(max_length=50, null=True, blank=True)
    tema = models.CharField(max_length=100, null=True, blank=True)
    timestamp = models.DateTimeField(default=timezone.now)

    def str(self):
        return f"Interacción de {self.usuario_id} - {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}"
