from django.shortcuts import render
from django.http import HttpResponse
from app1 import views
def index(request):
    return HttpResponse("<h2>welcome to index page</h2>")
# Create your views here.
def sam1(request):
    return render(request,"appp1/sample1.html")
