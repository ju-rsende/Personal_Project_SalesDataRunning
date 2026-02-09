from django.db import models

class SalesRecord(models.Model):
    region = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    item_type = models.CharField(max_length=100)
    sales_channel = models.CharField(max_length=50)
    order_priority = models.CharField(max_length=20)
    order_date = models.DateField()
    order_id = models.CharField(max_length=50, unique=True)
    ship_date = models.DateField()
    units_sold = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    unit_cost = models.DecimalField(max_digits=10, decimal_places=2)
    total_revenue = models.DecimalField(max_digits=15, decimal_places=2)
    total_cost = models.DecimalField(max_digits=15, decimal_places=2)
    total_profit = models.DecimalField(max_digits=15, decimal_places=2)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-order_date']
        indexes = [
            models.Index(fields=['order_date']),
            models.Index(fields=['country']),
            models.Index(fields=['item_type']),
            models.Index(fields=['sales_channel']),
            models.Index(fields=['region']),
        ]
    
    def __str__(self):
        return f"{self.order_id} - {self.item_type}"