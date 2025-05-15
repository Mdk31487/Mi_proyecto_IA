from decouple import config  # <-- agrega esto al inicio
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import InteraccionSerializer
from .models import Interaccion

from core.ia import generar_respuesta_ia, detectar_emocion_basica
from mi_ia_backend.utils import analizar_sentimiento_textblob

class RegistrarInteraccionView(APIView):
    def post(self, request):
        data = request.data.copy()

        # Configuración para cambiar entre análisis básico o con TextBlob
        usar_textblob = config('USAR_TEXTBLOB', default='false').lower() == 'true'

        # Detectar emoción automáticamente si no se proporciona
        if not data.get('emocion_detectada') and data.get('mensaje_usuario'):
            if usar_textblob:
                data['emocion_detectada'] = analizar_sentimiento_textblob(data['mensaje_usuario'])
            else:
                data['emocion_detectada'] = detectar_emocion_basica(data['mensaje_usuario'])

        # Generar respuesta automática de la IA
        if data.get('mensaje_usuario'):
            respuesta_ia = generar_respuesta_ia(data['mensaje_usuario'])
            data['respuesta_ia'] = respuesta_ia  # Guardar la respuesta de la IA en los datos

        serializer = InteraccionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        interacciones = Interaccion.objects.all().order_by('-timestamp')
        serializer = InteraccionSerializer(interacciones, many=True)
        return Response(serializer.data)
