from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import *


def Login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f" wecome {username} !!")
            return redirect("index")
        else:
            messages.info(request, f"account done not exit plz sign in")
    form = AuthenticationForm()
    data = {"form": form}
    return render(request, "users/login.html", data)


def Register(request):
    if request.method == "POST":
        pass
    form = RegisterForm()
    data = {"form": form, "title": Register}
    return render(request, "users/register.html", data)


def Profile(request):
    if request.method == "POST":
        pass
    form = RegisterForm()
    data = {"form": form}
    return render(request, "users/profile.html", data)
