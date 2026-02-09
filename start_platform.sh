#!/bin/bash

echo "Starting Sales Analytics API..."
echo ""
echo "Power BI endpoints:"
echo "  http://localhost:8000/api/powerbi/sales-summary/"
echo "  http://localhost:8000/api/powerbi/country-metrics/"
echo "  http://localhost:8000/api/powerbi/product-metrics/"
echo "  http://localhost:8000/api/powerbi/monthly-trends/"
echo "  http://localhost:8000/api/powerbi/sales-channel-metrics/"
echo "  http://localhost:8000/api/powerbi/regional-summary/"
echo ""
echo "Admin: http://localhost:8000/admin"
echo ""

python3 manage.py runserver 8000