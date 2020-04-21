from django import forms
from django.forms import ModelForm

from .models import *

class LoginUserForm(forms.ModelForm):

    class Meta:
        model = Users
        fields = ['email','password']
        widgets = {
            'email': forms.EmailInput(attrs={'class':'input', 'placeholder': 'Email'}),
            'password': forms.TextInput(attrs={'class':'input', 'placeholder': 'Password'}),
        }