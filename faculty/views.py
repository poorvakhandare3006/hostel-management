from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from .models import UserProfile

# from django.core.mail import EmailMessage
# from django.utils.encoding import force_bytes, force_text
# from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
# from .tokens import account_activation_token
# #from .token import forgot_password_token
# from django.template.loader import render_to_string
# from django.contrib.auth import authenticate, login ,logout
# from django.contrib.auth.decorators import login_required
# #from dateutil import parser
# from django.urls import reverse
# from django.contrib.auth.decorators import login_required
# from .task import send_verification_email
# from django import template
#from .forms import RegistrationForm, LoginForm


# Create your views here.
def index(request):
    return render(request,'faculty/index.html')
def register(request):
    if request.method=="POST":
        student_name = request.POST.get('name', '')
        student_email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        hostel = request.POST.get('hostel', '')
        address = request.POST.get('address', '')
        s_contact = request.POST.get('scontact', '')
        p_contact = request.POST.get('pcontact', '')
        image = request.POST.get('image','')
        enrollment_no = request.POST.get('enroll','')
        gender = request.POST.get('gender','')
        room_no = request.POST.get('room','')
        course = request.POST.get('course','')
        roll_no = request.POST.get('roll','')
        user = User.objects.create_user(username=student_email,email=student_email,password=password,first_name=student_name)
        profile = user.userprofile
        profile.hostel=hostel
        profile.address=address
        profile.contact=s_contact
        profile.p_contact=p_contact
        profile.image=image
        profile.enroll=enrollment_no
        profile.gender=gender
        profile.room=room_no
        profile.applied_for_member=True
        profile.student=True
        profile.course=course
        profile.roll=roll_no
        profile.save()
        user.save()
        thank = True
        # mail_subject = 'IIITM Hostel Management'
        # message=render_to_string('membership_apply.html',{'user': user,'reference_name' : student_name ,'domain': '127.0.0.1:8000','uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),'token': account_activation_token.make_token(user),})
        # email=EmailMessage(mail_subject,message,to=['poorvakhandare1999@gmail.com'])
        # email.send()
        return render(request, 'faculty/register.html',{'thank':thank})
    else:
        return render(request,"faculty/register.html")
def member_activate(request, uidb64, token):
	try:
		uid = force_text(urlsafe_base64_decode(uidb64))
		user = User.objects.get(pk=uid)
	except(TypeError, ValueError, OverflowError, User.DoesNotExist):
		user = None
	if user is not None and account_activation_token.check_token(user, token):
		profile = user.userprofile
		profile.is_member = True

		profile.save()
		return HttpResponse('Thank you for your confirmation')
	else:
		return HttpResponse('link is invalid! or You have already confirmed!!')



        