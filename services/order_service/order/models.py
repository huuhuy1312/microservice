from django.db import models


# Create your models here.
class Order(models.Model):
    cart_id = models.CharField(max_length=255)
    total = models.DecimalField(max_digits=9, decimal_places=2)
    status = models.IntegerField(default=0, auto_created=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "orders"
