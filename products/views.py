from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from .models import Product
from .forms import ProductForm


def list(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'products/list.html', context)


def product_retrieve(request, pk):
    product = Product.objects.get(id=pk)
    context = {
        "product": product
    }
    return render(request, "products/detail.html", context)


def product_create(request):
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(False)
            product.author = request.user
            product.save()
            return redirect('products:list')

    context = {
        "form": form
    }
    return render(request, "products/create.html", context)


def product_update(request, pk):
    product = Product.objects.get(id=pk)
    form = ProductForm(instance=Post)

    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return render(request, 'products:detail', Post)

    context = {
        "form": form
    }
    return render(request, "products/update.html", context)


def product_update_done(request, pk):
    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)

    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            # form.save()
            return redirect('products:list')

    context = {
        "form": form
    }
    return render(request, "products/update.html", context)


def product_delete(request, pk):
    product = Product.objects.get(id=pk)
    product.delete()
    return redirect("products:list")
