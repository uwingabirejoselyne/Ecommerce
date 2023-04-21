from django.shortcuts import render
from .models import *

# Create your views here.
def Home(request):

    return render(request,'index.html')

def Dashboard(request):

    return render(request,'admin/dashboard.html')