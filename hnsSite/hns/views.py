from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'home.html')

def services_list(request):
    return render(request, 'servicesList.html')

def becomeContractor(request):
    return render(request, 'becomeAContractor.html')

def login(request):
    return render(request, 'login.html')