from django.shortcuts import render
from .models import *
import random


# Create your views here.
def Home(request):
    data = Product.objects.all()
    return render(request,'index.html',{'data':data})

def Dashboard(request):

    return render(request,'admin/dashboard.html')


def BaseDashboard(request):

    return render(request,'admin/dashboard1.html')


def addProduct(request):
    Categories(request)
    cat = Category.objects.all()
    print(cat)
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
        
    return render(request,'admin/add_product.html',{'cat':cat})


def Categories(request):
    if request.method == "POST":
        categoryid = random.random()
        category_title =request.POST['category-title']
        slug=request.POST['slug']
        category_image=request.POST['category-image']
        category_description=request.POST['category-description']
        category=Category.objects.create(
        category_Id =categoryid,
        category_title =category_title,
        slug =slug,
        category_image= category_image,
        category_description = category_description,

        )
        category.save()
    return render(request,'admin/categories.html')






