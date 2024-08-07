from django.views.generic import TemplateView

# Create your views here.
class IndexView(TemplateView):
    template_name = "main/index.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Главная"
        context["content"] = "Магазин мебели Eugene"
        return context

class AboutView(TemplateView):
    template_name = "main/about.html"

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "О нас"
        context["content"] = "Текст о том какой классный этот интернет магазин."
        return context