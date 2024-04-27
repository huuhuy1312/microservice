from django.db import models


# Create your models here.
class Mobile(models.Model):
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255, null=False)
    slug = models.SlugField(
        max_length=255,
        unique=True,
        help_text="Unique value for mobile page URL, created from name.",
    )
    price = models.DecimalField(max_digits=9, decimal_places=2)
    quantity = models.IntegerField()
    image = models.CharField(max_length=255)
    description = models.TextField()
    is_bestseller = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "mobiles"

    def __str__(self):
        return self.name
