from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        "posts": [
            "Officia anim exercitation in sit voluptate culpa qui aliqua eiusmod eu deserunt" 
            "pariatur.",
            "Velit ea voluptate do ut anim nostrud commodo ut duis cupidatat sunt anim officia.",
            "Eiusmod velit sint consequat eiusmod.",
        ],
        "is_need_to_view": True,
        "title": "Main",
    }

    return render(request, "main/index.html", context)


def about(request):
    return HttpResponse("This is a page about me!<br><br> I love bananas")

def aboutus(request):
    return HttpResponse("This is a page about me!<br><br> I love bananas")
