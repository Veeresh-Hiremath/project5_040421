from django.shortcuts import render
from django.http import HttpResponse
from app2 import views

def index(request):
    return HttpResponse("<h2>welcome to index2 page</h2>")
def sam2(request):
    return render(request,"appp2/sample2.html")
