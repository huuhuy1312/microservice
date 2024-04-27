from django.db import models
from cart.models import Cart


# Create your models here.
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    category_id = models.CharField(max_length=50, unique=False, blank=False, null=False)
    product_id = models.CharField(max_length=50, unique=False, blank=False, null=False)
    quantity = models.IntegerField(default=1, unique=False, blank=False, null=False)

    class Meta:
        db_table = "cart_items"

    def augment_quantity(self, quantity):
        self.quantity = self.quantity + int(quantity)
        self.save()
