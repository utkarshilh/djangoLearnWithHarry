from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    # return HttpResponse("this is homepage")
    return render(request, 'index.html')


def aboutus(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contactus(request):
    return render(request, 'contactus.html')
