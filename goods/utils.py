

# from django.db.models import Q
from goods.models import Products

from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank, SearchHeadline


def q_search(query):

    if query == '':
        return Products.objects.all()
    
    if query.isdigit() and len(query) <= 5:
        return Products.objects.filter(id=query)
    
    vector = SearchVector("name", "description")
    query = SearchQuery(query)

    result = Products.objects.annotate(rank=SearchRank(vector, query)).filter(rank__gt=0).order_by("-rank")
    
    result = result.annotate(
        headline=SearchHeadline(
            "name",
            query,
            start_sel="<span style='background-color: yellow; '>",
            stop_sel="</span>",
        ))
    
    result = result.annotate(
        bodyline=SearchHeadline(
            "description",
            query,
            start_sel="<span style='background-color: yellow; '>",
            stop_sel="</span>",
        ))


    return result
    # keywords = [word for word in query.split() if len(word) > 2]

    # q_objs = Q()
    
    # for keyword in keywords:
    #     q_objs |= Q(name__icontains=keyword)
    #     q_objs |= Q(description__icontains=keyword)
    
    # return Products.objects.filter(q_objs)