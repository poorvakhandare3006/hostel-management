from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path("",views.index,name="facultyhome"),
    path("register/",views.register,name="registerstudent"),

]
