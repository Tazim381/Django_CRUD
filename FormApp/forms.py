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
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter your full name'}),
            'roll': forms.TextInput(attrs={'placeholder': 'Enter your roll number'}),  # Using TextInput for CharField
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email address'}),
            # EmailField uses EmailInput widget
            'department': forms.TextInput(attrs={'placeholder': 'Enter your department'}),
        }


class StudentUpdateForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'roll', 'email', 'department']
