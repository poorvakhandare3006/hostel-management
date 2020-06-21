from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path("",views.index,name="facultyhome"),
    path("register/",views.register,name="registerstudent"),
    path("login/",views.login, name="login"),
    path('logout/', views.logout, name='logout')

]
