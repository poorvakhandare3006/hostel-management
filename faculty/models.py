from django.db import models
import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.conf import settings
from django.utils import timezone




# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    enroll = models.CharField(max_length=10, unique=True,null=True)
    hostel = models.CharField(max_length=10,null=True)
    course = models.CharField(max_length=20,null=True)
    roll = models.CharField(max_length=20,null=True,unique=True)
    room = models.CharField(max_length=20,null=True)
    gender = models.CharField(max_length=10,null=True)
    address = models.CharField(max_length=3000, null=True)
    contact = models.CharField(max_length=9999999999, null=True)
    p_contact = models.CharField(max_length=9999999999, null=True)
    image = models.ImageField(upload_to="student/images",default="")
    student = models.BooleanField(default=False)
    warden = models.BooleanField(default=False)
    guard = models.BooleanField(default=False)
    office = models.BooleanField(default=False)
    applied_for_member = models.BooleanField(default=False)
    is_member = models.BooleanField(default=False)
    date_time = models.DateTimeField(default=timezone.now) 

    



def create_user_profile(sender, instance, created, **kwargs):
	if created:
	   profile, created = UserProfile.objects.get_or_create(user=instance)
	   # profile, created = Booking.objects.get_or_create(user=instance)

post_save.connect(create_user_profile, sender=User)





 