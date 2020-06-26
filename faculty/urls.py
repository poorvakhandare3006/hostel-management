from django.contrib import admin
from django.conf.urls import url ,include
from django.urls import path
from . import views


urlpatterns = [
    path("",views.index,name="facultyhome"),
    path("register/",views.register,name="registerstudent"),
    # path("gatepass/",views.gatepass,name="gatepass"),
    # path("leave/",views.leave,name="leave"),
    # path("complaint/",views.complaint,name="complaint"),
    path("login/",views.login,name="login"),
    path("logout/",views.logout,name="logout"),
    url(r'^activatemembers/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
]
