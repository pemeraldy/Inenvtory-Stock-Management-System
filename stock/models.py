from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=50, null= True)
    comp_name = models.CharField(max_length=50, null=True,blank=True)
    email = models.CharField(max_length=200, null= True)
    phone = models.CharField(max_length=200, null= True)
    address = models.CharField(max_length=200, null= True)
    date_created = models.DateTimeField(auto_now_add=True, null= True)

    def __str__ (self):
        return self.name +" "+ self.comp_name

class Vendor(models.Model):
    name = models.CharField(max_length=50, null= True)
    email = models.CharField(max_length=200, null= True)
    phone = models.CharField(max_length=200, null= True)
    address = models.CharField(max_length=200, null= True)
    date_created = models.DateTimeField(auto_now_add=True, null= True)
    def __str__ (self):
        return self.name + " "+ self.address

class Product(models.Model):
    STATUS = (
        ('Incoming', 'Incoming'),
        ('Outgoing', 'Outgoing'),
        ('Available', 'Available')
    )
    name = models.CharField(max_length=200, null= True)
    price = models.FloatField()
    description = models.CharField(max_length=200, null= True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null= True)
    stock_quantity  = models.IntegerField()
    status = models.CharField(max_length=20, null=True, choices=STATUS)
    vendor = models.ForeignKey(Vendor,null=True, on_delete=models.SET_NULL)
    def __str__ (self):
        return self.name + " "+ self.status 
        
class Order(models.Model):
    STATUS = (
        ('Pending','Pending'),
        ('Delivered', 'Delivered'),
    )
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    quantity = models.IntegerField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null= True)

    status = models.CharField(max_length=20, null=True, choices=STATUS)

    def __str__ (self):
        return self.customer 
