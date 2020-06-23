
from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib.auth import authenticate
from django.contrib.auth import login as loginn
from django.contrib.auth import logout as logout_view
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage

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
        user.is_active = False
        user.save()
        thank = True
        # mail_subject = 'IIITM Hostel Management'
        # message=render_to_string('faculty/register_apply.html',{'user': user,'reference_name' : student_name ,'domain': '127.0.0.1:8000','uid': force_text(urlsafe_base64_encode(force_bytes(user.pk))),'token': account_activation_token.make_token(user),})
        # to_email = student_email
        # email=EmailMessage(mail_subject,message,to=['poorvakhandare1999@gmail.com'])
        # email.send()
        #return HttpResponse('Please confirm your email address to complete the registration')
        return render(request, 'faculty/register.html',{'thank':thank})
    else:
        return render(request,"faculty/register.html")
def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        profile = user.userprofile
        profile.is_member = True
        profile.save()
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')
def login(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            loginn(request, user)
            return redirect("studenthome")
        else:
            return render(request,"faculty/login.html")
    else:
        return render(request,"faculty/login.html")
@login_required
def logout(request):
    logout_view(request)
    return redirect("facultyhome")

        