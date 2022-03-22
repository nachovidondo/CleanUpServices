from django.shortcuts import render
from .models import Services, Happy_Customer

from .forms  import Contactform
from django.shortcuts import render,reverse , redirect
from django.urls import reverse_lazy

# Create your views here.

def index(request):
    services = Services.objects.all()
    happy_customers = Happy_Customer.objects.all()
    return render (request,'index.html', {'services':services,'happy_customers' :happy_customers})

def services(request):
    services = Services.objects.all()
    
    return render (request,'services.html', {'services':services })


#Contact
def contact(request):
    contact_form = Contactform()
  
    if request.method == "POST":
        contact_form = Contactform(data=request.POST)
        if contact_form.is_valid():
            name= request.POST.get('name')
            email= request.POST.get('email')
            content= request.POST.get('content')
            """mail = EmailMessage(
                "vida Message : New Message Contact ",
                "From {} {}\n\n wrote :\n\n {}".format(name ,email,content),
                "vida.com", ["vida90@gmail.com"],-----> create a new email
                reply_to = [email]
                )"""
            try:
               """ mail.send() #Si esta todo ok redireccionar"""
               return redirect(reverse("automatic")+"?ok")



            except:
                return redirect(reverse("contact")+"?fail")

    return render (request, 'contact.html', {'form':contact_form})


#Automatic message after contact us and book us
def automatic(request):
  
    return render (request, 'automatic.html')
