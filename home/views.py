from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    context = {
        'variable1': "Hello I am Utkarsh",
        "variable2": "This is an example of variable2"
    }
    # return HttpResponse("this is homepage")
    return render(request, 'index.html', context)


def about(request):
    return HttpResponse("this is about page")


def services(request):
    return HttpResponse("this is services page")


def contacts(request):
    return HttpResponse("this is contact page")
