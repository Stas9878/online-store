from django.shortcuts import render
# from templates.other_files.goods_list import goods
from .models import Products,Categories


def catalog(request):
    goods = Products.objects.all()
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