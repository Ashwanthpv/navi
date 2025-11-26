from django.db import models
from products.models import Product

class Client(models.Model):
    ORDER_STATUS_CHOICES = [
        ('order_confirmed', 'Order Confirmed'),
        ('waiting_for_order', 'Waiting for Order'),
        ('meet_direct', 'Meet Direct'),
        ('others', 'Others'),
    ]
    
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    company = models.CharField(max_length=200, blank=True)
    industry = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=200, blank=True)
    client_value = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    product_description = models.TextField(blank=True, null=True)
    order_status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES, default='waiting_for_order')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
