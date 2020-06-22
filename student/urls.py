from django.contrib import admin
from django.urls import path, include
from rest_framework import routers 
from . import views

router = routers.DefaultRouter()                     
router.register(r'complaints', views.ComplaintView, 'student')   
 

urlpatterns = [
    path('admin/', admin.site.urls),           
    path('complaints/api/', include(router.urls)),  
    path("",views.index,name="studenthome"),
    path("gatepass/",views.gatepass,name="gatepass"),
    path("login/",views.login,name="login"),
    path("logout/",views.logout,name="logout"),
    path('complaints/', views.IndexView.as_view(), name='complaints'),
    path('complaints/<int:pk>/', views.ComplaintDetailView.as_view(), name='detail'),
    path("complaints/reg_complaint/",views.postcomplaint,name="post_complaint"),
    path('complaints/del_complaint/<int:pk>/', views.deletecomplaint, name='delete'),

]
