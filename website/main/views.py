from django.shortcuts import render
from django.http import HttpResponse
from .models import Task
def index (request):
    task = Task.objects.order_by("-id")
    return render(request,"main/index.html",{"title":"Главная страница","tasks": task})

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
def create(request):
    return render(request,"main/create.html")