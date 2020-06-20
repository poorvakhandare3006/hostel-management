from django.db import models


# Create your models here.
class Register(models.Model):
    register_id = models.AutoField
    student_name = models.CharField(max_length=50)
    student_email = models.EmailField(max_length=254)
    student_password = models.CharField(max_length=50)
    hostel = models.CharField(max_length=3)
    image = models.ImageField(upload_to='student/images', default="")
    date_in = models.DateTimeField(auto_now_add=True)
     






