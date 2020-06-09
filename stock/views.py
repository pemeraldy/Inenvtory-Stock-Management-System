from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def home(request):
    products = Product.objects.all()
    orders = Order.objects.all()
    return render(request, 'stock/dashboard.html', {'products':products, 'orders':orders})
