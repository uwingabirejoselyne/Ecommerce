from django.shortcuts import render
from .models import *
import random


# Create your views here.
def Home(request):

    return render(request,'index.html')

def Dashboard(request):

    return render(request,'admin/dashboard.html')


def BaseDashboard(request):

    return render(request,'admin/dashboard1.html')


def addProduct(request):
    if request.method == 'POST':
        productid = random.random()
        title=request.POST['title']
        description=request.POST['description']
        category=request.POST['category']
        image=request.POST['image']
        manufacture=request.POST['manufacture']
        stock=request.POST['stock']
        price=request.POST['price']
        brand=request.POST['brand']
        discount=request.POST['discount']
        order=request.POST['order']
        products=Product.objects.create(
        product_Id =productid,
        title =title,
        description =description,
        category = category,
        image = image,
        manufacture = manufacture,
        stock = stock,
        price = price,
        brand = brand,
        discount = discount,
        order = order,
        )
        products.save()
    return render(request,'admin/add_product.html')

