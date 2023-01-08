from django.urls import path
from .import views

urlpatterns = [
    path('',views.index),
    path('DZ/',views.DZ),
    path('about/',views.about),
    path ("DZ2/",views.DZ2)
]
