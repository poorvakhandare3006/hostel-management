from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path("",views.index,name="studenthome"),
    path("gatepass/",views.gatepass,name="gatepass"),
    path("login/",views.login,name="login"),



]
