import pandas as pd
from django.core.management.base import BaseCommand
from analytics_app.models import SalesRecord
from datetime import datetime

class Command(BaseCommand):
    help = 'Import sales data from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to CSV file')

    def handle(self, *args, **options):
        csv_file = options['csv_file']
        df = pd.read_csv(csv_file)
        
        for _, row in df.iterrows():
            SalesRecord.objects.get_or_create(
                order_id=row['Order ID'],
                defaults={
                    'region': row['Region'],
                    'country': row['Country'],
                    'item_type': row['Item Type'],
                    'sales_channel': row['Sales Channel'],
                    'order_priority': row['Order Priority'],
                    'order_date': pd.to_datetime(row['Order Date']).date(),
                    'ship_date': pd.to_datetime(row['Ship Date']).date(),
                    'units_sold': row['Units Sold'],
                    'unit_price': row['Unit Price'],
                    'unit_cost': row['Unit Cost'],
                    'total_revenue': row['Total Revenue'],
                    'total_cost': row['Total Cost'],
                    'total_profit': row['Total Profit'],
                }
            )
        
        self.stdout.write(f'Successfully imported {len(df)} records')