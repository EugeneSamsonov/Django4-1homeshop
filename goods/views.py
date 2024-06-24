from django.shortcuts import render
import goods_list
# Create your views here.

def catalog(request):
    context = {
        'title': 'Catalog',
        'goods': goods_list.goods,
    }
    return render(request, 'goods/catalog.html', context)


def product(request):
    return render(request, 'goods/product.html')
