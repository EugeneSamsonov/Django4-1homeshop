from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

from users.forms import ProfileForm, UserLoginForm, UserRegistrationForm

# Create your views here.


def login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = auth.authenticate(
                username=request.POST["username"], 
                password=request.POST["password"]
            )
            if user:
                auth.login(request, user)
                messages.success(request, f"{user.username}, вы успешно вошли в аккаунт")
                
                if request.POST.get('next'):
                    return HttpResponseRedirect(request.POST.get('next'))
                
                return HttpResponseRedirect(reverse("main:index"))
    else:
        form = UserLoginForm()

    context = {
        "title": "Вход", 
        "form": form
    }

    return render(request, "users/login.html", context)


def registration(request):
    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            messages.success(request, f"{user.username}, вы успешно зарегистрировались и вошли в аккаунт")
            return HttpResponseRedirect(reverse("main:index"))
    else:
        form = UserRegistrationForm()

    context = {
        "title": "Регистрация", 
        "form": form
        }

    return render(request, "users/registration.html", context)


@login_required
def profile(request):
    if request.method == "POST":
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse("user:profile"))
    else:
        form = ProfileForm(instance=request.user)

    context = {
        "title": "Профиль", 
        "form": form
        }
    
    return render(request, "users/profile.html", context)


@login_required
def logout(request):
    auth.logout(request)
    messages.success(request, "Вы вышли из аккаунта")
    return redirect(reverse("main:index"))
