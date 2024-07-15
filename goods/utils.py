

from django.db.models import Q
from goods.models import Products


def q_search(query):

    if query.isdigit() and len(query) <= 5:
        return Products.objects.filter(id=query)
    
    keywords = [word for word in query.split() if len(word) > 2]

    q_objs = Q()
    
    for keyword in keywords:
        q_objs |= Q(name__icontains=keyword)
        q_objs |= Q(description__icontains=keyword)
    
    
    return Products.objects.filter(q_objs)