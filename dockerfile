FROM python:3.10-slim

# Evitar archivos .pyc y usar logs legibles
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Instalar dependencias del sistema (por si usas Pillow, psycopg2, etc.)
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    libjpeg-dev \
    zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

# Copiar dependencias e instalarlas
COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copiar el resto del proyecto
COPY . .

# Recolectar archivos estáticos para producción
RUN python manage.py collectstatic --noinput

EXPOSE 8000

# Usa Gunicorn para producción
CMD ["gunicorn", "mi_ia_backend.wsgi:application", "--bind", "0.0.0.0:8000"]
