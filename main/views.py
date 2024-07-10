from django.shortcuts import render

from goods.models import Categories

# Create your views here.


def index(request):
    context = {
        "title": "Главная",
        "content": "Магазин мебели Eugene",
    }
    return render(request, "main/index.html", context)


def about(request):
    context = {
        "title": "О нас",
        "content": "Текст о том какой классный этот интернет магазин.",
    }
    return render(request, "main/about.html", context)
