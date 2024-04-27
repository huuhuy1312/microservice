from django.contrib import admin
from django import forms
from .models import Category


# Register your models here.
class CategoryAdminForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"


class CategoryAdmin(admin.ModelAdmin):
    form = CategoryAdminForm

    # sets values for how the admin site lists your books
    list_display = (
        "name",
        "created_at",
        "updated_at",
    )
    list_display_links = ("name",)
    list_per_page = 50
    ordering = ["-created_at"]
    search_fields = ["name"]
    exclude = (
        "created_at",
        "updated_at",
    )

    # sets up slug to be generated from book name
    prepopulated_fields = {"slug": ("name",)}


# registers your book model with the admin site
admin.site.register(Category, CategoryAdmin)
