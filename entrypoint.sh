#!/bin/sh

# ======================================================
# AGUARDA DATABASE
# ======================================================

echo "Aguardando PostgreSQL..."

while ! nc -z db 5432; do
  sleep 1
done

echo "PostgreSQL iniciado."

# ======================================================
# DJANGO
# ======================================================

python manage.py migrate --noinput

python manage.py collectstatic --noinput

# ======================================================
# GUNICORN
# ======================================================

exec gunicorn config.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 3 \
    --timeout 120