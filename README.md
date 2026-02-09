# 📊 Sales Analytics API for Power BI

Django REST API backend optimized for Power BI dashboards, providing clean data endpoints for business intelligence and analytics.

## Features

- **Power BI Optimized Endpoints** - Pre-aggregated data for fast BI consumption
- **RESTful API** - Clean, scalable architecture
- **Admin Panel** - Data management interface
- **Multiple Analysis Views** - Country, product, channel, time-based metrics

## Project Structure

```
Personal_Project_SalesDataRunning/
├── analytics_app/              # Django app
│   ├── models.py              # Database models
│   ├── views.py               # API views
│   ├── admin.py               # Admin configuration
│   ├── urls.py                # URL routing
│   └── management/commands/    # Custom commands
├── sales_analytics/           # Django project
│   ├── settings.py            # Project settings
│   └── urls.py                # Main URL config
├── manage.py                  # Django management
├── start_platform.sh          # Startup script
├── requirements_django.txt    # Dependencies
├── POWER_BI_SETUP.md         # Power BI guide
└── db.sqlite3                # SQLite database
```

## Installation

### Prerequisites
- Python 3.9+
- pip package manager

### Setup
```bash
# Navigate to project
cd Personal_Project_SalesDataRunning

# Install dependencies
pip install -r requirements_django.txt

# Run migrations
python3 manage.py migrate

# Create admin user
python3 manage.py createsuperuser

# Import CSV data (optional)
python3 manage.py import_csv "path/to/sales_data.csv"
```

## Running the Platform

### Quick Start
```bash
./start_platform.sh
```

### Manual Start
```bash
# Start Django API server
python3 manage.py runserver 8000
```

## Access Points

| Service | URL |
|---------|-----|
| **Django Admin** | http://localhost:8000/admin |
| **Power BI Endpoints** | http://localhost:8000/api/powerbi/ |

## Power BI Integration

See [POWER_BI_SETUP.md](POWER_BI_SETUP.md) for complete Power BI setup instructions.

### Power BI Endpoints

| Endpoint | Purpose | Key Fields |
|----------|---------|------------|
| `/api/powerbi/sales-summary/` | Main fact table | All sales data with calculated metrics |
| `/api/powerbi/country-metrics/` | Country analysis | Regional performance data |
| `/api/powerbi/product-metrics/` | Product analysis | Product performance metrics |
| `/api/powerbi/monthly-trends/` | Time series | Monthly trends and patterns |
| `/api/powerbi/sales-channel-metrics/` | Channel analysis | Sales channel performance |
| `/api/powerbi/regional-summary/` | Regional overview | High-level regional metrics |

## API Endpoints

All endpoints are optimized for Power BI consumption:

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/powerbi/sales-summary/` | GET | All sales records with metrics |
| `/api/powerbi/country-metrics/` | GET | Country-level aggregations |
| `/api/powerbi/product-metrics/` | GET | Product performance data |
| `/api/powerbi/monthly-trends/` | GET | Time series analysis |
| `/api/powerbi/sales-channel-metrics/` | GET | Channel performance |
| `/api/powerbi/regional-summary/` | GET | Regional overview |

## Admin Access

Create your admin user during setup:
```bash
python3 manage.py createsuperuser
```

## Data Management

### Import CSV Data
```bash
python3 manage.py import_csv "path/to/sales_data.csv"
```

### Set Admin Password
```bash
python3 manage.py setpassword
```

### Database Operations
```bash
# Reset database
python3 manage.py flush

# Create migrations
python3 manage.py makemigrations

# Apply migrations
python3 manage.py migrate
```

## Security Features

- **CSRF Protection** - Django built-in security
- **Admin Authentication** - Secure admin access
- **CORS Headers** - Cross-origin request handling
- **SQL Injection Protection** - ORM-based queries

## Dependencies

- **Django 4.2+** - Web framework & ORM
- **Django REST Framework** - API endpoints
- **Django CORS Headers** - Cross-origin requests

## Configuration

- **Database:** SQLite (development)
- **Debug Mode:** Enabled (development only)
- **CORS:** Enabled for Power BI access

## Performance

- **Optimized Queries** - Django ORM with aggregations
- **Pre-calculated Metrics** - Reduced Power BI processing
- **Clean JSON** - Fast API responses

## Production Deployment

### Environment Variables
```bash
export DJANGO_SECRET_KEY="your-secret-key"
export DEBUG=False
export ALLOWED_HOSTS="your-domain.com"
```

### Database Migration
- Switch from SQLite to PostgreSQL/MySQL
- Update `DATABASES` in `settings.py`
- Run migrations

### Static Files
```bash
# Not needed - API only backend
# Streamlit handles all frontend assets
```

## License

This project is licensed under the MIT License.

## Support

For issues:
- Check logs: `python3 manage.py runserver`
- Verify endpoints: http://localhost:8000/api/powerbi/sales-summary/
- Admin panel: http://localhost:8000/admin

---
