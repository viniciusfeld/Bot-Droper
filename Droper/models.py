from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=False, null=True)
    name = models.CharField(max_length=64)
    size = models.CharField(max_length=32)
    current_price = models.DecimalField(max_digits=5, decimal_places=2)
    min_price = models.DecimalField(max_digits=5, decimal_places=2)
    user = models.ForeignKey(User, verbose_name="relation users", on_delete=models.DO_NOTHING)
    created_by_id = models.BigIntegerField(null=True)
    updated_by_id = models.BigIntegerField(null=True)