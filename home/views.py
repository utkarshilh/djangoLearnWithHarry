from django.shortcuts import render, HttpResponse
from datetime import datetime

from home.models import Contact

# from django.contrib.messages import constants as messages
from django.contrib import messages
# Create your views here.


def index(request):
    # return HttpResponse("this is homepage")
    messages.success(request,"this is message")
    return render(request, 'index.html')




def aboutus(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contactus(request):
    if request.method == "POST":
        name= request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        desc = request.POST.get('desc')

        contact = Contact(name =name, email = email, phone= phone, desc = desc , date = datetime.today())
        contact.save()
        messages.success(request, 'your message has beend sent')
 
    return render(request, 'contactus.html')
