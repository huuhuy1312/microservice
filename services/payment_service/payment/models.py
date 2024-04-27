from django.db import models


# Create your models here.
class Payment(models.Model):
    ### The following are the fields of our table.
    user_id = models.CharField(max_length=255)
    order_id = models.CharField(max_length=255)
    subtotal = models.DecimalField(max_digits=9, decimal_places=2)
    total = models.DecimalField(max_digits=9, decimal_places=2)
    payment_mode = models.CharField(max_length=255)
    tel = models.CharField(max_length=10)
    status = models.BooleanField(default=False, auto_created=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s %s %s %s %s %s %s " % (
            self.user_id,
            self.order_id,
            self.subtotal,
            self.total,
            self.payment_mode,
            self.tel,
            self.status,
        )

    class Meta:
        db_table = "payments"
