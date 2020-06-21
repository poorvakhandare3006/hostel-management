from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Gatepass
from django.contrib.auth import authenticate
from django.contrib.auth import login as loginn
from django.contrib.auth import logout as logout_view
from django.contrib.auth.decorators import login_required







# Create your views here.
def index(request):
    return render(request,"student/index.html")
def gatepass(request):
    if request.method=="POST":
        student_name = request.POST.get('name', '')
        #student_email = request.POST.get('email', '')
        #hostel = request.POST.get('email', '')
        date_out = request.POST.get('datefrom', '')
        date_in = request.POST.get('dateto', '')
        reason = request.POST.get('reason', '')
        address = request.POST.get('address', '')
        s_contact = request.POST.get('scontact', '')
        p_contact = request.POST.get('pcontact', '')
        items = request.POST.get('items', '')
        gatepass = Gatepass(student_name=student_name, date_out=date_out, date_in= date_in,reason=reason,address=address,s_contact=s_contact,p_contact=p_contact,items=items)
        gatepass.save()
        thank = True
        return render(request, 'student/gatepass.html',{'thank':thank})
    else:
        return render(request,"student/gatepass.html")
      #  return redirect('studenthome')


   
def login(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            loginn(request, user)
            return redirect("studenthome")
        else:
            return render(request,"student/login.html")
    else:
        return render(request,"student/login.html")
@login_required
def logout(request):
    logout_view(request)
    return redirect("studenthome")
