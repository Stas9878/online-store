from django.shortcuts import get_list_or_404, render
# from templates.other_files.goods_list import goods
from .models import Products,Categories


def catalog(request, category_slug):
    if category_slug == 'all':
        goods = Products.objects.all()
    else:
        goods = get_list_or_404(Products.objects.filter(category__slug=category_slug))
        
    context = {
        'goods': goods
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