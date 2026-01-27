from django.urls import path
from . import views

urlpatterns = [
    path('api/suppliers/', views.suppliers_analysis, name='suppliers'),
    path('api/clients/', views.clients_analysis, name='clients'),
    path('api/products/', views.products_analysis, name='products'),
    path('api/dashboard/', views.dashboard_data, name='dashboard_data'),
]