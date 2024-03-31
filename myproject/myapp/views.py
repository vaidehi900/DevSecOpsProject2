from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate

# Create your views here.

# - Homepage 

def home(request):
    
    return render(request, 'myapp/index.html')
    

# - Register a user

def register(request):

    form = CreateUserForm()

    if request.method == "POST":

        form = CreateUserForm(request.POST)

        if form.is_valid():

            form.save()

            

            return redirect("login")

    context = {'form':form}

    return render(request, 'myapp/register.html', context=context)


# - Login a user

def login(request):

    form = LoginForm()

    if request.method == "POST":

        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            form.save()

            

            # return redirect("")

    context = {'form':form}

    return render(request, 'myapp/login.html', context=context)

