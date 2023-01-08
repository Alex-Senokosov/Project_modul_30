from django.shortcuts import render
from django.http import HttpResponse
def index (request):
    return HttpResponse("<h4>Hello<h4>")
def DZ (request):
    return HttpResponse("<h4>ДЗ-готово<h4>")
