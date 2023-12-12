from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.http import HttpResponseRedirect
from .models import Product, Category
from .forms import CategoryForm, ProductForm


def products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})


def product_view(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'product_view.html', {'product': product})


def category_add_view(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('products'))
    else:
        form = CategoryForm()
    return render(request, 'category_add_view.html', {'form': form})

from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.http import HttpResponseRedirect
from .models import Product, Category
from .forms import CategoryForm, ProductForm


def products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})


def product_view(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'product_view.html', {'product': product})


def category_add_view(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('products'))
    else:
        form = CategoryForm()
    return render(request, 'category_add_view.html', {'form': form})


def product_add_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        form = ProductForm()
        context = {
            'categories': categories,
            'form': form
        }
        return render(request, 'product_add_view.html', context)
    elif request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products')
        else:
            categories = Category.objects.all()
            context = {
                'categories': categories,
                'form': form
            }
            return render(request, 'product_add_view.html', context)



