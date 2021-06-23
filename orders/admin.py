# Django
from django.contrib import admin

# Third Party
from django_fsm_log.admin import StateLogInline
from fsm_admin.mixins import FSMTransitionMixin

# First Party
from orders.models import Category, Order, OrderLine, Product, Table


class BaseAdmin(admin.ModelAdmin):
    readonly_fields = ["created", "last_updated", "position"]


class ProductAdmin(BaseAdmin):
    model = Product
    list_display = ["name", "created", "last_updated"]


class CategoryAdmin(BaseAdmin):
    model = Category
    list_display = ["name", "created", "last_updated"]


class TableAdmin(BaseAdmin):
    model = Table


class OrderLineAdmin(admin.TabularInline):
    model = OrderLine
    readonly_fields = ["created", "last_updated", "position"]


class OrderAdmin(FSMTransitionMixin, admin.ModelAdmin):
    mode = Order
    list_display = ["created", "last_updated", "state", "table"]
    list_filter = ["state", "table"]
    readonly_fields = ["state", "created", "last_updated", "position"]
    fsm_field = ["state"]
    inlines = [OrderLineAdmin, StateLogInline]


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Table, TableAdmin)
admin.site.register(Order, OrderAdmin)
