from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Gatepass, Complaint
from django.contrib.auth import authenticate
from django.contrib.auth import login as loginn
from django.contrib.auth import logout as logout_view
from django.contrib.auth.decorators import login_required
from .forms import ComplaintForm
from django.views.generic import ListView, DetailView


# Create your views here.
def index(request):
    return render(request,"student/index.html")

def gatepass(request):
    if request.method=="POST":
        student_name = request.POST.get('name', '')
        student_email = request.user.username
        hostel = request.user.userprofile.hostel
        date_out = request.POST.get('datefrom', '')
        date_in = request.POST.get('dateto', '')
        reason = request.POST.get('reason', '')
        address = request.POST.get('address', '')
        s_contact = request.POST.get('scontact', '')
        p_contact = request.POST.get('pcontact', '')
        items = request.POST.get('items', '')
        gatepass = Gatepass(student_email=student_email,hostel=hostel,student_name=student_name, date_out=date_out, date_in= date_in,reason=reason,address=address,s_contact=s_contact,p_contact=p_contact,items=items)
        gatepass.save()
        thank = True
        return redirect("studenthome")
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

            if user.is_active:
                loginn(request, user)
                data = Complaint.objects.all()
                comp = {
                    "complaint_number": data
                }
                return render_to_response("login/index.html", compl)
            else:
                HttpResponse("Inactive User.")
                # return redirect("studenthome")
        else:
                return render(request,"student/login.html")
    else:
        return render(request,"student/login.html")

@login_required
def logout(request):
    logout_view(request)
    return redirect("studenthome")

def complaint(request):
    if request.method=="POST":
            student_email = request.user.username
            room = request.user.userprofile.room
            room_c = request.POST.get('room', '')
            category = request.POST.get('category', '')
            title = request.POST.get('title', '')
            description = request.POST.get('description', '')
            complaint = Complaint(student_email=student_email,room=room,room_c=room_c,category=category,title=title,description=description)
            complaint.save()
            thank = True
            return redirect("studenthome")
    else:
        return render(request,"student/complaint.html")

