# Django
from django.contrib import admin

# First Party
from service.models import Order, Product, Table


class ProductAdmin(admin.ModelAdmin):
    models = Product
    list_display = ("id", "name", "created", "last_updated")


class TableAdmin(admin.ModelAdmin):
    models = Table
    list_display = ("id", "created", "last_updated")


class OrderAdmin(admin.ModelAdmin):
    models = Order
    list_display = ("id", "created", "last_updated")


admin.site.register(Product, ProductAdmin)
admin.site.register(Table, TableAdmin)
admin.site.register(Order, OrderAdmin)
