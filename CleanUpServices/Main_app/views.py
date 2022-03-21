from django.shortcuts import render
from .models import Services, Happy_Customer

# Create your views here.

def index(request):
    services = Services.objects.all()
    happy_customers = Happy_Customer.objects.all()
    return render (request,'index.html', {'services':services,'happy_customers' :happy_customers})

def services(request):
    services = Services.objects.all()
    
    return render (request,'services.html', {'services':services })