from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('products/', views.products, name="products"),
    path('create-product/', views.createProduct, name="createProduct"),
    path('edit-product/<str:pk>/', views.editProduct, name="editProduct" )
    
]