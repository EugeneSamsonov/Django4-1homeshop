from django.shortcuts import render

# Create your views here.


def login(request):
    context = {
        'title': 'Вход'
    }
    
    return render(request, 'users/login.html', context)


def registration(request):
    context = {
        'title': 'Регистрация'
    }

    return render(request, 'users/registration.html', context)


def logout(request):
    context = {
        'title': 'Выход'
    }
    return render(request, 'users/logout.html', context)

def profile(request):
    context = {
        'title': 'Профиль'
    }
    return render(request, 'users/profile.html', context)

