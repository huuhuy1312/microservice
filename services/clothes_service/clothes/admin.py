from django.contrib import admin
from django import forms
from .models import Clothes


# Register your models here.
class ClothesAdminForm(forms.ModelForm):
    class Meta:
        model = Clothes
        fields = "__all__"

    def clean_price(self):
        if self.cleaned_data["price"] <= 0:
            raise forms.ValidationError("Price must be greater than zero.")
        return self.cleaned_data["price"]


class ClothesAdmin(admin.ModelAdmin):
    form = ClothesAdminForm

    # sets values for how the admin site lists your books
    list_display = (
        "name",
        "price",
        "created_at",
        "updated_at",
    )
    list_display_links = ("name",)
    list_per_page = 50
    ordering = ["-created_at"]
    search_fields = ["name", "description"]
    exclude = (
        "created_at",
        "updated_at",
    )

    # sets up slug to be generated from book name
    prepopulated_fields = {"slug": ("name",)}


# registers your book model with the admin site
admin.site.register(Clothes, ClothesAdmin)
