
# IA Game System

Este es un sistema base para una aplicación de juego interactiva impulsada por una IA. Incluye:

- Autenticación de usuarios
- Gestión de mundos y personajes
- Sistema de emociones para la IA
- Interfaces básicas de administración visual

## Requisitos

Python 3.10+

Instala las dependencias con:

```bash
pip install -r requirements.txt
```

## Configuración

1. Crea la base de datos:

```bash
python manage.py makemigrations
python manage.py migrate
```

2. Crea un superusuario para acceder al admin:

```bash
python manage.py createsuperuser
```

3. Ejecuta el servidor:

```bash
python manage.py runserver
```

Accede a la aplicación en [http://127.0.0.1:8000](http://127.0.0.1:8000)

## Funcionalidades

- Registro e inicio de sesión
- Creación y edición de mundos
- Creación y personalización de personajes
- IA base conectada al sistema emocional
