from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Gatepass



# Create your views here.
def index(request):
    return render(request,"student/index.html")
def gatepass(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        thank = True
        return render(request, 'shop/contact.html',{'thank':thank})
    else:
        return render(request,"student/gatepass.html")

      #  return redirect('studenthome')