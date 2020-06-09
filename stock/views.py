from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def home(request):
    products = Product.objects.all()
    orders = Order.objects.all()
    total_orders = orders.count()
    delivered = orders.filter(status = "Delivered").count()
    pending = orders.filter(status = "Pending").count()

    context = {'products':products, 'orders':orders,'total_orders':total_orders,'pending':pending, 'delivered':delivered}
    return render(request, 'stock/dashboard.html', context )
