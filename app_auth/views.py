from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import LoginForm, RegisterForm

def login_hotel(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            pwd = form.cleaned_data['pwd']
            user = authenticate(username=username, password=pwd)
            if user is not None:
                login(request, user)
                return redirect('dashboard1')
            else:
                messages.error(request, "Erreur d'authentification. Nom d'utilisateur et Mot de passe ne correspond pas 😥")
                context = {"forms": form}
                return render(request, "login.html", context)
        else:
            for field in form.errors:
                form[field].field.widget.attrs['class'] += ' is-invalid'
            context = {"forms": form}
            return render(request, "login.html", context)
    else:
        form = LoginForm()
        context = {"forms": form}
        return render(request, "login.html", context)


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            pwd = form.cleaned_data['pwd']
            email = form.cleaned_data['email']
            user = User.objects.create_user(username=username, password=pwd, email=email)
            if user is not None:
                return redirect("login-hotel1")
            else:
                messages.error(request, "Création de compte échouée 😥")
                context = {"forms": form}
                return render(request, "register.html", context)
        else:
            for field in form.errors:
                form[field].field.widget.attrs['class'] += ' is-invalid'
            context = {"forms": form} 
            return render(request, "register.html", context)
    else:
        form = RegisterForm()
        context = {"forms": form}
        return render(request, "register.html", context)

def logout_hotel(request):
    logout(request)
    return redirect('login-hotel1')

