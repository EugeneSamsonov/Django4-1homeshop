from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from django.db.models import Prefetch, prefetch_related_objects
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

from carts.models import Cart
from orders.models import Order, OrderItem
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

            session_key = request.session.session_key

            if user:
                auth.login(request, user)
                messages.success(request, f"{user.username}, вы успешно вошли в аккаунт")
                
                if session_key:
                    # delete old authorized user carts
                    forgot_carts = Cart.objects.filter(user=user)
                    if forgot_carts.exists():
                        forgot_carts.delete()
                    # add new authorized user carts from anonimous session

                Cart.objects.filter(session_key=session_key).update(user=user)

                redirect_page = request.POST.get('next', None)
                if redirect_page and redirect_page != reverse('user:logout'):
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

            session_key = request.session.session_key

            auth.login(request, user)
            messages.success(request, f"{user.username}, вы успешно зарегистрировались и вошли в аккаунт")

            if session_key:
                    Cart.objects.filter(session_key=session_key).update(user=user)
                    
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

    orders = Order.objects.filter(user=request.user).prefetch_related(
        Prefetch(
            "orderitem_set",
            queryset=OrderItem.objects.select_related("product"),
        )
    ).order_by("-id")

    context = {
        "title": "Профиль", 
        "form": form,
        "orders": orders,
    }
    
    return render(request, "users/profile.html", context)


@login_required
def logout(request):
    auth.logout(request)
    messages.success(request, "Вы вышли из аккаунта")
    return redirect(reverse("main:index"))


def user_cart(request):
    context = {
        'title': 'Корзина'
    }

    return render(request, "users/user_cart.html", context)