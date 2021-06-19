# Django
from django.contrib import admin

# First Party
from products.models import Category, Product

admin.site.register(Product)
admin.site.register(Category)
