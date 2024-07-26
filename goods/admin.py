from django.contrib import admin

# Register your models here.
from goods.models import Categories, Products

# admin.site.register(Categories)
# admin.site.register(Products)

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

    list_display = ["name", "id"]
    ordering = ["name", "id"]

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

    list_display = ["name", "quantity", "price", "discount"]
    list_editable = ["discount"]
    ordering = ["name", "quantity", "price", "discount"]
    fields = [
        ("name", "slug"),
        "category", 
        "description",
        ("price", "discount", "quantity"),
        "image"
    ]

    list_filter = ["quantity", "price", "discount", "category__name"]
    search_fields = ["name", "description"]



