from django.shortcuts import render
from django.http import HttpResponse
def index (request):
    return render(request,"main/index.html")
def DZ (request):
    return HttpResponse("<h4>ДЗ-готово<h4>")
def about (request):
    return render(request,"main/about.html")
def DZ2 (request):
    return render(request,"DZ2.html")

def DZ3 (request):
    return render(request,"DZ3.html")

def DZ3X (request):
    return render(request,"DZ3X.html")