from django.contrib import admin
from .models import *


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','product_Id','title','description','category','image','manufacture','stock','price','brand','discount','order','status')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','category_Id','category_title','slug','category_image','category_description',)


admin.site.register(Product,ProductAdmin)
admin.site.register(Category,CategoryAdmin)



