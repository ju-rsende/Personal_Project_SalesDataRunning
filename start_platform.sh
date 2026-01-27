#!/bin/bash

echo "Starting Sales Analytics Platform..."

# Start Django server in background
echo "Starting Django API server..."
python3 manage.py runserver 8000 &
DJANGO_PID=$!

# Wait for Django to start
sleep 3

# Start Streamlit dashboard
echo "Starting Streamlit dashboard..."
streamlit run streamlit_dashboard.py --server.port 8501

# Cleanup on exit
trap "kill $DJANGO_PID" EXIT