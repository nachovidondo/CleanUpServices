from django.shortcuts import render
from .models import Portfolio, Places, Index

from .forms  import Contactform
from django.shortcuts import render,reverse , redirect
from django.urls import reverse_lazy
from django.core.mail import EmailMessage


# Create your views here.

def index(request):
 
    index = Index.objects.all()
    return render (request,'index.html', {'index':index})


#Contact
def contact(request):
    contact_form = Contactform()
  
    if request.method == "POST":
        contact_form = Contactform(data=request.POST)
        if contact_form.is_valid():
            name= request.POST.get('name')
            email= request.POST.get('email')
            content= request.POST.get('content')
            mail = EmailMessage(
                "Clean Up Service  Message : New Message Contact ",
                "From {} {}\n\n wrote :\n\n {}".format(name ,email,content),
                "cleanupservice.dk", ["ignaciovidondo@hotmail.com"],
                reply_to = [email]
                )
            try:
               mail.send() #Si esta todo ok redireccionar"""
               return redirect(reverse("automatic")+"?ok")



            except:
                return redirect(reverse("contact")+"?fail")

    return render (request, 'contact.html', {'form':contact_form})


#Automatic message after contact us and book us
def automatic(request):
  
    return render (request, 'automatic.html')


def portfolio(request):
    
    portfolio = Portfolio.objects.all()
    
    return render (request,'portfolio.html', {'portfolio':portfolio})


def places(request):
    places = Places.objects.all()
    return render (request,'pricing.html', {'places':places})