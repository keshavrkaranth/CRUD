from django import forms
from django.core.exceptions import ValidationError
from .models import *


class studentReg(forms.ModelForm):
    class Meta():
        model = Student
        fields = "__all__"
        widgets = {
            'Name': forms.TextInput(attrs={'class': 'form-control'}),
            'Course': forms.TextInput(attrs={'class': 'form-control'}),
            'Phone_no': forms.TextInput(attrs={'class': 'form-control'}),
            'FatherName': forms.TextInput(attrs={'class': 'form-control'})
        }


