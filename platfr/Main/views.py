from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .form import RegisterForm



def home():

    pass

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.isvalid():
            print("cool")
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            Cohort   = form.cleaned_data.get("Cohort")
            (username, password, Cohort)
            user = authenticate(username=username,password=password,Cohort=Cohort)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                print("Authentication failed")
                form.add_error(None, "Invalid username or password or cohort")

    else:
        form = AuthenticationForm()

    return render(request, 'registration/login.html', {'form': form})

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        print("Form submitted")
        if form.is_valid():
            print("Form is Valid")
            user = form.save()
            print(f"User created: {user.username}")
            login(request, user)
            return redirect("/home")
        else:
            print("Form errors:", form.errors)

    else:
        form = RegisterForm()
    return render(request, "register/register.html", {"form": form})

# Create your views here.
