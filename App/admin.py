from django.contrib import admin
from .models import *


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','product_Id','title','description','category','image','manufacture','stock','price','brand','discount','order','status')

admin.site.register(Product,ProductAdmin)


