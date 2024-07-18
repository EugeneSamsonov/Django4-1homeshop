from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

from users.forms import UserLoginForm, UserRegistrationForm

# Create your views here.


def login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()

    context = {
        'title': 'Вход',
        'form': form
    }
    
    return render(request, 'users/login.html', context)


def registration(request):
    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserRegistrationForm()

    context = {
        'title': 'Вход',
        'form': form
    }
    
    return render(request, 'users/registration.html', context)


def logout(request):
    auth.logout(request)
    return redirect(reverse("main:index"))

def profile(request):
    context = {
        'title': 'Профиль'
    }
    return render(request, 'users/profile.html', context)

