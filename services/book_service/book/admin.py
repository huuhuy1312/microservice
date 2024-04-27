from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django import forms
from .models import Book


# Register your models here.
class BookAdminForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"

    def clean_price(self):
        if self.cleaned_data["price"] <= 0:
            raise forms.ValidationError("Price must be greater than zero.")
        return self.cleaned_data["price"]


class BookAdmin(admin.ModelAdmin):
    form = BookAdminForm

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
admin.site.register(Book, BookAdmin)
