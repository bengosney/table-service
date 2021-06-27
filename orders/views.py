# Create your views here.
# Django
from django.shortcuts import render


def index(request):
    context = {}

    return render(request, "orders/index.html", context)
