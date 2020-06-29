from django.contrib import admin
from django.urls import path, include
from . import views

 

urlpatterns = [
    path("",views.index,name="studenthome"),          
    path("gatepass/",views.gatepass,name="gatepass"),
    path("show_gatepass/",views.show_gatepass,name="show_gatepass"),
    path("leave/",views.leave,name="leave"),
    path("login/",views.login,name="login"),
    path("logout/",views.logout,name="logout"),
    path("complaint/",views.complaint,name="complaint"),
    path("show_complaint/",views.show_complaint,name="show_complaint"),
    path("change_password/",views.change_password,name="change_password"),

]
