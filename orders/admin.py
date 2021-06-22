# Django
from django.contrib import admin

# First Party
from orders.models import Category, Order, Product, Table

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Table)
admin.site.register(Order)
