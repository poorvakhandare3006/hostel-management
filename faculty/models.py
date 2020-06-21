from django.db import models


# Create your models here.
gender_choices = [('M', 'Male'), ('F', 'Female')]

class Register(models.Model):
    register_id = models.AutoField
    student_name = models.CharField(max_length=50, null=True)
    student_email = models.EmailField(max_length=254,default="pk@pk.com")
    student_password = models.CharField(max_length=50, null=True)
    enrollment_no = models.CharField(max_length=10, unique=True, null=True)
    hostel_name = models.CharField(max_length=10, null=True)
    course = models.CharField(max_length=20, null=True)
    room_no = models.CharField(max_length=5, null=True)
    gender = models.CharField(
        choices=gender_choices,
        max_length=1,
        default=None,
        null=True)
    address = models.CharField(max_length=3000, null=True)
    s_contact = models.CharField(max_length=9999999999, null=True)
    p_contact = models.CharField(max_length=9999999999, null=True)
    image = models.ImageField(upload_to='student/images', default="")
    date_in = models.DateTimeField(null=True)
     






 