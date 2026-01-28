#!/bin/bash

echo "Starting Sales Analytics Platform with Power BI Integration..."

# Start Django API server
echo "Starting Django API server on port 8000..."
echo "Power BI endpoints available at:"
echo "  - http://localhost:8000/api/powerbi/sales-summary/"
echo "  - http://localhost:8000/api/powerbi/country-metrics/"
echo "  - http://localhost:8000/api/powerbi/product-metrics/"
echo "  - http://localhost:8000/api/powerbi/monthly-trends/"
echo "  - http://localhost:8000/api/powerbi/sales-channel-metrics/"
echo "  - http://localhost:8000/api/powerbi/regional-summary/"
echo ""
echo "Django Admin available at: http://localhost:8000/admin"
echo "Legacy API endpoints still available for backward compatibility"
echo ""
echo "See POWER_BI_SETUP.md for Power BI integration instructions"
echo ""

python3 manage.py runserver 8000