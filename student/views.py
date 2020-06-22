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




class IndexView(ListView):
 template_name='student/index.html'
 context_object_name = 'complaint_list'
 def get_queryset(self):
  return Complaint.objects.all()

#Detail view (view post detail)
class ComplaintDetailView(DetailView):
 model=Complaint
 template_name = 'student/complaint_detail.html'

def viewcomplaint(request):
 if request.method == 'POST':
  form = ComplaintForm(request.POST)
  if form.is_valid():
   form.save()
  return redirect('index')
 form = ComplaintForm()
 return render(request,'student/index.html',{'form': form})

#create complaint
def postcomplaint(request):
 if request.method == 'POST':
  form = ComplaintForm(request.POST)
  if form.is_valid():
   form.save()
  return redirect('index')
 form = ComplaintForm()
 return render(request,'student/post_complaint.html',{'form': form})

#Delete complaint
def deletecomplaint(request, pk, template_name='del_complaint.html'):
    post= get_object_or_404(Complaint, pk=pk)    
    if request.method=='POST':
        post.delete()
        return redirect('index')
    return render(request, template_name, {'object':post})