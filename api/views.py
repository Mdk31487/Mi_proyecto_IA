from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.contrib.auth.models import User
from .serializers import UserSerializer
import jwt
from datetime import datetime, timedelta

# Configuración para generación de tokens
SECRET_KEY = "mi_secreto_super_seguro"
ALGORITHM = "HS256"
TOKEN_EXPIRATION_HOURS = 1

# --- VISTAS BÁSICAS Y DE PRUEBA ---

@api_view(['GET'])
def index(request):
    """Ruta de bienvenida a la API"""
    return Response({"mensaje": "¡Bienvenido a mi IA Backend!"}, status=status.HTTP_200_OK)

class SaludoAPIView(APIView):
    """Endpoint que devuelve un saludo"""
    def get(self, request):
        return Response({"message": "Hola, bienvenido a la API!"}, status=status.HTTP_200_OK)

class TestView(APIView):
    """Endpoint de prueba para verificar la conexión con la IA"""
    def get(self, request):
        return Response({"message": "¡Tu IA está lista para interactuar!"}, status=status.HTTP_200_OK)

# --- USUARIOS ---

class UserList(APIView):
    """Vista para obtener la lista de usuarios o crear un nuevo usuario"""
    
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# --- MODELO Y TOKEN ---

class UploadModelView(APIView):
    """Endpoint para subir un modelo IA"""
    def post(self, request):
        name = request.data.get("name")
        if not name:
            return Response({"error": "El nombre del modelo es obligatorio."}, status=status.HTTP_400_BAD_REQUEST)
        # Lógica de subida del modelo (por hacer)
        return Response({"status": "Modelo subido correctamente", "model_name": name}, status=status.HTTP_200_OK)

class GenerateTokenView(APIView):
    """Endpoint para generar un token JWT"""
    def post(self, request):
        username = request.data.get("username")
        if not username:
            return Response({"error": "El nombre de usuario es obligatorio."}, status=status.HTTP_400_BAD_REQUEST)
        expiration = datetime.utcnow() + timedelta(hours=TOKEN_EXPIRATION_HOURS)
        token_data = {"sub": username, "exp": expiration}
        token = jwt.encode(token_data, SECRET_KEY, algorithm=ALGORITHM)
        return Response({
            "access_token": token,
            "token_type": "bearer",
            "expires_in": TOKEN_EXPIRATION_HOURS * 3600
        }, status=status.HTTP_200_OK)
