from django.contrib import admin
from django import forms
from .models import User

# Register your models here.
class UserAdminForm(forms.ModelForm): 
    class Meta: 
        model = User
        fields = '__all__'
    

class UserAdmin(admin.ModelAdmin):
    form = UserAdminForm 

# registers your book model with the admin site 
admin.site.register(User, UserAdmin)