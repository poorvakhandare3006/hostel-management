from django.shortcuts import render
from django.http import HttpResponse
from .forms import RegistrationForm, LoginForm
from .models import Register


# Create your views here.
def index(request):
    return render(request,'faculty/index.html')
def register(request):
    if request.method=="POST":
        student_name = request.POST.get('name', '')
        student_email = request.POST.get('email', '')
        hostel = request.POST.get('email', '')
        date_in = request.POST.get('dateto', '')
        address = request.POST.get('address', '')
        s_contact = request.POST.get('scontact', '')
        p_contact = request.POST.get('pcontact', '')
        image = request.POST.get('image','')
        enrollment_no = request.POST.get('rollno','')
        gender = request.POST.get('gender','')
        room_no = request.POST.get('roomno','')
        course = request.POST.get('course','')

        register = Register( student_name=student_name, gender=gender, date_in= date_in, student_email=student_email, hostel=hostel, enrollment_no=enrollment_no,
         address=address,s_contact=s_contact,p_contact=p_contact,image=image, room_no=room_no, course=course )
        register.save()
        thank = True
        return render(request, 'faculty/register.html',{'thank':thank})
    else:
        return render(request,"faculty/register.html")


def login(request):
    return HttpResponse("login")
    # if request.method == 'POST':
    #     form = LoginForm(request.POST)
    #     return HttpResponse("login")
    # else:
    #     form = LoginForm()
    #     return render(request, 'login.html', {'form': form})
      

def logout(request):
    return HttpResponse("logout")        