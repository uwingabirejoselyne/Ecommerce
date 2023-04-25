from . import views
from django.urls import path

urlpatterns = [
    path('',views.Home,name='home'),
    path('dashboard',views.Dashboard,name='dashboard'),
    path('base-dashboard',views.BaseDashboard,name='base-dashboard'),
    path('addproduct',views.addProduct,name='addproduct'),

    ]