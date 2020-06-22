from django.contrib import admin
from .models import Gatepass, Complaint

# Register your models here.

admin.site.register(Gatepass) 
admin.site.register(Complaint)