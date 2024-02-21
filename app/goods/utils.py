from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank, SearchHeadline
from .models import Products

def annotate_result_search(result_search, query):
    result_search = result_search.annotate(
        headline=SearchHeadline(
        "name",
        query,
        start_sel="<span style='background-color: yellow;'>",
        stop_sel="</span>",
        )
    )

    result_search = result_search.annotate(
        bodyline=SearchHeadline(
        "description",
        query,
        start_sel="<span style='background-color: yellow;'>",
        stop_sel="</span>",)
    )

    return result_search

def q_search(query):
    if query.isdigit() and len(query) <= 5:
        return Products.objects.filter(id=int(query))
    
    vector = SearchVector('name', 'description')
    query = SearchQuery(query)
    result_search = Products.objects.annotate(rank=SearchRank(vector, query)).filter(rank__gt=0).order_by('-rank')
    return annotate_result_search(result_search, query)