from django.shortcuts import render
from django.http import HttpResponse
def abc(request):
    return HttpResponse("aaaaaaaaaaaaaaaaaaaaaaaaaaa")
def signin(request):
    return render(request, "signin.html")
def base(request):
    return render(request, "base.html")
def home(request):
    return render(request, "home.html")
def index(request):
    return render(request, "index.html")

# Create your views here.
