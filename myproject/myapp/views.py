from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm, CreateRecordForm, UpdateRecordForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate

from django.contrib.auth.decorators import login_required

from .models import Record

from django.contrib import messages

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

            messages.success(request, "Account created successfully!")

            return redirect("login")

    context = {'form':form}

    return render(request, 'myapp/register.html', context=context)


# - Login a user

def login(request):

    form = LoginForm()

    if request.method == "POST":

        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:

                auth.login(request, user)

                return redirect("dashboard")

    context = {'form':form}

    return render(request, 'myapp/login.html', context=context)

            



# - Dashboard

@login_required(login_url='login')
def dashboard(request):
    
    my_records = Record.objects.all()

    context = {'records': my_records}

    return render(request, 'myapp/dashboard.html', context=context)
    


# - User logout

def logout(request):

    auth.logout(request)
    
    messages.success(request, "Logout success!")

    return redirect("login")


# - Create a record 


@login_required(login_url='login')
def create(request):
    
    form = CreateRecordForm()

    if request.method == "POST":

        form = CreateRecordForm(request.POST)

        if form.is_valid():

            form.save()
            
            messages.success(request, "Your record was created!")

            return redirect("dashboard")

    context = {'form': form}

    return render(request, 'myapp/create.html', context=context)
    
    
    
# - Update a record 

@login_required(login_url='login')
def update(request, pk):

    record = Record.objects.get(id=pk)

    form = UpdateRecordForm(instance=record)

    if request.method == 'POST':

        form = UpdateRecordForm(request.POST, instance=record)

        if form.is_valid():

            form.save()

            messages.success(request, "Your record was updated!")

            return redirect("dashboard")
        
    context = {'form':form}

    return render(request, 'myapp/update.html', context=context)
    

# - Read / View a singular record

@login_required(login_url='login')
def singular_record(request, pk):

    all_records = Record.objects.get(id=pk)

    context = {'record':all_records}

    return render(request, 'myapp/view.html', context=context)
    
# - Delete a record

@login_required(login_url='login')
def delete(request, pk):

    record = Record.objects.get(id=pk)

    record.delete()

    messages.success(request, "Your record was deleted!")

    return redirect("dashboard")



