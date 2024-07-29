from django.shortcuts import render

# Create your views here.

def create_order(request):
    context = {
        "title": "Профиль"
    }
        
    return render(request, "orders/create_order.html", context)