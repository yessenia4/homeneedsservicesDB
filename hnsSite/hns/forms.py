from django import forms
from django.forms import ModelForm
from django.contrib.auth import authenticate

from localflavor.us.us_states import STATE_CHOICES
from localflavor.us.forms import *
from phone_field import PhoneField

from .models import *

class LoginUserForm(forms.ModelForm):

    class Meta:
        model = Users
        fields = ['email','password']
        widgets = {
            'email': forms.EmailInput(attrs={'class':'input', 'placeholder': 'Email'}),
            'password': forms.PasswordInput(attrs={'class':'input', 'placeholder': 'Password'}),
        }

class NewUserForm(forms.ModelForm):
    zipcode = USZipCodeField()
    phone = PhoneField(blank=True, help_text='Phone Number')

    class Meta:
        model = Users
        fields = ['firstname', 'lastname', 'email', 'password', 'dob', 'phone', 'address', 'aptnum', 'city', 'state', 'zipcode']
        widgets = {
            'firstname': forms.TextInput(attrs={'class':'input', 'placeholder': 'First Name'}),
            'lastname': forms.TextInput(attrs={'class':'input', 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class':'input', 'placeholder': 'Email'}),
            'password': forms.PasswordInput(attrs={'class':'input', 'placeholder': 'Password'}),
            'dob': forms.DateInput(attrs={'class':'input', 'placeholder': 'MM/DD/YY'}),
            'address': forms.TextInput(attrs={'class':'input', 'placeholder': 'Address'}),
            'aptnum': forms.TextInput(attrs={'class':'input', 'placeholder': 'Apt. Number'}),
            'city': forms.TextInput(attrs={'class':'input', 'placeholder': 'City'}),
            'state': USStateSelect(),
        }

class NewContractorForm(forms.ModelForm):
    ssn = USSocialSecurityNumberField()
    zipcode = USZipCodeField()
    phone = PhoneField(blank=True)

    class Meta:
        model = Contractorapplications
        fields = ['name', 'ssn', 'address', 'aptnum', 'city', 'state', 'zipcode', 'willingtravel', 'phone', 'dob', 'email', 'password']
        widgets = {
            'name': forms.TextInput(attrs={'class':'input', 'placeholder': 'Name'}),
            'address': forms.TextInput(attrs={'class':'input', 'placeholder': 'Address'}),
            'aptnum': forms.TextInput(attrs={'class':'input', 'placeholder': 'Apt. Number'}),
            'city': forms.TextInput(attrs={'class':'input', 'placeholder': 'City'}),
            'state': USStateSelect(),
            'willingtravel': forms.NumberInput(attrs={'class':'input'}),
            'dob': forms.DateInput(attrs={'class':'input', 'placeholder': 'MM/DD/YY'}),
            'email': forms.EmailInput(attrs={'class':'input', 'placeholder': 'Email'}),
            'password': forms.PasswordInput(attrs={'class':'input', 'placeholder': 'Password'}),
        }

class ContractForm(forms.ModelForm):
    servicezipcode = USZipCodeField()

    class Meta:
        model = Contracts
        fields = ['description', 'dateservice', 'starttime', 'servicezipcode', 'serviceaddress', 'serviceaptnum']
        widgets = {
            'description': forms.TextInput(attrs={'class':'input', 'placeholder': 'Description'}),
            'dateservice': forms.DateInput(attrs={'class':'input', 'placeholder': 'MM/DD/YY'}),
            'starttime': forms.TimeInput(attrs={'class':'input'}),
            'serviceaddress': forms.TextInput(attrs={'class':'input', 'placeholder': 'Address'}),
            'serviceaptnum': forms.TextInput(attrs={'class':'input', 'placeholder': 'Apt. Number'}),
        }

class NewPaymentInfoForm(forms.ModelForm):

    class Meta:
        model = Paymentinfo
        fields = ['cardtype', 'cardname', 'cardnumber', 'cvv', 'billingaddress', 'expdate']
        widgets = {
            'cardtype': forms.TextInput(attrs={'class':'input', 'placeholder': 'Card Type'}),
            'cardname': forms.TextInput(attrs={'class':'input', 'placeholder': 'Card Name'}),
            'cardnumber': forms.NumberInput(attrs={'class':'input'}),
            'cvv': forms.NumberInput(attrs={'class':'input'}),
            'billingaddress': forms.TextInput(attrs={'class':'input', 'placeholder': 'Billing Address'}),
            'expdate': forms.DateInput(attrs={'class':'input', 'placeholder': 'MM/YY'}),
        }

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['number_rating', 'title', 'comments']
        widgets = {
            'number_rating': forms.Select(choices={1, 2, 3, 4, 5}),
            'title': forms.TextInput(attrs={'class':'input', 'placeholder': 'Title'}),
            'comments': forms.TextInput(attrs={'class':'input', 'placeholder': 'Comments'}),
        }