from django.contrib import admin
from .models import SalesRecord

@admin.register(SalesRecord)
class SalesRecordAdmin(admin.ModelAdmin):
    list_display = ['order_id', 'country', 'item_type', 'total_revenue', 'total_profit', 'order_date']
    list_filter = ['region', 'country', 'item_type', 'sales_channel', 'order_date']
    search_fields = ['order_id', 'country', 'item_type']
    date_hierarchy = 'order_date'
    list_per_page = 50