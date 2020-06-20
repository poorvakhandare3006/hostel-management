from django.db import models
from django.utils import timezone



# Create your models here.
class Gatepass(models.Model):
    gatepass_id = models.AutoField
    student_name = models.CharField(max_length=50)
    student_email = models.EmailField(max_length=254,default="pk@pk.com")
    hostel = models.CharField(max_length=3,default="H")
    date_out = models.DateField()
    date_in = models.DateField()
    reason = models.CharField(max_length=300)
    address = models.CharField(max_length=3000)
    s_contact = models.CharField(max_length=9999999999)
    p_contact = models.CharField(max_length=9999999999)
    items = models.CharField(max_length=400)
    date_time = models.DateTimeField(default=timezone.now) 






