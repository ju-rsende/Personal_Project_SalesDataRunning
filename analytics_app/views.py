from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from django.db.models import Sum, Avg, Count
from django.db.models.functions import TruncMonth
from .models import SalesRecord

@api_view(['GET'])
def powerbi_sales_summary(request):
    """Main sales data table for Power BI - all records with key metrics"""
    queryset = SalesRecord.objects.all()
    
    paginator = PageNumberPagination()
    paginator.page_size = 1000
    paginated_records = paginator.paginate_queryset(queryset, request)
    
    data = []
    for record in paginated_records:
        data.append({
            'OrderID': record.order_id,
            'Region': record.region,
            'Country': record.country,
            'ItemType': record.item_type,
            'SalesChannel': record.sales_channel,
            'OrderPriority': record.order_priority,
            'OrderDate': record.order_date.isoformat(),
            'ShipDate': record.ship_date.isoformat(),
            'UnitsSold': record.units_sold,
            'UnitPrice': float(record.unit_price),
            'UnitCost': float(record.unit_cost),
            'TotalRevenue': float(record.total_revenue),
            'TotalCost': float(record.total_cost),
            'TotalProfit': float(record.total_profit),
            'ProfitMargin': round(float(record.total_profit / record.total_revenue * 100), 2) if record.total_revenue and record.total_revenue > 0 else 0
        })
    
    return paginator.get_paginated_response(data)

@api_view(['GET'])
def powerbi_country_metrics(request):
    """Country-level aggregated metrics for Power BI"""
    data = SalesRecord.objects.values('region', 'country').annotate(
        total_orders=Count('order_id'),
        total_revenue=Sum('total_revenue'),
        total_cost=Sum('total_cost'),
        total_profit=Sum('total_profit'),
        total_units=Sum('units_sold'),
        avg_order_value=Avg('total_revenue')
    ).order_by('region', 'country')
    
    result = []
    for item in data:
        result.append({
            'Region': item['region'],
            'Country': item['country'],
            'TotalOrders': item['total_orders'],
            'TotalRevenue': float(item['total_revenue']),
            'TotalCost': float(item['total_cost']),
            'TotalProfit': float(item['total_profit']),
            'TotalUnits': item['total_units'],
            'AvgOrderValue': float(item['avg_order_value']),
            'ProfitMargin': round(float(item['total_profit'] / item['total_revenue'] * 100), 2) if item['total_revenue'] and item['total_revenue'] > 0 else 0
        })
    
    return Response(result)

@api_view(['GET'])
def powerbi_product_metrics(request):
    """Product-level aggregated metrics for Power BI"""
    data = SalesRecord.objects.values('item_type').annotate(
        total_orders=Count('order_id'),
        total_revenue=Sum('total_revenue'),
        total_cost=Sum('total_cost'),
        total_profit=Sum('total_profit'),
        total_units=Sum('units_sold'),
        avg_unit_price=Avg('unit_price'),
        avg_unit_cost=Avg('unit_cost')
    ).order_by('-total_revenue')
    
    result = []
    for item in data:
        result.append({
            'ItemType': item['item_type'],
            'TotalOrders': item['total_orders'],
            'TotalRevenue': float(item['total_revenue']),
            'TotalCost': float(item['total_cost']),
            'TotalProfit': float(item['total_profit']),
            'TotalUnits': item['total_units'],
            'AvgUnitPrice': float(item['avg_unit_price']),
            'AvgUnitCost': float(item['avg_unit_cost']),
            'ProfitMargin': round(float(item['total_profit'] / item['total_revenue'] * 100), 2) if item['total_revenue'] and item['total_revenue'] > 0 else 0
        })
    
    return Response(result)

@api_view(['GET'])
def powerbi_monthly_trends(request):
    """Monthly sales trends for Power BI time series analysis"""
    data = SalesRecord.objects.annotate(
        year_month=TruncMonth('order_date')
    ).values('year_month').annotate(
        total_orders=Count('order_id'),
        total_revenue=Sum('total_revenue'),
        total_cost=Sum('total_cost'),
        total_profit=Sum('total_profit'),
        total_units=Sum('units_sold')
    ).order_by('year_month')
    
    result = []
    for item in data:
        result.append({
            'YearMonth': item['year_month'].isoformat(),
            'Year': item['year_month'].year,
            'Month': item['year_month'].month,
            'MonthName': item['year_month'].strftime('%B'),
            'TotalOrders': item['total_orders'],
            'TotalRevenue': float(item['total_revenue']),
            'TotalCost': float(item['total_cost']),
            'TotalProfit': float(item['total_profit']),
            'TotalUnits': item['total_units'],
            'ProfitMargin': round(float(item['total_profit'] / item['total_revenue'] * 100), 2) if item['total_revenue'] and item['total_revenue'] > 0 else 0
        })
    
    return Response(result)

@api_view(['GET'])
def powerbi_sales_channel_metrics(request):
    """Sales channel performance metrics for Power BI"""
    data = SalesRecord.objects.values('sales_channel', 'order_priority').annotate(
        total_orders=Count('order_id'),
        total_revenue=Sum('total_revenue'),
        total_cost=Sum('total_cost'),
        total_profit=Sum('total_profit'),
        total_units=Sum('units_sold'),
        avg_order_value=Avg('total_revenue')
    ).order_by('sales_channel', '-total_revenue')
    
    result = []
    for item in data:
        result.append({
            'SalesChannel': item['sales_channel'],
            'OrderPriority': item['order_priority'],
            'TotalOrders': item['total_orders'],
            'TotalRevenue': float(item['total_revenue']),
            'TotalCost': float(item['total_cost']),
            'TotalProfit': float(item['total_profit']),
            'TotalUnits': item['total_units'],
            'AvgOrderValue': float(item['avg_order_value']),
            'ProfitMargin': round(float(item['total_profit'] / item['total_revenue'] * 100), 2) if item['total_revenue'] and item['total_revenue'] > 0 else 0
        })
    
    return Response(result)

@api_view(['GET'])
def powerbi_regional_summary(request):
    """Regional summary metrics for Power BI"""
    data = SalesRecord.objects.values('region').annotate(
        total_countries=Count('country', distinct=True),
        total_orders=Count('order_id'),
        total_revenue=Sum('total_revenue'),
        total_cost=Sum('total_cost'),
        total_profit=Sum('total_profit'),
        total_units=Sum('units_sold'),
        avg_order_value=Avg('total_revenue')
    ).order_by('-total_revenue')
    
    result = []
    for item in data:
        result.append({
            'Region': item['region'],
            'TotalCountries': item['total_countries'],
            'TotalOrders': item['total_orders'],
            'TotalRevenue': float(item['total_revenue']),
            'TotalCost': float(item['total_cost']),
            'TotalProfit': float(item['total_profit']),
            'TotalUnits': item['total_units'],
            'AvgOrderValue': float(item['avg_order_value']),
            'ProfitMargin': round(float(item['total_profit'] / item['total_revenue'] * 100), 2) if item['total_revenue'] and item['total_revenue'] > 0 else 0
        })
    
    return Response(result)