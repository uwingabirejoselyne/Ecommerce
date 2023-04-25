from django.db import models

# Create your models here.
class Product(models.Model):
    product_Id =models.CharField(max_length = 20)
    title =models.CharField(max_length = 30)
    description =models.CharField(max_length = 30)
    category=models.CharField(max_length = 30)
    image = models.ImageField(upload_to='images/')
    manufacture =models.CharField(max_length = 20)
    stock =models.CharField(max_length = 30)
    price =models.CharField(max_length = 30)
    brand=models.CharField(max_length = 30)
    discount=models.CharField(max_length = 30)
    order=models.CharField(max_length = 30)
    status_choices = ('sold','Sold'),('Available','Available')
    status = models.CharField(max_length=10, choices=status_choices, default='Available')
    
