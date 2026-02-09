import pandas as pd
from django.core.management.base import BaseCommand
from analytics_app.models import SalesRecord
from django.db import transaction

class Command(BaseCommand):
    help = 'Import sales data from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to CSV file')

    def handle(self, *args, **options):
        csv_file = options['csv_file']
        
        try:
            df = pd.read_csv(csv_file)
            records = []
            
            for _, row in df.iterrows():
                records.append(SalesRecord(
                    order_id=row['Order ID'],
                    region=row['Region'],
                    country=row['Country'],
                    item_type=row['Item Type'],
                    sales_channel=row['Sales Channel'],
                    order_priority=row['Order Priority'],
                    order_date=pd.to_datetime(row['Order Date']).date(),
                    ship_date=pd.to_datetime(row['Ship Date']).date(),
                    units_sold=row['Units Sold'],
                    unit_price=row['Unit Price'],
                    unit_cost=row['Unit Cost'],
                    total_revenue=row['Total Revenue'],
                    total_cost=row['Total Cost'],
                    total_profit=row['Total Profit'],
                ))
            
            with transaction.atomic():
                SalesRecord.objects.bulk_create(records, ignore_conflicts=True)
            
            self.stdout.write(f'Successfully imported {len(records)} records')
            
        except Exception as e:
            self.stdout.write(f'Error importing CSV: {str(e)}')