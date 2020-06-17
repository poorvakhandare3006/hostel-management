from django.db import models


# Create your models here.
class Gatepass(models.Model):
    gatepass_id = models.AutoField
    student_name = models.CharField(max_length=50)
    student_email = models.EmailField(max_length=254)
    hostel = models.CharField(max_length=3)
    date_out = models.DateField()
    date_in = models.DateField()
    reason = models.CharField(max_length=300)
    address = models.CharField(max_length=3000)
    s_contact = models.CharField(max_length=9999999999)
    p_contact = models.CharField(max_length=9999999999)
    items = models.CharField(max_length=400)
    date_time = models.DateTimeField(auto_now_add=True) 






