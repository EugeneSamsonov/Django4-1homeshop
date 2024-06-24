from django.shortcuts import render

from goods.models import Categories

# Create your views here.


def index(request):
    categories = Categories.objects.all()
    context = {
        "title": "Главная",
        "content": "Магазин мебели Eugene",
        "categories": categories
    }
    return render(request, "main/index.html", context)


def about(request):
    context = {
        "title": "О нас",
        "content": "Текст о том какой классный этот интернет магазин.",
    }
    return render(request, "main/about.html", context)


def posts(request):
    context = {
        "posts": [
            "Officia anim exercitation in sit voluptate culpa qui aliqua eiusmod eu deserunt" 
            "pariatur.",
            "Velit ea voluptate do ut anim nostrud commodo ut duis cupidatat sunt anim officia.",
            "Eiusmod velit sint consequat eiusmod.",
        ],
        "is_need_to_view": True,
        "title": "Посты",
        "content": "Посты",
    }
    return render(request, 'main/posts.html', context)
