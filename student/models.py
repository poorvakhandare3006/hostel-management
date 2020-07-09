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
    roll = models.CharField(max_length=20,null=True)
    date_out = models.DateField()
    date_in = models.DateField()
    room = models.CharField(max_length=10,null=True)
    reason = models.CharField(max_length=300)
    address = models.CharField(max_length=3000)
    s_contact = models.CharField(max_length=9999999999)
    p_contact = models.CharField(max_length=9999999999, default="9999999999" )
    items = models.CharField(max_length=400)
    date_time = models.DateTimeField(default=timezone.now) 
    approved_supervisor = models.BooleanField(default=False)
    approved_supervisor_date_time = models.DateTimeField(null=True)
    approved_supervisor_email = models.EmailField(max_length=254,default="supervisor@pk.com")
    approved_guard = models.BooleanField(default=False)
    approved_guard_date_time = models.DateTimeField(null=True)
    approved_guard_email = models.EmailField(max_length=254,default="guard@pk.com")
    approved_control_room = models.BooleanField(default=False)
    approved_control_room_date_time = models.DateTimeField(null=True)
    approved_control_room_email = models.EmailField(max_length=254,default="cr@pk.com")
    active = models.BooleanField(default=True)
    left_gate = models.BooleanField(default=False)


    def __str__(self):
        return self.roll

class Complaint(models.Model):
    student_name = models.CharField(max_length=254, default="name")
    title = models.CharField(max_length=120)
    room_c = models.CharField(max_length=10,null=True)
    room = models.CharField(max_length=10,null=True)
    category = models.CharField(max_length=20)
    date_time  = models.DateTimeField(default=timezone.now) 
    description = models.TextField(help_text="what's the issue ...")
    active_complaint = models.BooleanField(default=True)
    work_guard = models.BooleanField(default=False)
    work_student = models.BooleanField(default=False)

    def __str__(self):
        return self.student_name
    



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
