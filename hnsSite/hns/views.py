from django.shortcuts import render
from django.http import HttpResponse

from .forms import *

# Create your views here.

def index(request):
    return render(request, 'home.html')

def services_list(request):
    return render(request, 'servicesList.html')

def becomeContractor(request):
    return render(request, 'becomeAContractor.html')

def login(request):
    '''
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    '''
    form = LoginUserForm()
    context = {'form':form}
    return render(request, 'login.html', context)