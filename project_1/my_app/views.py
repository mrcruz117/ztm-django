from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("Hello, world.")

def about(request):
    return HttpResponse("About me.")

def hello(request, first_name):
    return HttpResponse(f"Hello, {first_name}.")