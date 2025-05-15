# interacciones/serializers.py

from rest_framework import serializers
from .models import Interaccion

class InteraccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interaccion
        fields = '__all__'
