from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.db.models import Q

from .models import Product
from .forms import ProductForm
from django.core.paginator import Paginator


def list(request):
    page = request.GET.get('page', '1')
    kw = request.GET.get('kw', '')
    products = Product.objects.all()
    if kw:
        products = products.filter(
            Q(name__icontains=kw)
        ).distinct()

    paginator = Paginator(products, 5)
    page_obj = paginator.get_page(page)

    context = {
        'products': page_obj,
        'page': page,
        'kw': kw
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
    form = ProductForm(instance=product)

    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products:detail', product.id)

    context = {
        "form": form
    }
    return render(request, "products/update.html", context)


def product_delete(request, pk):
    product = Product.objects.get(id=pk)
    product.delete()
    return redirect("products:list")


def product_delete_confirm(request, pk):
    product = Product.objects.get(id=pk)
    context = {
        "product": product
    }
    return render(request, "products/delete_confirm.html", context)
