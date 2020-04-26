from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

from .forms import *

# Create your views here.

def index(request):
    return render(request, 'home.html')

def services_list(request):
    services = Services.objects.all()
    serviceCategories = Servicecategories.objects.all()

    context = {'services':services, 'serviceCategories':serviceCategories}

    return render(request, 'servicesList.html', context)

def becomeContractor(request):
    form = NewContractorForm()
    context = {'form':form}
    return render(request, 'becomeAContractor.html', context)

def login(request):
    if request.method == 'POST':
        form = form = LoginUserForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                #messages.info(request, f"You are now logged in as {username}")
                return redirect('index')
            else:
                messages.error(request, "Invalid username or password.")
    
    form = LoginUserForm()
    context = {'form':form}
    return render(request, 'login.html', context)

def createUserAccount(request):
    form = NewUserForm()
    context = {'form':form}
    return render(request, 'createNewUser.html', context)

def userProfile(request):
    context = {'user': request.user}
    return render(request, 'user/userProfile.html',context)