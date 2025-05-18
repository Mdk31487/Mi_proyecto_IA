#!/bin/bash

echo "Esperando a que PostgreSQL levante..."
while ! nc -z db 5432; do
  sleep 0.1
done

echo "PostgreSQL levantado. Corriendo migraciones..."
python manage.py migrate
exec "$@"