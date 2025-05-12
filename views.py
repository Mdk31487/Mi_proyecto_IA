from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .serializers import UserSerializer, SentimentAnalysisSerializer
from mi_ia_backend.utils import analizar_sentimiento_textblob, generar_recomendacion

class UserList(APIView):
    """Vista para listar usuarios y crear nuevos usuarios."""
    
    def get(self, request):
        """Obtiene todos los usuarios."""
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        """Crea un nuevo usuario."""
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SentimentAnalysisView(APIView):
    """Vista para analizar el sentimiento de un texto y generar una recomendación."""
    
    def post(self, request):
        """Maneja solicitudes POST para analizar sentimientos y generar recomendaciones."""
        serializer = SentimentAnalysisSerializer(data=request.data)
        
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        texto = serializer.validated_data["texto"]

        # Analizar sentimiento y generar recomendación
        sentimiento, _ = analizar_sentimiento_textblob(texto)
        recomendacion = generar_recomendacion(sentimiento)

        return Response(
            {"sentimiento": sentimiento, "recomendacion": recomendacion},
            status=status.HTTP_200_OK,
        )
