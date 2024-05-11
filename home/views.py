from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    context = {
        'variable': "this is variable comming from outside"
    }
    # return HttpResponse("this is homepage")
    return render(request, 'index.html')


def about(request):
    return HttpResponse("this is about page")


def services(request):
    return HttpResponse("this is services page")


def contacts(request):
    return HttpResponse("this is contact page")
