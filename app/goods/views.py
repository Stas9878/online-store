from django.shortcuts import get_list_or_404, render
# from templates.other_files.goods_list import goods
from django.core.paginator import Paginator
from .models import Products,Categories


def catalog(request, category_slug):
    page = request.GET.get('page', 1)

    if category_slug == 'all':
        goods = Products.objects.all()
    else:
        goods = get_list_or_404(Products.objects.filter(category__slug=category_slug))
    
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