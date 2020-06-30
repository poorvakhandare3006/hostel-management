from django.db import models
from django.utils import timezone

STATUS_CHOICES = (
    ('Active', 'Active'),
    ('Disable', 'Disable'),
    ('Accepted','Accepted'),
    ('Rejected','Rejected')
)


# Create your models here.
class Gatepass(models.Model):
    student_name = models.CharField(max_length=50)
    student_email = models.EmailField(max_length=254,default="pk@pk.com")
    hostel = models.CharField(max_length=3,null=True)
    date_out = models.DateField()
    date_in = models.DateField()
    room = models.CharField(max_length=10,null=True)
    reason = models.CharField(max_length=300)
    address = models.CharField(max_length=3000)
    s_contact = models.CharField(max_length=9999999999)
    p_contact = models.CharField(max_length=9999999999, default="9999999999" )
    items = models.CharField(max_length=400)
    date_time = models.DateTimeField(default=timezone.now) 
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="Active")

    def __str__(self):
        return self.room

class Complaint(models.Model):
    student_name = models.CharField(max_length=254, default="name")
    title = models.CharField(max_length=120)
    room_c = models.CharField(max_length=10,null=True)
    room = models.CharField(max_length=10,null=True)
    category = models.CharField(max_length=20)
    date_time  = models.DateTimeField(default=timezone.now) 
    description = models.TextField(help_text="what's the issue ...")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="Active")

    def __str__(self):
        return self.student_name
    
    class Meta:
        db_table = 'complaint'



class Leave(models.Model):
    student_name = models.CharField(max_length=50, default="name")
    student_email = models.EmailField(max_length=254,default="pk@pk.com")
    hostel = models.CharField(max_length=3,null=True)
    room_c = models.CharField(max_length=10,null=False)
    room = models.CharField(max_length=10,null=True)
    date_out = models.DateField()
    date_in = models.DateField()
    reason = models.CharField(max_length=300)
    address = models.CharField(max_length=3000)
    s_contact = models.CharField(max_length=9999999999)
    p_contact = models.CharField(max_length=9999999999)
    date_time = models.DateTimeField(default=timezone.now) 
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="Active")
