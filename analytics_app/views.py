from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Sum, Avg, Count
from .models import SalesRecord
import pandas as pd

@api_view(['GET'])
def suppliers_analysis(request):
    data = SalesRecord.objects.values('country').annotate(
        total_cost=Sum('total_cost')
    ).order_by('-total_cost')[:10]
    return Response({item['country']: float(item['total_cost']) for item in data})

@api_view(['GET'])
def clients_analysis(request):
    data = SalesRecord.objects.values('country').annotate(
        total_revenue=Sum('total_revenue')
    ).order_by('-total_revenue')[:10]
    return Response({item['country']: float(item['total_revenue']) for item in data})

@api_view(['GET'])
def products_analysis(request):
    data = SalesRecord.objects.values('item_type').annotate(
        units_sold=Sum('units_sold')
    ).order_by('-units_sold')
    return Response({item['item_type']: item['units_sold'] for item in data})

@api_view(['GET'])
def dashboard_data(request):
    suppliers = SalesRecord.objects.values('country').annotate(
        total_cost=Sum('total_cost')).order_by('-total_cost')[:5]
    clients = SalesRecord.objects.values('country').annotate(
        total_revenue=Sum('total_revenue')).order_by('-total_revenue')[:5]
    products = SalesRecord.objects.values('item_type').annotate(
        units_sold=Sum('units_sold')).order_by('-units_sold')[:5]
    
    return Response({
        'suppliers': {item['country']: float(item['total_cost']) for item in suppliers},
        'clients': {item['country']: float(item['total_revenue']) for item in clients},
        'products': {item['item_type']: item['units_sold'] for item in products},
        'total_records': SalesRecord.objects.count(),
        'total_revenue': float(SalesRecord.objects.aggregate(Sum('total_revenue'))['total_revenue__sum'] or 0)
    })