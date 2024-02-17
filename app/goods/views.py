from django.shortcuts import render
from templates.other_files.goods_list import goods

def catalog(request):
    context = {
        'goods': goods
    }

    # for i in goods:
    #     Products.objects.create(name=i['name'],
    #                             description=i['description'],
    #                             price=i['price'],
    #                             image=i['image'],
    #                             category=Categories.objects.get(id=1))

    return render(request, 'goods/catalog.html', context=context)

def product(request):
    return render(request, 'goods/product.html')