from django.shortcuts import get_list_or_404, render
# from templates.other_files.goods_list import goods
from django.core.paginator import Paginator
from .models import Products,Categories
from .utils import q_search


def catalog(request, category_slug=None):
    page = request.GET.get('page', 1)
    on_sale = request.GET.get('on_sale', None)
    order_by = request.GET.get('order_by', None)
    query = request.GET.get('q', None)

    if category_slug == 'all':
        goods = Products.objects.all()
    elif query:
        goods = q_search(query)
    else:
        goods = get_list_or_404(Products.objects.filter(category__slug=category_slug))
    
    if on_sale:
        goods = goods.filter(discount__gt=0)
    if order_by and order_by != 'default':
        goods = goods.order_by(order_by)

    
    paginator = Paginator(goods, 3)
    current_page = paginator.page(int(page))

    context = {
        'goods': current_page,
        'slug': category_slug,
    }

    # for i in goods:
    #     Products.objects.create(name=i['name'],
    #                             description=i['description'],
    #                             price=i['price'],
    #                             image=i['image'].split('/')[-1],
    #                             category=Categories.objects.get(id=1))

    return render(request, 'goods/catalog.html', context=context)

def product(request, slug):
    product = Products.objects.get(slug=slug)
    context = {
        'product': product
    }
    return render(request, 'goods/product.html', context=context)