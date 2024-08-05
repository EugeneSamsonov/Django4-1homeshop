from django.contrib import admin

# Register your models here.
from carts.models import Cart


class CartTabAdmin(admin.TabularInline):
    model = Cart
    fields = "product", "quantity", "created_timestamp"
    search_fielsd = "product", "quantity", "created_timestamp"
    readonly_fields = ("created_timestamp",)
    extra = 1
    

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ["user_display", "product_display", "quantity"]
    list_editable = "quantity",

    list_filter = ["created_timestamp", "user", "product__name"]
    search_fields = ["user", "product"]


    def product_display(self, obj):
        return str(obj.product.name)

    def user_display(self, obj):
        if obj.user:
            return str(obj.user)
        return "Анонимный пользователь"

    # user_display and product_display alter name of columns in admin panel
    user_display.short_description = "Пользователь"
    product_display.short_description = "Товар"