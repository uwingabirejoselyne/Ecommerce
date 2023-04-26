from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.urls import path

urlpatterns = [
    path('',views.Home,name='home'),
    path('dashboard',views.Dashboard,name='dashboard'),
    path('base-dashboard',views.BaseDashboard,name='base-dashboard'),
    path('addproduct',views.addProduct,name='addproduct'),
    path('category',views.Categories,name='category'),
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    