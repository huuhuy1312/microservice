from __future__ import unicode_literals
from django.db import models


# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    mobile = models.CharField(max_length=10)
    password = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.email} {self.mobile} {self.password} {self.address} {self.role}'
    
    class Meta:
        db_table = 'users' 