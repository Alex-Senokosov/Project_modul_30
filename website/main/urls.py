from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name="home"),
    path('DZ/',views.DZ,name="DZ1"),
    path('about/',views.about,name="about"),
    path ("DZ2/",views.DZ2,name="DZ2"),
    path("DZ3/", views.DZ3,name="DZ3"),
    path("DZ3X/", views.DZ3X,name="DZ3"),
    path("create/", views.create,name="create")

]
