from django.contrib import admin
from .models import Interaccion

@admin.register(Interaccion)
class InteraccionAdmin(admin.ModelAdmin):
    list_display = ("usuario_id", "tema", "timestamp")
    search_fields = ("usuario_id", "tema", "emocion_detectada")
