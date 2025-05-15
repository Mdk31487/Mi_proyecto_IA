from rest_framework import serializers
from django.contrib.auth.models import User

# Serializador para el análisis de sentimientos
class SentimentAnalysisSerializer(serializers.Serializer):
    texto = serializers.CharField(
        required=True,
        allow_blank=False,
        max_length=1000,
        error_messages={
            "required": "El campo 'texto' es obligatorio.",
            "blank": "El campo 'texto' no puede estar vacío.",
            "max_length": "El texto no puede superar los 1000 caracteres."
        }
    )

# Serializador para el modelo User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Este correo electrónico ya está registrado.")
        return value
