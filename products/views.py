from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
import csv
from .models import Product
from .forms import ProductForm

def download_products(request):
    products = Product.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="products.csv"'
    
    writer = csv.writer(response)
    writer.writerow(['ID', 'Name', 'Price', 'Description'])
    for product in products:
        writer.writerow([product.id, product.name, product.price or 0, product.description or ''])
    
    return response

def products_list(request):
    products = Product.objects.all()
    return render(request, 'products/products_list_mobile.html', {'products': products})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/products/')
    else:
        form = ProductForm()
    return render(request, 'products/add_product_mobile.html', {'form': form})

def edit_product(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('/products/')
    else:
        form = ProductForm(instance=product)
    return render(request, 'products/add_product_mobile.html', {'form': form})

def delete_product(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        product.delete()
        return redirect('/products/')
    return render(request, 'products/delete_product.html', {'product': product})
