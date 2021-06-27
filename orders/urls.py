# Django
from django.urls import path

# First Party
from orders import views
from orders.apps import OrdersConfig

app_name = OrdersConfig.name
urlpatterns = [
    path("", views.index, name="orders"),
]
