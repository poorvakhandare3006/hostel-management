from django.contrib import admin
from django.urls import path, include
from . import views

 

<<<<<<< HEAD
urlpatterns = [          
    path("gatepass/",views.gatepass,name="gatepass"),
    path("login/",views.login,name="login"),
    path("logout/",views.logout,name="logout"),
    path('', views.index, name='index'),
    path("complaint/",views.postcomplaint,name="post_complaint"),
    path('del_complaint/<int:pk>/', views.deletecomplaint, name='delete'),
=======
urlpatterns = [
    path("",views.index,name="studenthome"),          
    path("gatepass/",views.gatepass,name="gatepass"),
    path("login/",views.login,name="login"),
    path("logout/",views.logout,name="logout"),
    path("complaint/",views.complaint,name="complaint"),
>>>>>>> 33431f73677c79e488c0766a2fe6ad853d2abb5f

]
