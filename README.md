# 📊 Sales Analytics Platform

A comprehensive sales data analytics platform built with **Django** and **Streamlit**, featuring interactive dashboards, REST APIs, and admin panel for business intelligence.

## Features

### Interactive Dashboard (Streamlit)
- **Real-time Analytics** - Live data visualization
- **Interactive Charts** - Bar charts, pie charts, comparison graphs
- **Key Metrics** - Revenue, costs, product performance
- **Responsive Design** - Works on desktop and mobile
- **Auto-refresh** - Real-time data updates

### Admin Panel (Django)
- **Data Management** - Add, edit, delete sales records
- **User Authentication** - Secure admin access
- **Search & Filter** - Advanced data filtering
- **Bulk Operations** - Import/export capabilities

### REST API (Django REST Framework)
- **RESTful Endpoints** - Clean API architecture
- **JSON Responses** - Standard data format
- **CORS Enabled** - Cross-origin requests
- **Scalable** - Production-ready

## Project Structure

```
Sales Data Running Project/
├── analytics_app/              # Django app
│   ├── models.py              # Database models
│   ├── views.py               # API views
│   ├── admin.py               # Admin configuration
│   ├── urls.py                # URL routing
│   └── management/commands/    # Custom commands
├── sales_analytics/           # Django project
│   ├── settings.py            # Project settings
│   └── urls.py                # Main URL config
├── streamlit_dashboard.py     # Streamlit dashboard
├── manage.py                  # Django management
├── start_platform.sh          # Startup script
├── requirements_django.txt    # Dependencies
└── db.sqlite3                # SQLite database
```

## Installation

### Prerequisites
- Python 3.9+
- pip package manager

### Setup
```bash
# Clone/navigate to project
cd "Sales Data Running Project"

# Install dependencies
pip install -r requirements_django.txt

# Run database migrations
python3 manage.py migrate
python3 manage.py makemigrations analytics_app
python3 manage.py migrate

# Create admin user
python3 manage.py createsuperuser

# Import CSV data (if needed)
python3 manage.py import_csv "path/to/your/sales_data.csv"
```

## Running the Platform

### Option 1: Quick Start (Recommended)
```bash
./start_platform.sh
```

### Option 2: Manual Start
```bash
# Terminal 1: Start Django API
python3 manage.py runserver 8000

# Terminal 2: Start Streamlit Dashboard
python3 -m streamlit run streamlit_dashboard.py --server.port 8501
```

## Access Points

| Service | URL | Description |
|---------|-----|-------------|
| **Streamlit Dashboard** | http://localhost:8501 | Main analytics dashboard |
| **Django Admin** | http://localhost:8000/admin | Data management panel |
| **REST API** | http://localhost:8000/api | REST API endpoints |

## Dashboard Features

### Key Metrics
- Total sales records
- Total revenue
- Number of countries
- Product types count

### Interactive Charts
- **Top Suppliers** - Countries with highest costs
- **Top Clients** - Countries with highest revenue
- **Product Performance** - Units sold by product type
- **Revenue vs Cost** - Comparative analysis

### Data Tables
- Detailed supplier information
- Client revenue breakdown
- Product performance metrics

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/suppliers/` | GET | Top suppliers by cost |
| `/api/clients/` | GET | Top clients by revenue |
| `/api/products/` | GET | Product performance data |
| `/api/dashboard/` | GET | Combined dashboard data |

### Example API Response
```json
{
  "suppliers": {"Honduras": 4726597.96, "Turkmenistan": 4554777.8},
  "clients": {"Germany": 5234567.89, "France": 4567890.12},
  "products": {"Cosmetics": 15000, "Clothes": 12000},
  "total_records": 100,
  "total_revenue": 50000000.00
}
```

## Admin Credentials

**Default Admin User:**
- **Username:** `admin`
- **Password:** `password`
- **Email:** `admin@example.com`

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

### Core Frameworks
- **Django 4.2+** - Web framework & API
- **Django REST Framework** - API endpoints
- **Streamlit** - Interactive dashboard

### Data & Visualization
- **Pandas** - Data manipulation
- **NumPy** - Numerical computing
- **Plotly** - Interactive charts
- **Requests** - HTTP client

### Additional
- **Django CORS Headers** - CORS handling

## Configuration

### Django Settings
- **Database:** SQLite (development)
- **Debug Mode:** Enabled (development)
- **CORS:** Enabled for all origins
- **API Only:** No templates or static files

### Streamlit Config
- **Port:** 8501
- **Auto-refresh:** 60 seconds
- **Interactive Charts:** Plotly integration

## Performance

- **Database:** Optimized queries with Django ORM
- **API:** RESTful endpoints with JSON responses
- **Caching:** Streamlit data caching (60s TTL)
- **Visualization:** Fast interactive Plotly charts
- **Architecture:** Clean separation of API and dashboard

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

For issues and questions:
- Check Django API logs: `tail -f django.log`
- Review Streamlit dashboard: `tail -f streamlit.log`
- Verify API endpoints: http://localhost:8000/api/dashboard
- Ensure both servers are running on ports 8000 & 8501

---
