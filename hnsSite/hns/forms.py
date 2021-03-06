from django import forms
from django.forms import ModelForm
from django.contrib.auth import authenticate

from localflavor.us.us_states import STATE_CHOICES
from localflavor.us.forms import *
from phone_field import PhoneField

from .models import *

# iterable 
CARD_TYPE_CHOICES =( 
    ("VISA","VISA"), 
    ("MasterCard","MasterCard"), 
    ("Discover","Discover"), 
    ("American Express","American Express"),
)

class LoginUserForm(forms.ModelForm):

    class Meta:
        model = Users
        fields = ['email','password']
        widgets = {
            'email': forms.EmailInput(attrs={'class':'input', 'placeholder': 'Email', 'maxlength': '100',}),
            'password': forms.PasswordInput(attrs={'class':'input', 'placeholder': 'Password', 'maxlength': '50',}),
        }

class NewUserForm(forms.ModelForm):
    aptnum = CharField(max_length=10, help_text='Apt. Number', widget=forms.TextInput(attrs={'class':'input'}), required=False)
    #dob = DateField(help_text='MM/DD/YYYY', widget=forms.DateInput(attrs={'class':'input'}), disabled=True)
    zipcode = USZipCodeField()
    phone = PhoneField(blank=True, help_text='Phone Number')

    class Meta:
        model = Users
        fields = ['firstname', 'lastname', 'email', 'password', 'dob', 'phone', 'address', 'aptnum', 'city', 'state', 'zipcode']
        widgets = {
            'firstname': forms.TextInput(attrs={'class':'input', 'placeholder': 'First Name', 'maxlength': '20',}),
            'lastname': forms.TextInput(attrs={'class':'input', 'placeholder': 'Last Name', 'maxlength': '20',}),
            'email': forms.EmailInput(attrs={'class':'input', 'placeholder': 'Email', 'maxlength': '100',}),
            'password': forms.PasswordInput(attrs={'class':'input', 'placeholder': 'Password', 'maxlength': '50',}, render_value=True),
            'dob': forms.DateInput(attrs={'class':'input', 'placeholder': 'YYYY/MM/DD'}),
            'address': forms.TextInput(attrs={'class':'input', 'placeholder': 'Address', 'maxlength': '150',}),
            'city': forms.TextInput(attrs={'class':'input', 'placeholder': 'City', 'maxlength': '50',}),
            'state': USStateSelect(),
        }

class NewContractorForm(forms.ModelForm):
    ssn = USSocialSecurityNumberField()
    zipcode = USZipCodeField()
    phone = PhoneField(blank=True, help_text='Phone Number')
    aptnum = CharField(max_length=10, help_text='Apt. Number', widget=forms.TextInput(attrs={'class':'input'}), required=False)

    class Meta:
        model = Contractorapplications
        fields = ['name', 'ssn', 'address', 'aptnum', 'city', 'state', 'zipcode', 'willingtravel', 'phone', 'dob', 'email', 'password']
        widgets = {
            'name': forms.TextInput(attrs={'class':'input', 'placeholder': 'Name', 'maxlength': '100',}),
            'address': forms.TextInput(attrs={'class':'input', 'placeholder': 'Address', 'maxlength': '150',}),
            'city': forms.TextInput(attrs={'class':'input', 'placeholder': 'City', 'maxlength': '50',}),
            'state': USStateSelect(),
            'willingtravel': forms.NumberInput(attrs={'class':'input'}),
            'dob': forms.DateInput(attrs={'class':'input', 'placeholder': 'YYYY/MM/DD'}),
            'email': forms.EmailInput(attrs={'class':'input', 'placeholder': 'Email', 'maxlength': '100',}),
            'password': forms.PasswordInput(attrs={'class':'input', 'placeholder': 'Password', 'maxlength': '50',}, render_value=True),
        }

class ContractForm(forms.ModelForm):
    servicezipcode = USZipCodeField()
    serviceaptnum = CharField(max_length=10, help_text='Apt. Number', widget=forms.TextInput(attrs={'class':'input'}), required=False)

    class Meta:
        model = Contracts
        fields = ['description', 'dateservice', 'starttime', 'servicezipcode', 'serviceaddress', 'serviceaptnum']
        widgets = {
            'description': forms.Textarea(attrs={'class':'input', 'placeholder': 'Description', 'maxlength':'500',}),
            'dateservice': forms.DateInput(attrs={'class':'input', 'placeholder': 'YYYY-MM-DD'}),
            'starttime': forms.TimeInput(attrs={'class':'input'}),
            'serviceaddress': forms.TextInput(attrs={'class':'input', 'placeholder': 'Address', 'maxlength':'150',}),
        }

class NewPaymentInfoForm(forms.ModelForm):
    cardtype = forms.ChoiceField(choices=CARD_TYPE_CHOICES)

    class Meta:
        model = Paymentinfo
        fields = ['cardtype', 'cardname', 'cardnumber', 'cvv', 'billingaddress', 'expdate']
        widgets = {
            'cardname': forms.TextInput(attrs={'class':'input', 'placeholder': 'Card Name', 'maxlength':'150',}),
            'cardnumber': forms.NumberInput(attrs={'class':'input'}),
            'cvv': forms.NumberInput(attrs={'class':'input'}),
            'billingaddress': forms.TextInput(attrs={'class':'input', 'placeholder': 'Billing Address', 'maxlength':'150'}),
            'expdate': forms.DateInput(attrs={'class':'input', 'placeholder': 'YY-MM'}),
        }

class SelectPaymentForm(forms.ModelForm):
    
    class Meta:
        model = Contracts
        fields = ['paymentid']

    def __init__(self, qs, *args, **kwargs):
        super(SelectPaymentForm, self).__init__(*args, **kwargs)
        self.fields['paymentid'].queryset = qs       

class RatingForm(forms.ModelForm):

    class Meta:
        model = Rating
        fields = ['number_rating', 'title', 'comments']
        widgets = {
            'number_rating': forms.Select(choices={1, 2, 3, 4, 5}),
            'title': forms.TextInput(attrs={'class':'input', 'placeholder': 'Title', 'maxlength':'50',}),
            'comments': forms.TextInput(attrs={'class':'input', 'placeholder': 'Comments', 'maxlength':'300',}),
        }

class newServiceForm(forms.ModelForm):
    #serviceid = forms.ModelChoiceField(queryset=Services.objects.all())

    class Meta:
        model = Serviceapplications
        fields = ['serviceid', 'chargeservice', 'yearsexperience']
