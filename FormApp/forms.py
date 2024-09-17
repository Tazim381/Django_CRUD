from django import forms
from .models import Student

class StudentModelForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name','roll','email','department']
        labels = {
            'name': 'Enter Your Name',
            'roll': 'Enter Your Roll',
            'email': 'Enter Your Email',
            'department': 'Enter Your Department',
        }

class StudentUpdateForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'roll', 'email', 'department']
