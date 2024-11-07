from django import forms
from django.contrib.auth.models import User
from .models import Attendance
from .models import Student

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'student_id', 'course', 'email']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match")

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['course', 'course_unit', 'duration']  
