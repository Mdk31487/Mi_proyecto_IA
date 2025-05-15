# mi_ia_backend/asgi.py

import os
from django.core.asgi import get_asgi_application
from fastapi_app import app as fastapi_app  # Asegúrate de que este sea el path correcto

from starlette.middleware.cors import CORSMiddleware
from starlette.routing import Mount
from starlette.applications import Starlette

# Configurar el entorno para Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mi_ia_backend.settings')

# Inicializar la aplicación ASGI de Django
django_app = get_asgi_application()

# Agregar middleware CORS a la aplicación FastAPI
fastapi_app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Reemplaza "*" con dominios específicos en producción
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Crear la aplicación ASGI combinada
application = Starlette(
    routes=[
        Mount("/fastapi", app=fastapi_app),  # FastAPI accesible en /fastapi
        Mount("/", app=django_app)           # Django maneja el resto
    ]
)
