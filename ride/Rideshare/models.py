from django.db import models

# Create your models here.
class Ride(models.Model):
    STATUS_CHOISE=(
        ('pending','pending'),
        ('ongoing','ongoing'),
        ('completed','completed'),
        ('cancelled','cancelled'),
    )
    rider=models.CharField(max_length=255)
    driver=models.CharField(max_length=255)
    pickup_location=models.CharField(max_length=300)
    drop_location=models.CharField(max_length=300)
    status=models.CharField(max_length=200, choices=STATUS_CHOISE, default='pending')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    completed=models.BooleanField(default=False)
