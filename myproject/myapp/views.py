from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm

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

            

            # return redirect("login")

    context = {'form':form}

    return render(request, 'myapp/register.html', context=context)

