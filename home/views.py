from django.shortcuts import render, HttpResponse
from datetime import datetime 
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    context={
        "variable1": "this is sent",
        "variable2": "im good"
    }
    return render(request,'index.html')
    # return HttpResponse("this is Homepage")

def about(request):
    return render(request,'about.html')
    # return HttpResponse("this is about page")

def services(request):
    return render(request,'services.html')
    # return HttpResponse("this is service page")        

def contact(request):
    if request.method=="POST":
        name=request.POST('name')
        email=request.POST('email')
        phone=request.POST('phone')
        contact=Contact.objects.create(name=name,email=email,phone=phone,date=datetime.today())
        contact.save()
        messages.success(request, 'Your Message have been sent')
    return render(request,'contact.html')
    