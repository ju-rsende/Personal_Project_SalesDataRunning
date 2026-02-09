from django.urls import path
from . import views

urlpatterns = [
    path('powerbi/sales-summary/', views.powerbi_sales_summary, name='powerbi_sales_summary'),
    path('powerbi/country-metrics/', views.powerbi_country_metrics, name='powerbi_country_metrics'),
    path('powerbi/product-metrics/', views.powerbi_product_metrics, name='powerbi_product_metrics'),
    path('powerbi/monthly-trends/', views.powerbi_monthly_trends, name='powerbi_monthly_trends'),
    path('powerbi/sales-channel-metrics/', views.powerbi_sales_channel_metrics, name='powerbi_sales_channel_metrics'),
    path('powerbi/regional-summary/', views.powerbi_regional_summary, name='powerbi_regional_summary'),
]