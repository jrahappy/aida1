from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Product


def list(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'products/list.html', context)
