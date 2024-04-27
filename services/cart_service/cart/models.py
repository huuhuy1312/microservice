from django.db import models


# Create your models here.
class Cart(models.Model):
    user_id = models.CharField(max_length=255)
    status = models.BooleanField(default = False, auto_created = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "carts"
