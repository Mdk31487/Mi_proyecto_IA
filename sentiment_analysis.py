import os
import django

# Establecer la configuración de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mi_ia_backend.settings')
django.setup()

# Importar componentes de Django y otros módulos necesarios
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from mi_ia_backend.serializers import SentimentAnalysisSerializer
from mi_ia_backend.utils import analizar_sentimiento_textblob, generar_recomendacion

class SentimentAnalysisView(APIView):
    def post(self, request):
        # Validar los datos recibidos mediante el serializer
        serializer = SentimentAnalysisSerializer(data=request.data)
        
        if serializer.is_valid():
            texto = serializer.validated_data['texto']

            # Analizar el sentimiento del texto
            sentimiento = analizar_sentimiento_textblob(texto)

            # Generar una recomendación basada en el sentimiento
            recomendacion = generar_recomendacion(sentimiento)

            # Devolver la respuesta con el sentimiento y la recomendación
            return Response({
                "sentimiento": sentimiento,
                "recomendacion": recomendacion
            }, status=status.HTTP_200_OK)

        # Si el serializer no es válido, devolver los errores
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
