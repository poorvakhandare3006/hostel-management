from .models import Register
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = [
            'student_name',
            'student_email',
            'enrollment_no',
            's_contact',
            'p_contact',
            'date_in',
            'room_no',
            'hostel_name',
            'address',
            'image',
            'course',
            'gender', ]