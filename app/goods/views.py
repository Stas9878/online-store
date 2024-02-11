from django.shortcuts import render
from templates.other_files.goods_list import goods

def catalog(request):
    context = {
        'goods': goods
    }
    return render(request, 'goods/catalog.html', context=context)

def product(request):
    return render(request, 'goods/product.html')