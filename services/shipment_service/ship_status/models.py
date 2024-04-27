from __future__ import unicode_literals
from django.db import models

# Create your models here.
class shipment(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    mobile = models.CharField(max_length=10)
    address = models.CharField(max_length=255)
    product_id = models.CharField(max_length = 10)
    quantity = models.CharField(max_length = 5)
    payment_status = models.CharField(max_length = 15)
    transaction_id = models.CharField(max_length = 5)
    shipment_status = models.CharField(max_length =20)

    def __str__(self):
        return '%s %s %s %s %s %s %s %s %s %s' % (self.first_name, self.last_name, self.email, self.mobile, self.product_id, self.address, self.quantity , self.payment_status, self.transaction_id, self.shipment_status)