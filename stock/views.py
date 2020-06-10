from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import ProductForm

# Create your views here.

def home(request):
    products = Product.objects.all()
    orders = Order.objects.all()
    total_orders = orders.count()
    delivered = orders.filter(status = "Delivered").count()
    pending = orders.filter(status = "Pending").count()

    context = {'products':products, 'orders':orders,'total_orders':total_orders,'pending':pending, 'delivered':delivered}
    return render(request, 'stock/dashboard.html', context )


def products(request):
    products = Product.objects.all()
    # total_products = Product.objects.all().count
    available = products.filter(status="Available").count()
    incoming = products.filter(status="Incoming").count()
    outgoing = products.filter(status="Outgoing").count()
    context = {'available':available,'incoming':incoming,'outgoing':outgoing, 'products':products}
    return render(request, 'stock/products.html', context)



def createProduct(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        
    context ={'productForm':form}
    return render(request, 'stock/product_form.html', context)


def editProduct(request, pk):
    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)
    context ={'form': form}
    
    return render(request, 'stock/product_form.html', context)