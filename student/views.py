from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Gatepass, Complaint, Leave
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as loginn
from django.contrib.auth import logout as logout_view
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from .forms import ComplaintForm
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User



# Create your views here.
def index(request):
    return render(request,"student/index.html")

  
@csrf_protect 
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
                if(request.user.userprofile.student==True):
                    loginn(request, user)
                    return redirect("studenthome")
                else:
                    return render(request,'student/error_page.html')
        else:
            return render(request,"student/login.html")
    else:
        return render(request,"student/login.html")

@login_required
def logout(request):
    if(request.user.userprofile.student==True):
        logout_view(request)
        return redirect("studenthome")
    else:
        return render(request,'student/error_page.html')

@login_required
def complaint(request):
    if(request.user.userprofile.student==True):
        if request.method=="POST":
            student_name = request.user.username
            room = request.user.userprofile.room
            room_c = request.POST.get('room', '')
            category = request.POST.get('category', '')
            title = request.POST.get('title', '')
            description = request.POST.get('description', '')
            status = request.POST.get('status', '')
            complaint = Complaint(student_name=student_name, room=room, room_c=room_c, category=category, title=title, description=description, status=status  )
            complaint.save()
            thank = True
            return render(request,"student/index.html", {'thank':thank})
        else:
            return render(request,"student/complaint.html")
    else:
        return render(request,'student/error_page.html')


@login_required
def gatepass(request):
    if(request.user.userprofile.student==True):
        if request.method=="POST":
            student_name = request.user.userprofile.first_name
            student_email = request.user.email
            hostel = request.user.userprofile.hostel
            date_out = request.POST.get('datefrom', '')
            date_in = request.POST.get('dateto', '')
            room = request.user.userprofile.room
            reason = request.POST.get('reason', '')
            address = request.POST.get('address', '')
            s_contact = request.POST.get('scontact', '')
            p_contact = request.POST.get('pcontact', '')
            items = request.POST.get('items', '')
            status = request.POST.get('status', '')
            gatepass = Gatepass(student_email=student_email,hostel=hostel,student_name=student_name, date_out=date_out, date_in= date_in,reason=reason,
                address=address,s_contact=s_contact,p_contact=p_contact,items=items ,  status=status )
            gatepass.save()
            thank = True
            return render(request,"student/index.html", {'thank':thank})
        else:
            return render(request,"student/gatepass.html")
        #  return redirect('studenthome')
    else:
        return render(request,'student/error_page.html')


@login_required
def leave(request):
    if request.method=="POST":
        student_name = request.POST.get('name', '')
        student_email = request.user.email
        hostel = request.user.userprofile.hostel
        room = request.user.userprofile.room
        room_c = request.POST.get('room', '')
        date_out = request.POST.get('datefrom', '')
        date_in = request.POST.get('dateto', '')
        reason = request.POST.get('reason', '')
        address = request.POST.get('address', '')
        s_contact = request.POST.get('scontact', '')
        p_contact = request.POST.get('pcontact', '')
        status = request.POST.get('status', '')
        gatepass = Gatepass(student_email=student_email,hostel=hostel,student_name=student_name, date_out=date_out, date_in= date_in,
            reason=reason,address=address,s_contact=s_contact,p_contact=p_contact, status=status )
        gatepass.save()
        thank = True
        return render(request,"student/index.html", {'thank':thank})
    else:
        return render(request,"student/leave.html")
      #  return redirect('studenthome')     



@login_required
def change_password(request):
    if(request.user.userprofile.student==True):
        if request.method=="POST":
                username = request.user.username
                current_password = request.POST.get('password', '')
                new_password1 = request.POST.get('n_password1', '')
                new_password2 = request.POST.get('n_password2', '')
                user1 = authenticate(username=username, password=current_password)
                if user1 is not None:
                    u = User.objects.get(username=username)
                    u.set_password(new_password1)
                    u.save()
                    userr = authenticate(request, username=username, password=new_password1)
                    loginn(request, userr)
                    pass_set = True
                    return render(request,"student/index.html",{'pass_set':pass_set})


                else:
                    current_pass = True
                    return render(request,"student/change_password.html",{'c_pass':current_pass})
        else:
            return render(request,"student/change_password.html")
    else:
        return render(request,'student/error_page.html')

@login_required
def show_complaint(request):    
    student_name = request.user.username
    room = request.user.userprofile.room
    sc = Complaint.objects.filter(student_name=student_name, room=room)
    return render(request, 'student/show_complaints.html', {'sc': sc})

@login_required
def show_gatepass(request):
    student_name = request.user.username
    room = request.user.userprofile.room
    sg = Gatepass.objects.filter(student_name=student_name, room=room)
    return render(request, 'student/show_gatepass.html', {'sg': sg})


def disable_complaint(request, pk):
    comp = get_object_or_404(Complaint, pk=pk)
    comp.status = 'Disable' if comp.status == 'Active' else 'Active'
    comp.save(update_fields=['status'])
    messages.success(request, 'Complaint for title {} is {} successfully!!..' .format(comp.title, comp.status))
    
    return redirect( 'show_complaint')