#!/bin/bash

# Generate a secure secret key if not set
if [ -z "$DJANGO_SECRET_KEY" ]; then
    export DJANGO_SECRET_KEY=$(python3 -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())")
    echo "Generated new SECRET_KEY for this session"
fi

# Start the Django server
python3 manage.py runserver 8000