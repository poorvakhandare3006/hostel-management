from django.db import models
from django.utils import timezone



# Create your models here.
class Gatepass(models.Model):
    student_name = models.CharField(max_length=50)
    student_email = models.EmailField(max_length=254,default="pk@pk.com")
    hostel = models.CharField(max_length=3,null=True)
    date_out = models.DateField()
    date_in = models.DateField()
    reason = models.CharField(max_length=300)
    address = models.CharField(max_length=3000)
    s_contact = models.CharField(max_length=9999999999)
    p_contact = models.CharField(max_length=9999999999)
    items = models.CharField(max_length=400)
    date_time = models.DateTimeField(default=timezone.now) 


<<<<<<< HEAD

class Complaint(models.Model):
 title = models.CharField(max_length=120)
 room = models.CharField(max_length=10)
 category = models.CharField(max_length=20)
 date_time  = models.DateTimeField(default=timezone.now) 
 description = models.TextField(help_text="what's the issue ...")
 
 def __str__(self):
  return self.title



=======
class Complaint(models.Model):
    student_email = models.EmailField(max_length=254,default="pk@pk.com")
    title = models.CharField(max_length=120)
    room_c = models.CharField(max_length=10,null=True)
    room = models.CharField(max_length=10)
    category = models.CharField(max_length=20)
    date_time  = models.DateTimeField(default=timezone.now) 
    description = models.TextField(help_text="what's the issue ...")

    def __str__(self):
        return self.category
>>>>>>> 33431f73677c79e488c0766a2fe6ad853d2abb5f
